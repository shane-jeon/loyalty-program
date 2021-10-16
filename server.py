"""GlowUp Server"""

## from the flask library, import ...
from flask import (Flask, session, render_template, request, jsonify, flash, redirect)
from flask_debugtoolbar import DebugToolbarExtension
from model import BusinessUser, connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "sk"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#################################################
#################################################
###############   login &      ##################
###############  registration  ##################
#################################################
#################################################

@app.route('/')
## view function: function that returns web response (response is string, usually HTML)
def homepage():
    """Show homepage."""
    
    return render_template('homepage.html')

@app.route("/register")
def render_form():
    # purely for display NOT action
    return render_template('register.html')

@app.route("/registration", methods=['POST'])
def register_user():
    """Register new business user."""

    bu_email = request.form.get("registration-email")
    bu_password_hash = request.form.get("registration-password")
    bu_name = request.form.get("name")
    bu_business = request.form.get("business")
    bu_pic_path = request.form.get("pic_path")
    # print(bu_email)
    # print(bu_password_hash)


    business_user = crud.get_business_user_by_email(bu_email)
    print(business_user)

    if business_user:
        flash("There's already an account with that e-mail! Try again.")
    else:
        crud.create_business_user(bu_email, bu_password_hash, bu_name, bu_business, bu_pic_path)
        flash("Account created! Please log in.")
    
    return redirect("/")

@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    bu_email = request.form.get("login-email")
    bu_password_hash = request.form.get("login-password")
    print(bu_email)
    print(bu_password_hash)

    business_user = crud.get_business_user_by_email(bu_email)

    # adjust bu_password later and in html
    if not business_user or business_user.bu_password_hash != bu_password_hash:
        flash("The e-mail or password you entered is incorrect. Try again.")

        return redirect("/")

    else:
        session["bu_email"] = business_user.bu_email
        flash(f"Welcome back {business_user.bu_name}!")

        return redirect(f"/directory/{business_user.business_user_id}")



#################################################
#################################################
###############   DIRECTORY     ##################
#################################################
#################################################


# shows directory for corresponding business user id
@app.route("/directory/<business_user_id>")
def directory(business_user_id):
    """Show business user's directory."""
    
    # business_user = in crud.py call function "get_business_user_by_id(business_user_id"
    business_user = crud.get_business_user_by_id(business_user_id)
    clients = crud.show_all_client()
    # client = in crud.py call function "get_client_by_id(client_id)"
    # client = crud.get_client_by_id(client_id)

    # returns TEMPLATE, and variable from above w/field
    return render_template('directory.html',business_user=business_user, clients=clients)



#################################################
#################################################
###############   CLIENTS     ##################
#################################################
#################################################

#####################    @APP.ROUTE/NEW_CLIENT     ###############################

@app.route("/new_client")
def new_client_form():
    """Show form to sign up a new client."""
    
    return render_template('register_client.html')

################  @APP.ROUTE("/NEW_CLIENT_SIGNUP").  ##############################

@app.route("/new_client_signup", methods=['POST'])
def signup_new_client():
    """Add new client to business user's profile"""

    client_name = request.form.get("name")
    client_email = request.form.get("email")
    bu_email = request.form.get("bu_email")
    # print(business_email)
    # RETURN TO CHANGE
    # print(bu_email)
    # print(bu_password_hash)


    client = crud.get_client_by_email(client_email)
    business_user = crud.get_business_user_by_email(bu_email)
    # print(client)

    if client:
        flash("There's already a client with that e-mail! Try again.")

        return redirect("/new_client")
    else:
        crud.create_client(client_name, client_email, business_user)
        flash("New client added.")
    
        return redirect("/new_client")

###################  @APP.ROUTE("/CLIENTS/<CLIENT_ID>")  ###########################

# shows directory for corresponding business user id
@app.route("/clients/<client_id>")
def client_profile(client_id):
    """Show client profile."""
    
    # business_user = in crud.py call function "get_business_user_by_id(business_user_id"
    client = crud.get_client_by_id(client_id)
    transactions = crud.show_all_transaction()
    business_user = crud.show_all_business_user()
    # client = in crud.py call function "get_client_by_id(client_id)"
    # client = crud.get_client_by_id(client_id)

    # returns TEMPLATE, and variable from above w/field
    return render_template('client_profile.html',client=client, transactions=transactions, business_user=business_user)


#################################################################################


#################################################
#################################################
###############  TRANSACTIONS  ##################
#################################################
#################################################


################  @APP.ROUTE("/ADD_TRANSACTION/<CLIENT_ID>").  ####################
@app.route('/add_transaction/<client_id>')
def show_transaction_page(client_id):
    """Show form to add client transaction"""
    # change to singular later
    clients = crud.get_client_by_id(client_id)

    return render_template('add_transaction.html',clients=clients)

##################  @APP.ROUTE("/NEW_TRANSACTION").  ##############################

@app.route('/new_transaction', methods=['POST'])
def add_transaction():
    """Add transaction to client profile."""

    # assigning variable to get entry from html form
    transaction_date = request.form.get('transaction_date')
    appointment_type = request.form.get('appointment_type')
    total_cost = request.form.get('total_cost')
    client_id = request.form.get("client_id")

    # transaction = crud.get_transaction_by_id(transaction_id)
    # clients = crud.get_client_by_id(client_id)

    client = crud.get_client_by_id(client_id)
    # calling crud function
    crud.create_transaction(transaction_date, appointment_type, total_cost, client)
    flash("Transaction added.")

    return redirect(f"/add_transaction/{client.client_id}")


#################################################
#################################################
###############    REWARDS     ##################
#################################################
#################################################

################  @APP.ROUTE("/REWARDS/<BUSINESS_USER_ID") ########################

@app.route("/rewards/<business_user_id>")
def show_rewards_page(business_user_id):

    rewards = crud.show_all_reward
    business_users = crud.get_business_user_by_id(business_user_id)

    return render_template('add_reward.html', business_users=business_users)

########################  @APP.ROUTE("/ADD_REWARDS")  ##############################

@app.route("/add_rewards", methods=["POST"])
def add_reward():
    """Adds new reward for business user."""

    reward_type = request.form.get('reward_type')
    reward_cost = request.form.get('reward_cost')
    business_user_id = request.form.get('business_user_id')
 
    # RETURNS LIST OF BUSINESS USER, WILL NEED TO ITERATE TO GRAB BU_ID
    # business_user = crud.show_all_business_user()
   
#    MY ERROR, CAN ADD BUSINESS_USER_ID BUT NEED TO ADD AS HIDDEN INPUT
    business = crud.get_business_user_by_id
    # print(business_user_id)
    crud.create_reward(reward_type, reward_cost, business_user_id)
    
    flash("Reward added.")

    return redirect(f"/rewards/{ business.business_user_id}")

## if this script is being called directly, than run(method) app(instance) 
## need to let module to scan for routes when creating a Flask application
if __name__ == "__main__":
    #DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)