import sys
import unittest

sys.path.insert(0, '../')

import gravify


class TestMain(unittest.TestCase):

    def test_plain_email(self):
        self.assertEqual(gravify.Gravatar("bensoyka@icloud.com").url,
                         "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052")

    def test_hash(self):
        self.assertEqual(gravify.Gravatar("bensoyka@icloud.com").hash, "7246821a7bf0b1b37794b39cb08ee052")

    def test_hash_whitespace(self):
        self.assertEqual(gravify.Gravatar("   \tbensoyka@icloud.com\n").hash, "7246821a7bf0b1b37794b39cb08ee052")

    def test_hash_inner_spaces(self):
        self.assertEqual(gravify.Gravatar('"ben soyka"@icloud.com').hash, "5d09bd0d26efc0871a3977aa55fb3f9c")

    def test_hash_to_lowercase(self):
        self.assertEqual(gravify.Gravatar("bEnSoYkA@iClOuD.cOm").hash, "7246821a7bf0b1b37794b39cb08ee052")

    def test_default_identicon(self):
        self.assertEqual(gravify.Gravatar("bensoyka@icloud.com", default_image="identicon").url,
                         "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?d=identicon")

    def test_without_param(self):
        self.assertEqual(
            gravify.Gravatar("bensoyka@icloud.com").url,
            "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052")

    def test_with_size_param(self):
        self.assertEqual(
            gravify.Gravatar("bensoyka@icloud.com", size=200).url,
            "https://www.gravatar.com/avatar/7246821a7bf0b1b37794b39cb08ee052?s=200")
    
    def test_file_handler(self):
        self.assertIsInstance(gravify.Gravatar("bensoyka@icloud.com").file.read(4), bytes)


if __name__ == "__main__":
    unittest.main()
