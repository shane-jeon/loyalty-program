"""GlowUp Server"""

## from the flask library, import ...
from flask import (
    Flask,
    session,
    render_template,
    request,
    jsonify,
    flash,
    redirect,
    url_for,
    Blueprint)
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import (
    login_user,
    LoginManager,
    login_required,
    logout_user,
    current_user,
    UserMixin
    )
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, ValidationError
from wtforms.fields.html5 import URLField
from flask_bcrypt import Bcrypt
from model import BusinessUser, connect_to_db
from sqlalchemy.sql import text
import crud
from jinja2 import StrictUndefined
# from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "*xZJ_0d7c#+ii0C"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_business_user(business_user_id):
    return BusinessUser.query.get(business_user_id)


#################################################
#################################################
###############  registration     ################
###############   login       ##################
#################################################
#################################################

# created registration form that inherits from FlaskForm
class RegisterForm(FlaskForm):
    """Register user form."""
    # StringField allows user to see characters
    # InputRequired() --> must be filled out
    # min and max for characters username, placeholder is placeholder for Username, use with render_kw

    bu_email = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "E-mail"})

    bu_username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})

    # instead use PasswordField, will show black dots
    # minimum difference is because password will hash (not sure how long, so in db is set to 80)
    bu_password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})

    bu_name = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Full Name"})

    bu_business = StringField(validators=[InputRequired(), Length(
    min=4, max=80)], render_kw={"placeholder": "Business Name"})

    bu_pic_path = StringField(validators=[InputRequired(), Length(
        min=4, max=500)], render_kw={"placeholder": "Profile Picture (optional) "})

    # button to register
    submit = SubmitField("Register")

    # validates if there is username that has already been typed in
    # queries database, checks if similar username
    def validate_bu_username(self, bu_username):
        existing_business_user_bu_username = crud.get_business_user_by_username(bu_username=bu_username.data)

        if existing_business_user_bu_username:
            raise ValidationError(
                "That username already exists. PLease choose a different one.")

class LoginForm(FlaskForm):

    # StringField allows user to see characters
    # InputRequired() --> must be filled out
    # min and max for characters username, placeholder is placeholder for Username, use with render_kw
    bu_username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    print(bu_username)

    # instead use PasswordField, will show black dots
    # minimum difference is because password will hash (not sure how long, so in db is set to 80)
    bu_password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})

    # button to register
    submit = SubmitField("Login")


#################################################
#################################################
###############   login, logout &   ##############
###############  registration  ##################
#################################################
#################################################



@app.route('/')
## view function: function that returns web response (response is string, usually HTML)
def index():
    """Show index."""
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # print(form.bu_username.data)
        # print(type(form.bu_username.data))
        # print("got here")
        business_user = crud.get_business_user_by_username(form.bu_username.data)
        print(form.bu_username.data)
        # print("got here 2")
        print(business_user)
        if business_user:
            # print("hey2")
            # print(business_user.bu_password, form.bu_password.data)
            if bcrypt.check_password_hash(business_user.bu_password, form.bu_password.data):
                print(form.bu_password.data)
                login_user(business_user)
                # print("got here")
                # return redirect(url_for(f'directory/{business_user.business_user_id}'))
                return redirect(url_for('directory', business_user_id = business_user.business_user_id))
                

    return render_template('login.html', form=form)


@app.route("/register", methods=['GET','POST'])
# @auth.route("/register", methods=['GET','POST'])
def register():
    form = RegisterForm()
    # EDGE CASE ==> PREVENT USER FROM ENTERING USERNAME WITH SPACES
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.bu_password.data).decode('utf-8')
        # print(hashed_password)

        crud.create_business_user(form.bu_email.data,
                                  form.bu_username.data,
                                  hashed_password,
                                  form.bu_name.data,
                                  form.bu_business.data,
                                  form.bu_pic_path.data)

        

        return redirect(url_for('login'))

    return render_template('register.html', form=form)

# @app.route("/register", methods=['GET','POST'])
# # @auth.route("/register", methods=['GET','POST'])
# def register():
#     """Register new business user."""

#     if request.method == 'POST':
#         bu_email = request.form.get("registration-email")
#         bu_password_hash = request.form.get("registration-password")
#         bu_name = request.form.get("name")
#         bu_business = request.form.get("business")
#         bu_pic_path = request.form.get("pic_path")
#         print(bu_email)
#         print(bu_password_hash)


#         business_user = crud.get_business_user_by_email(bu_email)
#         print(business_user)

#         if business_user:
#             flash("There's already an account with that e-mail! Try again.")
#         else:
#             crud.create_business_user(bu_email, bu_password_hash, bu_name, bu_business, bu_pic_path)
#             flash("Account created! Please log in.")
    
#         return redirect("/login")
    
#     return render_template('register.html')


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """Process user login."""

#     if request.method == 'POST':
#         session.pop('bu_email', None)
#         bu_email = request.form.get("login-email")
#         bu_password_hash = request.form.get("login-password")
#         # print(bu_email)
#         # print(bu_password_hash)

#         business_user = crud.get_business_user_by_email(bu_email)

 
#         # # adjust bu_password later and in html
#         if not business_user or business_user.bu_password_hash != bu_password_hash:
#             flash("The e-mail or password you entered is incorrect. Try again.")

#             return redirect("/login")

#         elif business_user == business_user and business_user.bu_password_hash == bu_password_hash:
#             session["bu_email"] = business_user.bu_email
#             flash(f"Weßlcome back {business_user.bu_name}!")

#             return redirect(f"/directory/{business_user.business_user_id}")
    
#     return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

#################################################
#################################################
###############   DIRECTORY     ##################
#################################################
#################################################


