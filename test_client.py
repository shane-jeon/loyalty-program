
import unittest

import os 

# from server, import flask
from server import app
import crud
import model

os.system('dropdb loyalty')
os.system('createdb loyalty')

class ClientsTestCase(unittest.TestCase):

    def setUp(self):
        """Defining instructions to be executed before test method."""

        print("------------------------test-----------------------")

        model.connect_to_db(app)
        model.db.create_all()


    def test_client_exists(self):
        """Checks to see business_user has been added to table."""
        # assign crud functions w/test values to overall test variable
        test_client = crud.create_business_user(client_name="Dave",
                                                client_email="dave@test.test",
                                                reward_point=8, num_of_reward=0)

        model.db.session.add(test_business_user)
        model.db.session.commit()
        
        test_query = model.Client.query.filter(model.Client.client_name == test_client.client_name).first()

        self.assertEqual(test_client, test_query)

    def test_show_all_clients(self):
        """Tests if function returns all business users."""
        
        test_show_all_clients= model.Client.query.all()
      
        crud_show_all_clients = crud.show_all_clients()
        
        self.assertEqual(test_show_all_clients, crud_show_all_clients)


    def test_get_client_by_id(self):

        test_client_id = crud.get_client_by_id(client_id=3)


        test_query_by = model.Client.query.get(model.Client.client_id)
        self.assertEqual(test_client_id, test_query_by)



    if __name__ == "__main__":
        unittest.main()