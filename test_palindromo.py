import unittest

from Palindromo import palindrome

class TestPalindromo(unittest.TestCase):
    def test_palindromo_neuquen(self):
        result = palindrome("neuquen")
        self.assertEqual(result, True)
    def test_palindromo_oso(self):
        result = palindrome("oso")
        self.assertEqual(result, True)
    def test_palindromo_agua(self):
        result = palindrome("agua")
        self.assertEqual(result, False)
    def test_palindromo_casa(self):
        result = palindrome("casa")
        self.assertEqual(result, False)
    


if __name__ == "__main__":
    unittest.main()