# shows directory for corresponding business user id
@app.route("/directory/<business_user_id>")
# @login_required
def directory(business_user_id):
    """Show business user's directory."""
    
    # business_user = in crud.py call function "get_business_user_by_id(business_user_id"
    business_user = crud.get_business_user_by_id(business_user_id)
    print(business_user)
    clients = crud.show_all_client()
    rewards = crud.show_all_reward()
    # client = in crud.py call function "get_client_by_id(client_id)"
    # client = crud.get_client_by_id(client_id)

    # returns TEMPLATE, and variable from above w/field
    return render_template('directory.html',business_user=business_user, clients=clients, rewards=rewards)



#################################################
#################################################
###############   CLIENTS     ##################
#################################################
#################################################

#####################    @APP.ROUTE/NEW_CLIENT     ###############################

@app.route("/new_client/<business_user_id>")
def new_client_form(business_user_id):
    """Show form to sign up a new client."""
    
    business_user = crud.get_business_user_by_id(business_user_id)

    return render_template('register_client.html', business_user=business_user)

################  @APP.ROUTE("/NEW_CLIENT_SIGNUP").  ##############################

@app.route("/new_client_signup", methods=['POST'])
def signup_new_client():
    """Add new client to business user's profile"""

    client_name = request.form.get("name")
    client_email = request.form.get("email")
    # change to business_user for consistency 10/16 8:40pm
    # NVM 8:42pm bu_email is for FORM and NOT "dictionary"
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

        # return redirect("/new_client")
    else:
        crud.create_client(client_name, client_email, business_user)
        flash("New client added.")
    
    return redirect("/new_client/<business_user_id>")

#################  @APP.ROUTE("/CLIENTS/<BUSINESS_USER_ID>/<CLIENT_ID>/<REWARD_ID>")  #################

@app.route("/new_client/<business_user_id>/<client_id>/<reward_id>")
def edit_client_rewards(business_user_id, client_id, reward_id):
    """Show form to sign up a new client."""
    
    business_user = crud.get_business_user_by_id(business_user_id)
    client = crud.get_client_by_id(client_id)
    rewards = crud.get_reward_by_id(reward_id)

    return render_template('register_client.html', business_user=business_user, client=client, rewards=rewards)


#################  @APP.ROUTE("/CLIENTS/<BUSINESS_USER_ID>/<CLIENT_ID>")  #################

# shows directory for corresponding business user id
@app.route("/clients/<business_user_id>/<client_id>")
def client_profile(business_user_id, client_id):
    """Show client profile."""
    
    # business_user = in crud.py call function "get_business_user_by_id(business_user_id"
    client = crud.get_client_by_id(client_id)
    transactions = crud.show_all_transaction()
    business_user = crud.get_business_user_by_id(business_user_id)
 

    # returns TEMPLATE, and variable from above w/field
    return render_template('client_profile.html',client=client, transactions=transactions, business_user=business_user)


#################################################################################


@app.route("/edit_rewards/<business_user_id>/<client_id>", methods=['GET', 'POST'])
def edit_client_reward(business_user_id, client_id):
    """Allows user to edit a client's points, rewards."""
    
    business_user = crud.get_business_user_by_id(business_user_id)
    client = crud.get_client_by_id(client_id)
    rewards = crud.show_all_reward()
    # rewards = crud.get_reward_by_id(reward_id)

    return render_template('edit_reward.html', business_user=business_user, client=client, rewards=rewards)


@app.route("/adjusting_points", methods=['POST'])
def adjusting_points():
    """Adjust user points."""

    reward_point = int(request.form.get('plus-count'))
    client_id = request.form.get('client_id')
    business_user_id = request.form.get('business_user_id')
    # print(client_id)
    # print(type(client_id))
    # print(reward_point)
    # print(type(reward_point))

    business = crud.get_business_user_by_id(business_user_id)
    client = crud.get_client_by_id(client_id)

    client_point = crud.adjust_client_points(client_id, reward_point)
    # print("got here")


    total_client_point = client.reward_point

    # flash(f"{total_client_point}")
    return redirect(f"/edit_rewards/{business.business_user_id}/{client.client_id}")
    # return flash(f"{total_client_point}")


# susie and bob (query parameters) or add in route
# /add_transaction/susie/bob
# /add_transaction?bu=susie&cu=bob
# /add_transction/susie?cu=bob


# @app.route('/data/bu=<business_user_id>', methods=['GET'])
# def get_query_string():
#     return request.query_string



#################################################
#################################################
###############  TRANSACTIONS  ##################
#################################################
#################################################


################  @APP.ROUTE("/ADD_TRANSACTION/<BUSINESS_USER_ID/<CLIENT_ID>").  ####################
@app.route('/add_transaction/<business_user_id>/<client_id>')
def show_transaction_page(business_user_id,client_id):
    """Show form to add client transaction"""
    # change to singular later
    # "clients" is a way to tap into database THEN use crud function to grab w/e
    business_user = crud.get_business_user_by_id(business_user_id)
    clients = crud.get_client_by_id(client_id)

    # SOOOOOO clients = clients is so i can put that before whatever attribute i need
    return render_template('add_transaction.html',business_user=business_user,clients=clients)

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
    business_user = crud.get_business_user_by_id(business_user_id)

    return render_template('add_reward.html', business_user=business_user, rewards=rewards)

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
    crud.create_reward(reward_type, reward_cost)
    
    flash("Reward added.")

    return redirect(f"/rewards/{ business_user_id }")


## if this script is being called directly, than run(method) app(instance) 
## need to let module to scan for routes when creating a Flask application
if __name__ == "__main__":
    #DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)