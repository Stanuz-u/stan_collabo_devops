import unittest
from checker import is_valid_project_name


class TestProjectNameChecker(unittest.TestCase):

    def test_valid_name(self):
        self.assertTrue(is_valid_project_name("my-app"))

    def test_empty_name(self):
        self.assertFalse(is_valid_project_name(""))

    def test_name_with_spaces(self):
        self.assertFalse(is_valid_project_name("my app"))

    def test_non_string_input(self):
        self.assertFalse(is_valid_project_name(None))


if __name__ == "__main__":
    unittest.main()
