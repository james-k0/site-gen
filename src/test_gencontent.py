import unittest
from gencontent import extract_title

class TestExtract(unittest.TestCase):
    def test_eq(self):
        actual = extract_title("# This is a title")
        self.assertEqual(actual, "This is a title")

    def test_not_eq(self):
        actual = extract_title("# foo")
        self.assertNotEqual(actual,"bar")