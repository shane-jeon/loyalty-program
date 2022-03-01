"""Models for loyalty program project"""

# importing SQLAlchemy constructor function
from flask_sqlalchemy import SQLAlchemy
# flask WTForms to populate database
from flask_wtf import FlaskForm
# all of below relevant to incorporating security
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from flask_login import UserMixin
# importing werkzeug
# from werkzeug.security import generate_password_hash, check_password_hash



# calling to create SQLAlchemy instance at variable db
db = SQLAlchemy()




#################################################
#################################################
###############  business_users  ################
###############    table       ##################
#################################################
#################################################

class BusinessUser(db.Model, UserMixin):
    """Business user information."""

    # defining table name
    __tablename__ = 'business_users'

    # specifying types of columns, in this case integer, it is primary key,...
    # ...should autoincrement
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # email is String type w/max size of 120 characters
    bu_email = db.Column(db.String(120), nullable=False, unique=True)
    bu_username = db.Column(db.String(30), nullable=False, unique=True)
    # changed "bu_password" to "bu_password", is 128 character hash
    bu_password = db.Column(db.String(500), nullable=True)
    bu_name = db.Column(db.String, nullable=False)
    bu_business = db.Column(db.String, nullable=False, unique=True)
    bu_pic_path = db.Column(db.String, nullable=True)



    def __repr__(self):
        """User repr method."""
        return f"""<Business_user id={self.id} bu_email={self.bu_email}
        bu_username={self.bu_username} bu_business={self.bu_business}>"""

    # variable = db.relationship('Class', back_populates='class_relationship_varaible')
    # backpopulating to connect tables
    client = db.relationship('Client', back_populates='business_user')
    client_reward = db.relationship('ClientReward', back_populates='business_user')
    reward = db.relationship('Reward', back_populates='business_user')
    # photo = db.relationship('Photo', back_populates='business_user')


# #################################################
# #################################################
# ###############  registration     ################
# ###############   login       ##################
# #################################################
# #################################################

# # created registration form that inherits from FlaskForm
# class RegisterForm(FlaskForm):
#     """Register user form."""
#     # StringField allows user to see characters
#     # InputRequired() --> must be filled out
#     # min and max for characters username, placeholder is placeholder for Username, use with render_kw
#     bu_username = StringField(validators=[InputRequired(), Length(
#         min=4, max=20)], render_kw={"placeholder": "Username"})

#     # instead use PasswordField, will show black dots
#     # minimum difference is because password will hash (not sure how long, so in db is set to 80)
#     bu_password = PasswordField(validators=[InputRequired(), Length(
#         min=4, max=20)], render_kw={"placeholder": "Password"})

#     # button to register
#     submit = SubmitField("Register")

#     # validates if there is username that has already been typed in
#     # queries database, checks if similar username
#     def validate_bu_username(self, bu_username):
#         existing_business_user_bu_username = BusinessUser.query.filter_by(bu_username=bu_username.data).first()

#         if existing_business_user_bu_username:
#             raise ValidationError(
#                 "That username already exists. PLease choose a different one.")

# class LoginForm(FlaskForm):

#     # StringField allows user to see characters
#     # InputRequired() --> must be filled out
#     # min and max for characters username, placeholder is placeholder for Username, use with render_kw
#     bu_username = StringField(validators=[InputRequired(), Length(
#         min=4, max=20)], render_kw={"placeholder": "Username"})

#     # instead use PasswordField, will show black dots
#     # minimum difference is because password will hash (not sure how long, so in db is set to 80)
#     bu_password = PasswordField(validators=[InputRequired(), Length(
#         min=4, max=20)], render_kw={"placeholder": "Password"})

#     # button to register
#     submit = SubmitField("Login")


#################################################
#################################################
###############  clients         ################
###############    table       ##################
#################################################
#################################################


