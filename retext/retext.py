import re


def add(a, b):
    """Return the sum of a and b."""
    return a + b

def remove_whitespace(s):
    """Removes leading and trailing whitespace."""
    return s.strip()

def is_palindrome(s):
    """Checks if the string is a palindrome."""
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

def to_snake_case(s):
    """Converts a string to snake_case."""
    s = re.sub(r'([a-z])([A-Z])', r'\1_\2', s)  # Insert underscore between lowercase and uppercase letters
    return s.replace(" ", "_").lower()

def to_camel_case(s):
    """Converts a string to camelCase."""
    words = s.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])
