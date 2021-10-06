"""CRUD operations."""

from model import db, BusinessUser, Client, Transaction, ClientReward, Reward, connect_to_db

def create_business_user(bu_email, bu_password, bu_name, bu_business, bu_pic_path):
    """Create and return new business user."""

    business_user = BusinessUser(bu_email=bu_email, 
                                bu_password=bu_password, 
                                bu_name=bu_name, 
                                bu_business=bu_business,
                                bu_pic_path=bu_pic_path
    )


    db.session.add(business_user)
    db.session.commit()

    return business_user

def show_all_business_user():
    """Return all business users"""

    return BusinessUser.query.all()

def get_business_user_by_id(business_user_id):
    """Display e-mail by user_id"""

    business_user = BusinessUser.query.get(business_user_id)

    return business_user

def create_client(client_name, client_email, reward_point, num_of_reward):
    """Create client."""
    
    client = Client(client_name=client_name,
                    client_email=client_email,
                    reward_point=reward_point,
                    num_of_reward=num_of_reward
    )

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

def create_transaction(appointment_type, transaction_date, total_cost):
    """Create client transaction."""

    transaction = Transaction(appointment_type=appointment_type,
                              transaction_date=transaction_date,
                              total_cost=total_cost)

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