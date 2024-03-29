"""GlowUp Server"""

import os

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

from wtforms.validators import InputRequired, DataRequired, Length, ValidationError, Optional

from wtforms.fields.html5 import URLField

from flask_bcrypt import Bcrypt

# to check for secure filename during image upload
from werkzeug.utils import secure_filename

from urllib.parse import urlunsplit, urlencode

from model import BusinessUser, connect_to_db

from sqlalchemy.sql import text

import crud

from jinja2 import StrictUndefined


# Creating instance of class, first argument is name of application's module
# __name__ is needed so Flask knows where to look for resources such as...
# ... templates and static files
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "*xZJ_0d7c#+ii0C"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_business_user(id):
    return BusinessUser.query.get(id)



################################################
#############   registration     ###############
#############     login       ##################
################################################


# created registration form that inherits from FlaskForm
class RegisterForm(FlaskForm):
    """Creates registration form, inheriting from FlaskForm"""
    # StringField allows user to see characters

    bu_email = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "E-mail"})

    bu_username = StringField(validators=[InputRequired(), Length(
        min=4, max=20, message='Username length must be between %(min)d and %(max)dcharacters')], render_kw={"placeholder": "Username"})

    # instead use PasswordField, will show black dots
    bu_password_original = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})

    bu_name = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Full Name"})

    bu_business = StringField(validators=[InputRequired(), Length(
    min=4, max=80)], render_kw={"placeholder": "Business Name"})

    bu_pic_path = StringField(validators=[Optional(), Length(
        min=4, max=500)], render_kw={"placeholder": "Profile Picture (optional) "})

    submit = SubmitField("Register")

    # validates if there is username that has already been typed in
    # queries database, checks if similar username
    def validate_bu_username(self, bu_username):
        """Queries database to check if entered username already exists.
        
        Restricts certain characters. If restricted character entered,
        Validation Error is raised. Else, if username already exists,
        raise Validation Error."""

        excluded_chars = " *?!'^+%&/()=}][{$#"

        for char in self.bu_username.data:
            if char in excluded_chars:
                raise ValidationError(f"Character {char} is not allowed in a username.")

        existing_business_user_bu_username = crud.get_business_user_by_username(bu_username=bu_username.data)

        if existing_business_user_bu_username:
            raise ValidationError(
                "That username already exists. Please choose a different one.")

    def validate_bu_password(self, bu_password_original):
        """Restricts user from entering a space in password.

        Was unable to figureout how to prevent user from
        using 'easy' password """

        excluded_chars = ' '
        # required_chars = "~`! @#$%^&*()_-+={[}]|\:;'<,>.?/"
        # required_nums = "0123456789"
        # alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
        # alphabet_upper = alphabet_lower.upper()

        for char in self.bu_password_original.data:
            if char in excluded_chars:
                raise ValidationError("Password cannot include spaces.")

            # elif char not in required_chars and required_nums and alphabet_lower and alphabet_upper:
            #     raise ValidationError("Your password needs to be stronger")

class LoginForm(FlaskForm):
    """Uses WTForms for Login, inherits from FlaskForm."""

    bu_username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    print(bu_username)

    # Using PasswordField, will show black dots
    bu_password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})

    submit = SubmitField("Login")


#################################################
###########    login, logout &      #############
############     registration     ###############
#################################################


#########################################    VIEWS    ###################################################

# route() decorator tells Flask what URL should trigger function
# route() decorator also binds a function to a URL
# function will ten return message I want displayed in user's browser
# default content type is HTML (so render template or enter HTML)
@app.route('/')
def index():
    """Show index.html at localhost:5000."""
    
    if session: 
        return render_template('index.html')

    else:
        return redirect (f"/directory/{{bu_id}}")


#########################################    @APP.ROUTE/login    ###################################################
@app.route("/login")
def login():
    """Renders login.html template."""

    form = LoginForm()
    return render_template('login.html', form=form)


#############################################    @APP.ROUTE/login_form    ##########################################
@app.route("/login_form", methods=["POST"])
def login_form():
    """Route for login form POST request."""

    form = LoginForm()
    if form.validate_on_submit():
        business_user = crud.get_business_user_by_username(form.bu_username.data)
        if business_user:
            if bcrypt.check_password_hash(business_user.bu_password, form.bu_password.data):
                login_user(business_user, remember=True)
                session["bu_username"] = form.bu_username.data
                print("session")
                print(session)
        else:
            flash("username or password not recognized.")
            return redirect('/login')
        return redirect(f'/directory/{business_user.id}')


