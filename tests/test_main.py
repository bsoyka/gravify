import sys
import unittest

sys.path.insert(0, '../')

from gravify import Gravatar


class TestMain(unittest.TestCase):

    def test_plain_email(self):
        self.assertEqual(Gravatar("bensoyka@icloud.com").url,
                         "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052")

    def test_hash(self):
        self.assertEqual(Gravatar("bensoyka@icloud.com").hash, "7246821a7bf0b1b37794b39cb08ee052")

    def test_hash_whitespace(self):
        self.assertEqual(Gravatar("   \tbensoyka@icloud.com\n").hash, "7246821a7bf0b1b37794b39cb08ee052")

    def test_hash_to_lowercase(self):
        self.assertEqual(Gravatar("bEnSoYkA@iClOuD.cOm").hash, "7246821a7bf0b1b37794b39cb08ee052")

    def test_default_identicon(self):
        self.assertEqual(Gravatar("bensoyka@icloud.com", default_image="identicon").url,
                         "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?d=identicon")

    def test_without_param(self):
        self.assertEqual(
            Gravatar("bensoyka@icloud.com").url,
            "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052")

    def test_size_param(self):
        self.assertEqual(
            Gravatar("bensoyka@icloud.com", size=200).url,
            "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?s=200")
        self.assertEqual(
            Gravatar("bensoyka@icloud.com", size=300).url,
            "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?s=300")

    def test_force_default_param(self):
        self.assertEqual(
            Gravatar("bensoyka@icloud.com", force_default=True).url,
            "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?f=y")

    def test_file_handler(self):
        self.assertIsInstance(Gravatar("bensoyka@icloud.com").file.read(4), bytes)

    def test_rating(self):
        self.assertEqual(
            Gravatar("bensoyka@icloud.com", rating="pg").url,
            "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?r=pg")


if __name__ == "__main__":
    unittest.main()
