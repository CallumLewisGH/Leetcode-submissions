class Solution(object):
    def longestCommonPrefix(self, strs):
        for pos1,i in enumerate(strs):
            realPrefix = ""
            if pos1 == 0:
                prefix = i
                continue
                
            for pos2,char in enumerate(i):

                if pos2 != len(prefix) and char == prefix[pos2]:
                    realPrefix += char
                    
                else:
                    break
                
            prefix = realPrefix
            
        return prefix
