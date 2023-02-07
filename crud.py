"""CRUD ('CREATE, READ, UPDATE, DESTROY') operations."""
# actions to perform on set of data
# CRUD.py acts as a bridge from database tables to python

from model import db, BusinessUser, Client, Transaction, ClientReward, Reward, connect_to_db
import bcrypt

#################################################
###########    BUSINESS_USERS     ###############
#################################################


####################################################################
################  def CREATE_BUSINESS_USER() #######################
####################################################################

def create_business_user(bu_email, bu_username, bu_password_original, bu_name, bu_business, bu_pic_path="/static/img/pusheen_default.jpg"):
    """Create, add, & return new business user."""
    
    bu_password_code = bcrypt.hashpw(bu_password_original.encode('utf-8'), bcrypt.gensalt())
    bu_password = bu_password_code.decode('utf-8')
    business_user = BusinessUser(bu_email=bu_email, 
                                bu_username=bu_username,
                                bu_password=bu_password, 
                                bu_name=bu_name, 
                                bu_business=bu_business,
                                bu_pic_path=bu_pic_path)

    
    db.session.add(business_user)
    db.session.commit()

    return business_user


####################################################################
################  def SHOW_ALL_BUSINESS_USER() ######################
####################################################################

def show_all_business_user():
    """Return all business users"""

    return BusinessUser.query.all()


####################################################################
################  def GET_BUSINESS_USER_BY_ID ######################
####################################################################

def get_business_user_by_id(id):
    """Gets business user by id"""

    business_user = BusinessUser.query.get(id)

    return business_user


####################################################################
################  def GET_BUSINESS_USER_BY_USERNAME ################
####################################################################

def get_business_user_by_username(bu_username):
    """Checks if business user email exists in database"""

    business_user = BusinessUser.query.filter_by(bu_username=bu_username).first()
    return business_user


####################################################################
################  def GET_BUSINESS_USER_BY_EMAIL ################
####################################################################

def get_business_user_by_email(bu_email):
    """Checks if business user email exists in database"""

    # print("reached here")
    business_user = BusinessUser.query.filter_by(bu_email=bu_email).first()
    print(business_user, "email")
    # print("reached here 2")
    # print(business_user)
    return business_user


####################################################################
################  def UPDATE_BUSINESS_USER() #######################
####################################################################

def update_business_user(id):
    """Update business user profile."""

    business_user = BusinessUser.query.get(id)

    new_bu_name = request.form['bu_name']
    business_user.bu_name = new_bu_name

    db.session.commit()

    return business_user


#################################################
#################################################
###############    CLIENTS     ##################
#################################################
#################################################

####################################################################
#######################  def CREATE_CLIENT #########################
####################################################################

def create_client(client_name, client_email, business,
                  reward_point=0):
    """Creates a business user's new client."""
    
    client = Client(client_name=client_name,
                    client_email=client_email,
                    # associated w/model.py BusinessUser
                    id=business.id,
                    reward_point=reward_point
    )

    db.session.add(client)
    db.session.commit()

    return client


####################################################################
#######################  def SHOW_ALL_CLIENT ########################
####################################################################

def show_all_client():
    """Return all clients"""

    return Client.query.all()


####################################################################
####################  def GET_CLIENT_BY_ID #########################
####################################################################

def get_client_by_id(client_id):
    """Gets client by client_id"""

    client = Client.query.get(client_id)

    return client


####################################################################
###################  def GET_CLIENT_BY_EMAIL #######################
####################################################################

def get_client_by_email(client_email):
    """Checks if business user email exists in database."""

    client = Client.query.filter_by(client_email=client_email).first()
    return client


####################################################################
###################  def ADJUST_CLIENT_POINTS ######################
####################################################################

def adjust_client_points(client_id, reward_point):
    """Adds reward point to client account."""
    # EDGECASE ==> GOING INTO NEGATIVE
    client = Client.query.get(client_id)
    print(client)


    client.reward_point += reward_point
    print(client.reward_point)

    # # # when calling funciton, call w/client_id and 2nd argument, pass
    # # # in number that can be positive or negative

    db.session.commit()

    return client.reward_point

# Left Join
# SELECT client_name FROM clients AS c LEFT JOIN business_users AS bu USING(id);

# SELECT client_name FROM clients
# SELECT * --> .all()
# client = BusinessUser.query.get('business_users)

# bu_clients = db.session.query(Client, BusinessUser).outerjoin(BusinessUser).all()
# problem, need to assign business user id to clients


#################################################
##############   TRANSACTIONS     ################
#################################################

####################  def CREATE_TRANSACTION #########################


def create_transaction(transaction_date, appointment_type, total_cost, client):
    """Create client transaction."""

    transaction = Transaction(transaction_date=transaction_date,
                              appointment_type=appointment_type,
                              total_cost=total_cost,
                              client_id=client.client_id
    )

    db.session.add(transaction)
    db.session.commit()

    return transaction

###################  def SHOW_ALL_TRANSACTION ######################

def show_all_transaction():
    """Show all client transactions."""
    
    return Transaction.query.all()

###################  def GET_TRANSACTION_BY_ID ######################

def get_transaction_by_id(transaction_id):
    """Display transaction by transaction_id."""
    
    transaction = Transaction.query.get(transaction_id)

    return transaction

#################################################
###########    REWARDS/POINTS     ###############
#################################################

###################  def CREATE_CLIENT_REWARD ######################

def create_client_reward(client_id, reward_id):
    """Create client reward."""

    client_reward = ClientReward(client_id=client_id, reward_id=reward_id)

    db.session.add(client_reward)
    db.session.commit()

    return client_reward


##################  def GET_CLIENT_POINT.   ######################
def get_client_point(client_id):
    """Add point to client reward account."""
    client_point = ClientReward.query.filter_by(client_id=client_id).first()

    return client_point
######################  def CREATE_REWARD ##########################

def create_reward(reward_type, reward_cost, business):
    """Create reward."""

    reward = Reward(reward_type=reward_type,
                    reward_cost=reward_cost,
                    id=business.id
    )

    db.session.add(reward)
    db.session.commit()

    return reward

######################  def DELETE_REWARD ##########################

def delete_reward(reward_id):
    """Delete reward."""

    reward = Reward.query.get(reward_id)

    db.session.delete(reward)
    db.session.commit()

#######################  def SHOW_ALL_REWARD #######################

def show_all_reward():
    """Show all reward."""

    return Reward.query.all()

#######################  def GET_REWARD_BY_ID #######################

def get_reward_by_id(reward_id):
    """Get reward by reward_id."""

    reward = Reward.query.get(reward_id)

    return reward


if __name__ == '__main__':
    from server import app
    connect_to_db(app)