"""CRUD ('CREATE, READ, UPDATE, DELETE') operations."""

# CRUD.py acts as a bridge from database tables to python

# importing database, classes, and connect_to_db from model.py
from model import db, BusinessUser, Client, Transaction, ClientReward, Reward, connect_to_db


def create_business_user(bu_email, bu_password_hash, bu_name, bu_business, bu_pic_path):
    """Create, add, & return new business user."""

    business_user = BusinessUser(bu_email=bu_email, 
                                bu_password_hash=bu_password_hash, 
                                bu_name=bu_name, 
                                bu_business=bu_business,
                                bu_pic_path=bu_pic_path
    )

    # 
    db.session.add(business_user)
    db.session.commit()

    return business_user

def show_all_business_user():
    """Return all business users"""

    return BusinessUser.query.all()

def get_business_user_by_id(business_user_id):
    """Gets business user by business_user_id"""

    business_user = BusinessUser.query.get(business_user_id)

    return business_user

def get_business_user_by_email(bu_email):
    """Checks if business user email exists in database"""

    print("reached here")
    business_user = BusinessUser.query.filter_by(bu_email=bu_email).first()
    print("reached here 2")
    print(business_user)
    return business_user

# don't need to add reward point, default to none
def create_client(client_name, client_email, business,
                  reward_point=None, num_of_reward=None):
    """Creates a business user's new client."""
    
    client = Client(client_name=client_name,
                    client_email=client_email,
                    # associated w/model.py BusinessUser
                    business_user_id=business.business_user_id,
                    reward_point=reward_point,
                    num_of_reward=num_of_reward
    )
    # pass in business name

    db.session.add(client)
    db.session.commit()

    return client

def show_all_client():
    """Return all clients"""

    return Client.query.all()

def get_client_by_id(client_id):
    """Gets client by client_id"""

    client = Client.query.get(client_id)

    return client

def get_client_by_email(client_email):
    """Checks if business user email exists in database"""

    # print("reached here")
    client = Client.query.filter_by(client_email=client_email).first()
    # print("reached here 2")
    # print(client_name)
    return client


# Left Join
# SELECT client_name FROM clients AS c LEFT JOIN business_users AS bu USING(business_user_id);

# SELECT client_name FROM clients
# SELECT * --> .all()
# client = BusinessUser.query.get('business_users)
# def get_clients_by_business_user_id(business_user_id):
#     """Gets client through business_users table."""
#     clients=set()
    
#     for business_users in(
#         BusinessUser.query.options(db.joinedload("clients")).filter_by(business_user_id=business_user_id)
#         .all()

#     ):
#         clients.add(business_users.client_name)

#     return list(clients)

# bu_clients = db.session.query(Client, BusinessUser).outerjoin(BusinessUser).all()
# problem, need to assign business user id to clients


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

def show_all_transaction():
    """Show all client transactions."""
    
    return Transaction.query.all()

def get_transaction_by_id(transaction_id):
    """Display transaction by transaction_id."""
    
    transaction = Transaction.query.get(transaction_id)

    return transaction

def create_reward(reward_type, reward_cost):
    """Create reward."""

    reward = Reward(reward_type=reward_type,
                    reward_cost=reward_cost)

    db.session.add(reward)
    db.session.commit()

    return reward

def show_all_reward():
    """Show all reward."""

    return Reward.query.all()

def get_reward_by_id(reward_id):
    """Get reward by reward_id."""

    reward = Reward.query.get(reward_id)

    return reward


if __name__ == '__main__':
    from server import app
    connect_to_db(app)