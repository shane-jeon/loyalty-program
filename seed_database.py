import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb loyalty")
os.system("createdb loyalty")

model.connect_to_db(server.app)
model.db.create_all()


#################################################
#################################################
###############    business      ################
#################################################
#################################################

# grabs data from dummy file
with open('data/bu_dummydata.json') as f:
    bu_data = json.loads(f.read())

bus_in_db = []

for bu in bu_data:
    # assigning respective variables to access keys?
    bu_email, bu_password_hash, bu_name, bu_business, bu_pic_path = (
        bu['bu_email'],
        bu['bu_password_hash'],
        bu['bu_name'],
        bu['bu_business'],
        bu['bu_pic_path']
    )    

    # db_bu is creating business user 
    db_bu = crud.create_business_user(bu_email, bu_password_hash, bu_name, bu_business,
                                      bu_pic_path)

    # appending created business_user to bus_in_db
    bus_in_db.append(db_bu)


#################################################
#################################################
###############     clients      ################
#################################################
#################################################

with open('data/client_dummydata.json') as f:
    client_data = json.loads(f.read())

clients_in_db = []
for client in client_data:
    client_name, client_email, business, reward_point, num_of_reward = (
        client['client_name'],
        client['client_email'],
        choice(bus_in_db),
        client['reward_point'],
        client['num_of_reward']
    )    

    db_client = crud.create_client(client_name, client_email, business, 
                                   reward_point, num_of_reward)

    clients_in_db.append(db_client)


#################################################
#################################################
###############   transactions   ################
#################################################
#################################################

with open('data/transaction_dummydata.json') as f:
    transaction_data = json.loads(f.read())

transaction_in_db = []
for transaction in transaction_data:
    transaction_date, appointment_type, total_cost, client = (
        transaction['appointment_type'],
        transaction['transaction_date'],
        transaction['total_cost'],
        choice(clients_in_db)
    )    

    db_transaction = crud.create_transaction(appointment_type, transaction_date, 
                                             total_cost, client)

    transaction_in_db.append(db_transaction)


#################################################
#################################################
###############     rewards       ###############
#################################################
#################################################

with open('data/rewards_dummydata.json') as f:
    reward_data = json.loads(f.read())

reward_in_db = []
for reward in reward_data:
    reward_type, reward_cost= (
        reward['reward_type'],
        reward['reward_cost'],
        # reward['client_reward']
    )

    db_reward = crud.create_reward(reward_type, reward_cost)

    reward_in_db.append(db_reward)

# for association table ("many-to-many")
for client in clients_in_db:
    crud.create_client_reward(client.client_id, randint(1, 20))