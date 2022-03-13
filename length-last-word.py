# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        for c in reversed(s):
            if c.isalpha():
                length += 1
            else:
                if length > 0:
                    return length
        return length