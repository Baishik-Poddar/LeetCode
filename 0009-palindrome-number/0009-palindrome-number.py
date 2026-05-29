class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        l=0
        r=len(s)-1
        flag= True
        while l<r:
            if s[l]!=s[r]:
                flag=False
            l+=1
            r-=1
        return flag