#############################################    @APP.ROUTE/register    #############################################
@app.route("/register", methods=['GET','POST'])
def register():
    """Renders register.html template, and route for 'user-registration' form POST request."""

    form = RegisterForm(request.form)
    # EDGE CASE ==> PREVENT USER FROM ENTERING USERNAME WITH SPACES (done 10/26)
    bu_email = form.bu_email.data

    check_user = crud.get_business_user_by_email(bu_email)

    if check_user:
        flash("Email address already exists to another user.")
        return redirect(url_for('register'))


    elif form.validate_on_submit():
        crud.create_business_user(form.bu_email.data,
                                form.bu_username.data,
                                form.bu_password_original.data,
                                form.bu_name.data,
                                form.bu_business.data,
                                form.bu_pic_path.data)

        return redirect(url_for('login'))

    return render_template('register.html', form=form)

#############################################    @APP.ROUTE/logout    #############################################
@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    """Logout user"""
    logout_user()
    return redirect(url_for('login'))

#################################################
###############   DIRECTORY     ##################
#################################################

#############################################    @APP.ROUTE/register    #############################################
# Can add variable sections to URL by marking sections with <variable name>
# Function will receive <variable name> as keyword argument
#  --option to use converter to specify type of argument like <converter: variable_name>
@app.route("/directory/<bu_id>")
@login_required
def directory(bu_id=None):
    """Show business user directory, session create dynamic URL."""

    bu_id = session["_user_id"]
    business_user = crud.get_business_user_by_id(bu_id)

    clients = crud.show_all_client()
    rewards = crud.show_all_reward()

    return render_template('directory.html', clients=clients, rewards=rewards, business_user=business_user, bu_id=bu_id)

#################################################
###############   CLIENTS     ##################
#################################################

#############################################    @APP.ROUTE/new_client/<bu_id>    #############################################
@app.route("/new_client/<bu_id>")
@login_required
def new_client(bu_id=None):
    """Renders template register_client.html, displays new client registration form."""

    bu_id = session["_user_id"]
    business_user = crud.get_business_user_by_id(bu_id)

    return render_template('register_client.html', business_user=business_user, bu_id=bu_id)


#############################################    @APP.ROUTE/register    #############################################
@app.route("/new_client_signup", methods=['POST'])
def signup_new_client():
    """Route for form 'new-client', on register_client.html.
    
    Queries client database, checks if e-mail exists--returns flash message
    stating so. """

    bu_id = session["_user_id"]
    client_name = request.form.get("name")
    client_email = request.form.get("email")
    client = crud.get_client_by_email(client_email)
    business_user = crud.get_business_user_by_id(bu_id)

    if client:
        flash("There's already a client with that e-mail! Try again.")
    else:
        crud.create_client(client_name, client_email, business_user)
        flash("New client added.")
    return redirect(f"/new_client/{{ bu_id }}")

####################################  @APP.ROUTE("/client_profile/<bu_id>/<client_id>")  #####################################

@app.route("/client_profile/<bu_id>/<client_id>")
@login_required
def client_profile(bu_id=None, client_id=None):
    """Show client profile, renders 'client_profile.html'."""
    
    bu_id = session["_user_id"]

    client_reward = crud.get_client_point(client_id)
    client = crud.get_client_by_id(client_id)
    transactions = crud.show_all_transaction()
    business_user = crud.get_business_user_by_id(bu_id)
    rewards = crud.show_all_reward()

    return render_template('client_profile.html',client=client, client_reward=client_reward, rewards=rewards, transactions=transactions, business_user=business_user, bu_id=bu_id)


####################################  @APP.ROUTE("/edit_rewards/<bu_id>/<client_id>")  #####################################
@app.route("/edit_rewards/<bu_id>/<client_id>")
@login_required
def edit_client_reward(bu_id=None, client_id=None):
    """Shows client's reward points and available rewards,
    
    Renders 'edit_reward.html'. Allows user to add/sub points."""
  
    bu_id = session["_user_id"]

    business_user = crud.get_business_user_by_id(bu_id)
    client = crud.get_client_by_id(client_id)
    rewards = crud.show_all_reward()

    return render_template('edit_reward.html', bu_id=bu_id, business_user=business_user, client=client, rewards=rewards)

