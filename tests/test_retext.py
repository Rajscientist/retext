import unittest
from retext.retext import (
    reverse_string,
    capitalize_first,
    count_vowels,
    remove_whitespace,
    is_palindrome,
    to_snake_case,
    to_camel_case
)


class TestStringManipulation(unittest.TestCase):
    
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
    
    def test_capitalize_first(self):
        self.assertEqual(capitalize_first("hello"), "Hello")
        self.assertEqual(capitalize_first("python"), "Python")
        self.assertEqual(capitalize_first(""), "")
    
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("Python"), 1)
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("rhythm"), 0)

    def test_remove_whitespace(self):
        self.assertEqual(remove_whitespace("  hello "), "hello")
        self.assertEqual(remove_whitespace("Python  "), "Python")
        self.assertEqual(remove_whitespace("  "), "")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertFalse(is_palindrome("hello"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_to_snake_case(self):
        self.assertEqual(to_snake_case("My Variable Name"), "my_variable_name")
        self.assertEqual(to_snake_case("PythonIsCool"), "python_is_cool")
        self.assertEqual(to_snake_case("hello world"), "hello_world")

    def test_to_camel_case(self):
        self.assertEqual(to_camel_case("my variable name"), "myVariableName")
        self.assertEqual(to_camel_case("python is cool"), "pythonIsCool")
        self.assertEqual(to_camel_case("hello world"), "helloWorld")

if __name__ == "__main__":
    unittest.main()
