import unittest

from server import app
from model import db, connect_to_db


class UserLogIn(unittest.TestCase):
    """pass."""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn(b"Welcome", result.data)

    def test_not_registered(self):
        result = self.client.get("/")
        self.assertIn(b"Please signup", result.data)
        self.assertNotIn(b"Welcome", result.data)

    def test_not_registered_yet(self):
        result = self.client.post("/register",
                                  data={"email": "nicki@nicki.test",
                                        "password": "pinkprint1"},
                                  follow_redirects=True)
        self.assertIn(b"Welcome", result.data)
        self.assertIn(b"")


# class PartyTestsDatabase(unittest.TestCase):
#     """Flask tests that use the database."""

#     def setUp(self):
#         """Stuff to do before every test."""

#         self.client = app.test_client()
#         app.config['TESTING'] = True

#         # Connect to test database (uncomment when testing database)
#         # connect_to_db(app, "postgresql:///testdb")

#         # Create tables and add sample data (uncomment when testing database)
#         # db.create_all()
#         # example_data()

#     def tearDown(self):
#         """Do at end of every test."""

#         # (uncomment when testing database)
#         # db.session.close()
#         # db.drop_all()

#     def test_games(self):
#         # FIXME: test that the games page displays the game from example_data()
#         print("FIXME")


if __name__ == "__main__":
    unittest.main()
