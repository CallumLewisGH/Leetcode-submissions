class Solution(object):
    def longestConsecutive(self, nums):
        numSet = set(nums)
        returnLength = 0
        runLength = 0

        for i in (numSet):
            if i - 1 not in numSet:
                while i in numSet:
                    runLength += 1
                    i += 1
                if runLength > returnLength:
                    returnLength = runLength
                 
                runLength = 0
       
        return returnLength
            