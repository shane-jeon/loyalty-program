# import unittest to inherit TestCase
import unittest
# module providing functions for interacting w/operating system (from Python's standard modules)
import os 

# from server, import flask
from server import app
# import crud.py
import crud
# import model.py
import model

# executes command (string) in subshell --> so runs following commands in dummy shell? 
# parameter is string type stating what command to execute
os.system('dropdb loyalty')
os.system('createdb loyalty')

class BusinessUserTestcase(unittest.TestCase):

    def setUp(self):
        """Defining instructions to be executed before test method."""

        print("------------------------test-----------------------")
        # model.py is now an instantiated attribute of test class
        # calls function w/flask as parameter
        model.connect_to_db(app)
        # creates tables from database
        model.db.create_all()

    # def tearDown(self):
    #     """Defining instructions to be executed after test method."""

    # method
    def test_business_user_exists(self):
        """Checks to see business_user has been added to table."""
        # assign crud functions w/test values to overall test variable
        test_business_user = crud.create_business_user(bu_email="test@test.test", 
                                              bu_password="pw123", bu_name="Testie Test", 
                                              bu_business="Testie's Business", bu_pic_path="https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.thebalancesmb.com%2Fimprove-your-small-business-2951413&psig=AOvVaw1QpHUzhVJssfOXotWwZ0a_&ust=1633719579591000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCMiQuuz9uPMCFQAAAAAdAAAAABAD") 

        # performing typical commands used to create business user
        model.db.session.add(test_business_user)
        model.db.session.commit()
        test_query = model.BusinessUser.query.filter(model.BusinessUser.bu_name == test_business_user.bu_name).first()
        self.assertEqual(test_business_user, test_query)

    def test_show_all_business_user(self):
        """Tests if function returns all business users."""
        
        # create test variable, value is model.Class.query.____
        test_show_all_business_user = model.BusinessUser.query.all()
        # crud variable is calling crud function 
        crud_show_all_business_user = crud.show_all_business_user()
        
        # checks if the test query is equal to the function output
        self.assertEqual(test_show_all_business_user, crud_show_all_business_user)

if __name__ == "__main__":
    unittest.main()