class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        cmm_prefix=""
        smallest= min(strs,key=len)
        for i in range(0,len(smallest)):
            if all(word[i]== smallest[i] for word in strs):
                cmm_prefix+= smallest[i]
                # print(cmm_prefix)
            else:
                break
        return cmm_prefix
