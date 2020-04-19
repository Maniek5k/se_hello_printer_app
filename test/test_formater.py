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
        r = h.plain_text("Test", "MikeZ")
        name = r.split(" ")[0]
        msg = r.split(" ")[1]
        self.assertEqual("MikeZ", name)
        self.assertEqual("Test", msg)

    def test_json(self):
        r = h.format_to_json("Test", "MikeZ")
        self.assertIn("MikeZ", r)
        self.assertIn("Test", r)

    def test_xml(self):
        r = h.format_to_xml("Test", "MikeZ")
        name = "MikeZ".encode()
        message = "Test".encode()
        self.assertEqual(r.mimetype, "application/xml")
        self.assertIn(name, r.data)
        self.assertIn(message, r.data)
