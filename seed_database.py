import os
import json
# from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb loyalty")
os.system("createdb loyalty")

model.connect_to_db(server.app)
model.db.create_all()

with open('data/bu_dummydata.json') as f:
    bu_data = json.loads(f.read())

bus_in_db = []
for bu in bu_data:
    bu_email, bu_password_hash, bu_name, bu_business, bu_pic_path = (
        bu['bu_email'],
        bu['bu_password_hash'],
        bu['bu_name'],
        bu['bu_business'],
        bu['bu_pic_path']
    )    

    db_bu = crud.create_business_user(bu_email, bu_password_hash, bu_name, bu_business,
                                      bu_pic_path)
    bus_in_db.append(db_bu)

with open('data/client_dummydata.json') as f:
    client_data = json.loads(f.read())

clients_in_db = []
for client in client_data:
    client_name, client_email, reward_point, num_of_reward = (
        client['client_name'],
        client['client_email'],
        client['reward_point'],
        client['num_of_reward']
    )    

    db_client = crud.create_client(client_name, client_email, 
                                   reward_point, num_of_reward)

    clients_in_db.append(db_client)




with open('data/transaction_dummydata.json') as f:
    transaction_data = json.loads(f.read())

transaction_in_db = []
for transaction in transaction_data:
    appointment_type, transaction_date, total_cost = (
        transaction['appointment_type'],
        transaction['transaction_date'],
        transaction['total_cost']
    )    

    db_transaction = crud.create_transaction(appointment_type, transaction_date, 
                                             total_cost)

    clients_in_db.append(db_client)
    


with open('data/rewards_dummydata.json') as f:
    reward_data = json.loads(f.read())

reward_in_db = []
for reward in reward_data:
    reward_type, reward_cost = (
        reward['reward_type'],
        reward['reward_cost']
    )    

    db_reward = crud.create_reward(reward_type, reward_cost)

    reward_in_db.append(db_reward)    
