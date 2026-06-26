class Solution:
    def isPalindrome(self, s: str) -> bool:
        clear = ''.join(char.lower() for char in s if char.isalnum())

        return clear == clear[::-1]
