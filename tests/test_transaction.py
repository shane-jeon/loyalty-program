import unittest

import os 

# from server, import flask
from server import app
import crud
import model

os.system('dropdb loyalty')
os.system('createdb loyalty')

class TransactionTestCase(unittest.TestCase):

    def setUp(self):
        """Defining instructions to be executed before test method."""

        print("------------------------test-----------------------")

        model.connect_to_db(app)
        model.db.create_all()


    def test_transaction_exists(self):
        """Checks to see transaction has been added to table."""
        # assign crud functions w/test values to overall test variable
        test_transaction = crud.create_transaction(appointment_type="test_type",
                                                transaction_date=datetime.now(),
                                                total_cost="$120.00")

        model.db.session.add(test_transaction)
        model.db.session.commit()
        
        test_query = model.Transaction.query.filter(model.Transaction.client_name == test_transaction.total_cost).first()

        self.assertEqual(test_transaction, test_query)

    def test_show_all_transactions(self):
        """Tests if function returns all business users."""
        
        test_show_all_transactions= model.Transaction.query.all()
      
        crud_show_all_transactions = crud.show_all_transactions()
        
        self.assertEqual(test_show_all_transactions, crud_show_all_transactions)


    def test_get_transaction_by_id(self):

        test_transaction_id = crud.get_transaction_by_id(transaction_id=3)


        test_query_by = model.Transaction.query.get(model.Transaction.transaction_id)
        self.assertEqual(test_transaction_id, test_query_by)


    if __name__ == "__main__":
        unittest.main()