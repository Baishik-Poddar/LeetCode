class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = []
        win_length=[]
        for  i  in s:
            res.append(i)
        win=[]
        l=r=0
        first = False
        for i in range(0,len(res)):
            if res[i] not in win:
                win.append(res[i])
                r+=1
            else:
                r+=1
                l= win.index(res[i])
                del win[0:l+1]
                win.append(res[i])
            win_length.append(len(win))
        return(max(win_length,default=0))