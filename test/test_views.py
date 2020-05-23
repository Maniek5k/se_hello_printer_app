import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_json(self):
        rv = self.app.get('/?output=json')
        self.assertEqual(b'{\n    "Imie": "MikeZ",\n    "msg": "Application"\n}', rv.data)

    def test_msg_with_xml(self):
        rv = self.app.get('/?output=xml')
        self.assertIn(b'<Greetings><Name>', rv.data)

    def test_msg_with_name(self):
        rv = self.app.get('/?name=apolonia')
        self.assertEqual(b'apolonia Hello World!', rv.data)
