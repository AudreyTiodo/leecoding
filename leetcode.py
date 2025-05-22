"""


"""

class LeetCode:
    def IsPalindrome(self, s: str) -> bool:
        """
        Given a string s, return true if it is a palindrome, or false otherwise.
        """
        # Remove all non-alphanumeric characters and convert to lowercase
        s = ''.join(c.lower() for c in s if c.isalnum())
        # Check if the string is equal to its reverse
        return s == s[::-1]
    