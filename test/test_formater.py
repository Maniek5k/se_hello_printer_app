import hello_world.formater as h
import unittest


class TestFormater(unittest.TestCase):
    def test_plain_uppercase(self):
        r = h.plain_text_upper_case("lower", "LOWER")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.isupper())
        self.assertTrue(msg.isupper())

    def test_plain_lowercase(self):
        r = h.plain_text_lower_case("UPPER", "upper")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertTrue(name.islower())
        self.assertTrue(msg.islower())

    def test_plain_text(self):
        imie = "MikeZ"
        msg = "Test message"
        self.assertEqual("MikeZ", imie)
        self.assertEqual("Test message", msg)