"""HausStar Server"""

## from the flask library, import ...
from flask import (Flask, session, render_template, request, flash, redirect)
from flask_debugtoolbar import DebugToolbarExtension
from model import BusinessUser, connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "sk"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


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


# shows directory for corresponding business user id
@app.route("/directory/<business_user_id>")
def directory(business_user_id):
    """Show business user's directory."""
    
    # business_user = in crud.py call function "get_business_user_by_id(business_user_id"
    business_user = crud.get_business_user_by_id(business_user_id)
    # client = in crud.py call function "get_client_by_id(client_id)"
    client = crud.get_client_by_id(client_id)

    # returns TEMPLATE, and variable from above w/field
    return render_template('directory.html',business_user=business_user, client=client)

@app.route("/")

## if this script is being called directly, than run(method) app(instance) 
## need to let module to scan for routes when creating a Flask application
if __name__ == "__main__":
    #DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)