"""
Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = 0
        lastspace = True
        for c in s:
            if c == ' ':
                lastspace = True
            else:
                if lastspace:
                    n = 0
                    lastspace = False
                n += 1
            print('c, n ', c, n)

        return n

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord('   fly me   to   the moon  '))
    print(s.lengthOfLastWord('luffy is still joyboy'))
    print(s.lengthOfLastWord('Hello World'))
        