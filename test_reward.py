import unittest

import os 

# from server, import flask
from server import app
import crud
import model

os.system('dropdb loyalty')
os.system('createdb loyalty')

class RewardTestCase(unittest.TestCase):

    def setUp(self):
        """Defining instructions to be executed before test method."""

        print("------------------------test-----------------------")

        model.connect_to_db(app)
        model.db.create_all()


    def test_reward_exists(self):
        """Checks to see reward has been added to table."""
        test_reward = crud.create_reward(reward_type="special reward",
                                         reward_cost="10 points")

        model.db.session.add(test_reward)
        model.db.session.commit()
        
        test_query = model.Reward.query.filter(model.Reward.client_name == test_reward.reward_type).first()

        self.assertEqual(test_reward test_query)

    def test_show_all_reward(self):
        """Tests if function returns all business users."""
        
        test_show_all_reward= model.Reward.query.all()
      
        crud_show_all_rewards = crud.show_all_rewards()
        
        self.assertEqual(test_show_all_rewards, crud_show_all_rewards)


    def test_get_reward_by_id(self):

        test_reward_id = crud.get_reward_by_id(reward_id=3)


        test_query_by = model.Reward.query.get(model.Reward.reward_id)
        self.assertEqual(test_reward_id, test_query_by)



    if __name__ == "__main__":
        unittest.main()