####################################  @APP.ROUTE("/adjusting_points")  ############################################
@app.route("/adjusting_points", methods=['POST'])
def adjusting_points():
    """Route for 'submit-form' POST request on 'edit_reward.html'."""
    reward_point = int(request.form.get('point'))
    client_id = request.form.get('client_id')
    bu_id = request.form.get('bu_id')
    # I don't know if I still need this, but I don't want to break my code 10/29/21
    business_user =crud.get_business_user_by_id(bu_id)
    client = crud.get_client_by_id(client_id)
    crud.adjust_client_points(client_id, reward_point)
    total_client_point = client.reward_point

    return {"new_points": total_client_point}

#################################################
###############  TRANSACTIONS  ##################
#################################################

####################################  @APP.ROUTE("/add_transaction/<bu_id>/<client_id>")  ############################################
@app.route('/add_transaction/<bu_id>/<client_id>')
@login_required
def transaction(bu_id=None ,client_id=None):
    """Renders 'add_transaction.html', shows form (for route '/new_transaction') to add transaction."""
    bu_id = session["_user_id"]
    business_user = crud.get_business_user_by_id(bu_id)
    clients = crud.get_client_by_id(client_id)

    return render_template('add_transaction.html', bu_id=bu_id, business_user=business_user,clients=clients)

####################################  @APP.ROUTE("/new_transaction")  ############################################
@app.route('/new_transaction', methods=['POST'])
def add_transaction():
    """Adds transaction to client profile, rendering form from 'add_transaction.html'."""

    transaction_date = request.form.get('transaction_date')
    appointment_type = request.form.get('appointment_type')
    total_cost = request.form.get('total_cost')
    client_id = request.form.get("client_id")

    client = crud.get_client_by_id(client_id)

    crud.create_transaction(transaction_date, appointment_type, total_cost, client)

    flash("Transaction added.")

    return redirect(url_for('transaction', bu_id=client.business_user.id, client_id=client.client_id))


#################################################
###############    REWARDS     ##################
#################################################

####################################  @APP.ROUTE("/rewards/<bu_id>")  ############################################
@app.route("/rewards/<bu_id>")
@login_required
def rewards_page(bu_id=None):
    """Renders 'rewards.html', shows list of rewards,
    
    with options to add a new reward or delete existing."""

    bu_id = session["_user_id"]
    rewards = crud.show_all_reward()
    business_user = crud.get_business_user_by_id(bu_id)

    return render_template('rewards.html', business_user=business_user, rewards=rewards, bu_id=bu_id)


####################################  @APP.ROUTE("/add_rewards/<bu_id>")  ############################################
@app.route("/add_rewards/<bu_id>")
@login_required
def add_reward(bu_id=None):
    """Renders 'add_reward.html' page, shows form for route '/adding_reward'."""
    
    bu_id = session["_user_id"]
    business_user = crud.get_business_user_by_id(bu_id)

    return render_template('add_reward.html', bu_id=bu_id, business_user=business_user)


####################################  @APP.ROUTE("/add_rewards/<bu_id>")  ############################################
@app.route("/adding_reward", methods=['POST'])
def adding_reward():
    """Processes POST form request from 'add_reward.html'."""

    reward_type = request.form.get('reward_type')
    reward_cost = request.form.get('reward_cost')
    bu_id = session["_user_id"]
    business_user = crud.get_business_user_by_id(bu_id)
    crud.create_reward(reward_type, reward_cost, business_user)
    flash("Reward added.")

    return redirect(f'/add_rewards/{bu_id}')

#######################################  @APP.ROUTE("/deleting_reward")  ############################################
@app.route("/deleting_reward", methods=['POST'])
def deleting_reward():
    """Deletes reward from '/add_rewards' route, 'add_reward.html'."""

    bu_id = session["_user_id"]
    delete_reward = request.form.get('reward_id')

    crud.delete_reward(delete_reward)
    return redirect(f'/rewards/{bu_id}')

## if this script is being called directly, than run(method) app(instance) 
## need to let module to scan for routes when creating a Flask application

if __name__ == "__main__":
    #DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)