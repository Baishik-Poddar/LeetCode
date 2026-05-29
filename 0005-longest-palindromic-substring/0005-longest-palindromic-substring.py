class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, longest_palindrome_len = 0, 1
        for i in range(0, n):
            right = i
            while right < n and s[i] == s[right]:
                right += 1
                
            left = i - 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            
            # s[left + 1, right - 1] inclusive is palindromic
            palindrome_len = right - left - 1
            if palindrome_len > longest_palindrome_len:
                longest_palindrome_len = palindrome_len
                start = left + 1
            
        return s[start: start + longest_palindrome_len]