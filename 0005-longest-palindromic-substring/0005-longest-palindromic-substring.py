class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=[]
        if(len(s)<=1):
            return s
        longest = s[0]
        for i in range(len(s)):
            p1 = self.expand(s, i, i)
            if len(p1) > len(longest):
                longest = p1
            p2 = self.expand(s, i, i + 1)
            if len(p2) > len(longest):
                longest = p2
        return longest

    def expand(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
