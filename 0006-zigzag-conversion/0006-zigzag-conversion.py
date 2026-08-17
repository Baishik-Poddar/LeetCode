import sys
class Solution(object):
    def convert(self, s, numRows):
        s= s.strip()
        if len(s) == 1 or numRows ==1:
            return s 
        else:
            rows = [""]*numRows
            idx =0
            rnum=0
            while idx< len(s):
                ch = s[idx]
                rows[rnum] += ch
                if rnum ==0:
                    step =1
                elif rnum == numRows -1 :
                    step=-1
                rnum+=step
                idx+=1
            return "".join(rows)
    




        