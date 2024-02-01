class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        
        for p, i in enumerate(nums):

            if i in hashMap:
                return [hashMap[i], p]

            else:
                hashMap[target - i] = p

        