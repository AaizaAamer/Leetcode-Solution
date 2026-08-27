class Solution(object):
    def lengthOfLongestSubstring(self, s):
        longest = 0
        for s1 in range(len(s)):
            current = ""
            for s2 in range(s1, len(s)):
                if s[s2] in current:
                    break
                current += s[s2]
                if len(current) > longest:
                    longest = len(current)
        return longest
            
