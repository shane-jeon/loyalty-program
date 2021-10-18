"""Models for loyalty program project"""

# import SQL alchemy to link SQL and PYTHON
from flask_sqlalchemy import SQLAlchemy
# importing werkzeug
from werkzeug.security import generate_password_hash, check_password_hash

# db object, representing database
db = SQLAlchemy()




#################################################
#################################################
###############  business_users  ################
###############    table       ##################
#################################################
#################################################

class BusinessUser(db.Model):
    """Business user information."""

    __tablename__ = 'business_users'

    # table fields
    business_user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # email is String type w/max size of 120 characters
    bu_email = db.Column(db.String(120), nullable=False, unique=True)
    # changed "bu_password" to "bu_password_hash", is 128 character hash
    bu_password_hash = db.Column(db.String(128), nullable=True)
    bu_name = db.Column(db.String, nullable=False)
    bu_business = db.Column(db.String, nullable=False, unique=True)
    bu_pic_path = db.Column(db.String, nullable=True)

    # creating pw hashing functions
    # write test for following later (return to)
    def set_password(self, password):
        """Sets PW hash using werkzeug."""
        self.bu_password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Compares input pw w/corresponding PW hash."""
        return check_password_hash(self.bu_password_hash, password)



    def __repr__(self):
        return f"""<Business_user business_user_id={self.business_user_id} bu_email={self.bu_email} 
        bu_name={self.bu_name} bu_business={self.bu_business}>"""

    # variable = db.relationship('Class', back_populates='class_relationship_varaible')
    client = db.relationship('Client', back_populates='business_user')




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
    business_user_id = db.Column(db.Integer, db.ForeignKey('business_users.business_user_id'))

    def __repr__(self):
        return f'<Client client_id={self.client_id}, client_name={self.client_name}, client_email={self.client_email}>'

    # relationship to business_users table
    business_user = db.relationship('BusinessUser', back_populates='client')
    # relationship to client_rewards table
    client_reward = db.relationship('ClientReward', back_populates='client')
    # relationship to transactions table
    transaction = db.relationship('Transaction', back_populates='client')




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
    transaction_date =db.Column(db.DateTime)
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

    def __repr__(self):
        return f'<ClientReward client_reward_id={self.client_reward_id}>'

    # relationship to rewards table
    reward = db.relationship('Reward', back_populates='client_reward')
    # relationship to clients table
    client = db.relationship('Client', back_populates='client_reward')



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


    def __repr__(self):
        return f'<Reward reward_id={self.reward_id} reward_type={self.reward_type}>'

    client_reward = db.relationship('ClientReward', back_populates='reward')



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
