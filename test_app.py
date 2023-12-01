from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed based
        on if the table displaying the board and form exists"""

        with app.test_client() as client:
            response = client.get('/')
            html = response.get_data(as_text=True)

            self.assertEqual(response.status_code, 200)
            #could also look by comment in html
            self.assertIn('<table class="board">', html)
            # test that you're getting a template

    def test_api_new_game(self):
        """Test starting a new game."""

        with app.test_client() as client:
            response = client.post('/api/new-game')
            #response.json
            # json_data = response.get_data(as_text=True)
            #why does response.json not work but response.get_json does
            json_obj = response.get_json()
            # breakpoint()

            self.assertEqual(response.status_code, 200)
            self.assertIn(json_obj['gameId'], games)
            self.assertIn('gameId', json_obj)
            self.assertIsInstance(json_obj["gameId"], str)
            self.assertIsInstance(json_obj["board"], list)
            self.assertIsInstance(json_obj["board"][0], list)
            # write a test for this route