# 10/17/2021, 10:01PMremoved "num_of_rewards"
# removed from model.py; crud.py; seed_database.py
class Client(db.Model):
    """a client"""
    
    __tablename__ = 'clients'

    client_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    client_name = db.Column(db.Text, nullable=False)
    client_email = db.Column(db.String(254), nullable=False, unique=True)
    reward_point = db.Column(db.Integer, nullable=True)
    # client_pic_path = db.Column(db.String(254), nullable=True)
    id = db.Column(db.Integer, db.ForeignKey('business_users.id'))

    def __repr__(self):
        return f'<Client client_id={self.client_id}, client_name={self.client_name}, client_email={self.client_email}, reward_point={self.reward_point}>'

    # relationship to business_users table
    business_user = db.relationship('BusinessUser', back_populates='client')
    # relationship to client_rewards table
    client_reward = db.relationship('ClientReward', back_populates='client')
    # relationship to transactions table
    transaction = db.relationship('Transaction', back_populates='client')
    # # relationship to photo table
    # photo = db.relationship('Photos', back_populates='client')

#################################################
#################################################
###############  photos   ######################
#################################################
#################################################
#################################################

# class Photo(db.Model):
#     """Business User and Client profile pictures."""

#     __tablename__ = 'photos'

#     photo_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     bu_pic_path = db.Column(db.String(254))
#     client_pic_path = db.Column(db.String(254))
#     id = db.Column(db.Integer, db.ForeignKey('business_users.id'))
#     client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))

#     def __repr__(self):
#         return f'<Business User photo_id={self.photo_id}, bu_pic_path={self.bu_pic_path}, client_pic_path={self.client_pic_path}>'

#     # relationship to business_users table
#     business_user = db.relationship('BusinessUser', back_populates='photo')
#     client = db.relationship('Client', back_populates='photo')


#################################################
#################################################
###############  transactions.   ################
###############    table       ##################
#################################################
#################################################

class Transaction(db.Model):
    """a transaction"""

    __tablename__ = 'transactions'
    
    transaction_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    appointment_type = db.Column(db.Text, nullable=False)
    transaction_date =db.Column(db.Date)
    total_cost = db.Column(db.String)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))


    def __repr__(self):
        return f'<Transaction transaction_id={self.transaction_id} appointment_type={self.appointment_type}, transaction_date={self.transaction_date}, client_id={self.client_id}>'

    client = db.relationship('Client', back_populates='transaction')
    




#################################################
#################################################
###############  client_rewards  ################
###############    table       ##################
#################################################
#################################################

class ClientReward(db.Model):
    """client reward association table"""

    __tablename__ = 'client_rewards'
    client_reward_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('clients.client_id'))
    reward_id = db.Column(db.Integer, db.ForeignKey('rewards.reward_id'))
    id = db.Column(db.Integer, db.ForeignKey('business_users.id'))

    def __repr__(self):
        return f'<ClientReward client_reward_id={self.client_reward_id}, client_id={self.client_id}, reward_id={self.reward_id}>'

    # relationship to rewards table
    reward = db.relationship('Reward', back_populates='client_reward')
    # relationship to clients table
    client = db.relationship('Client', back_populates='client_reward')
    business_user = db.relationship('BusinessUser', back_populates='client_reward')



#################################################
#################################################
###############    rewards       ################
###############    table       ##################
#################################################
#################################################

class Reward(db.Model):

    __tablename__ = 'rewards'

    reward_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    reward_type = db.Column(db.Text, nullable=False)
    reward_cost = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, db.ForeignKey('business_users.id'))


    def __repr__(self):
        return f'<Reward reward_id={self.reward_id} reward_type={self.reward_type}>'

    client_reward = db.relationship('ClientReward', back_populates='reward')
    business_user = db.relationship('BusinessUser', back_populates='reward')



#################################################
#################################################
###############  connect_to_db   ################
#################################################
#################################################

def connect_to_db(flask_app, db_uri='postgresql:///loyalty', echo=True):
    """Connect to the database."""
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



#################################################
#################################################
############__name__ == "__main__"   ############
#################################################
#################################################

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
