"""CRUD ('CREATE, READ, UPDATE, DESTROY') operations."""

# CRUD.py acts as a bridge from database tables to python

# importing database, classes, and connect_to_db from model.py
from model import db, BusinessUser, Client, Transaction, ClientReward, Reward, connect_to_db



#################################################
#################################################
###########    BUSINESS_USERS     ###############
#################################################
#################################################


####################################################################
################  def CREATE_BUSINESS_USER() ########################
####################################################################



def create_business_user(bu_email, bu_username, bu_password, bu_name, bu_business, bu_pic_path):
    """Create, add, & return new business user."""

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

    # print(bu_username)
    # print("over_here")
    business_user = BusinessUser.query.filter_by(bu_username=bu_username).first()
    # print(business_user, "hi")
    # print("reached here 2")
    # print(business_user)
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
#######################  def CREATE_CLIENT #########################
####################################################################

# don't need to add reward point, default to none
def create_client(client_name, client_email, business,
                  reward_point=0):
    """Creates a business user's new client."""
    
    client = Client(client_name=client_name,
                    client_email=client_email,
                    # associated w/model.py BusinessUser
                    id=business.id,
                    reward_point=reward_point,
    )
    # pass in business name

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

    # print("reached here")
    client = Client.query.filter_by(client_email=client_email).first()
    # print("reached here 2")
    # print(client_name)
    return client


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

    # db.session.add()
    db.session.commit()

    return client.reward_point

 
# business user in session


# Left Join
# SELECT client_name FROM clients AS c LEFT JOIN business_users AS bu USING(id);

# SELECT client_name FROM clients
# SELECT * --> .all()
# client = BusinessUser.query.get('business_users)

# bu_clients = db.session.query(Client, BusinessUser).outerjoin(BusinessUser).all()
# problem, need to assign business user id to clients

####################################################################
####################  def CREATE_TRANSACTION #########################
####################################################################

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


####################################################################
###################  def SHOW_ALL_TRANSACTION #######################
####################################################################

def show_all_transaction():
    """Show all client transactions."""
    
    return Transaction.query.all()


####################################################################
###################  def GET_TRANSACTION_BY_ID ######################
####################################################################

def get_transaction_by_id(transaction_id):
    """Display transaction by transaction_id."""
    
    transaction = Transaction.query.get(transaction_id)

    return transaction


####################################################################
###################  def CREATE_CLIENT_REWARD ######################
####################################################################

def create_client_reward(client_id, reward_id):
    """Create client reward."""

    client_reward = ClientReward(client_id=client_id, reward_id=reward_id)

    db.session.add(client_reward)
    db.session.commit()

    return client_reward


####################################################################
###################  def ADD_CLIENT_POINTS.   ######################
####################################################################

# def add_client_point(reward_point):
#     """Add point to client reward account."""
#     client = Client.query.all()
#     client_point = client.reward_point=reward_point

#     db.session.add(client_point)
#     db.session.commit()

#     return client_point

####################################################################
######################  def CREATE_REWARD ##########################
####################################################################

def create_reward(reward_type, reward_cost):
    """Create reward."""

    reward = Reward(reward_type=reward_type,
                    reward_cost=reward_cost,
    )

    db.session.add(reward)
    db.session.commit()

    return reward


####################################################################
#######################  def SHOW_ALL_REWARD #######################
####################################################################

def show_all_reward():
    """Show all reward."""

    return Reward.query.all()


####################################################################
#######################  def GET_REWARD_BY_ID #######################
####################################################################

def get_reward_by_id(reward_id):
    """Get reward by reward_id."""

    reward = Reward.query.get(reward_id)

    return reward


############################################################################


if __name__ == '__main__':
    from server import app
    connect_to_db(app)