class Solution(object):
    def longestPalindrome(self, s):
        longest=""
        for start in range(1,len(s)):
            for end in range(start,len(s)):
                substring=s[start:end +1]
                if substring==substring[::-1]:
                    if len(substring)>len(longest):
                        longest=substring
        return longest
