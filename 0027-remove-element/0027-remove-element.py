class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for item in nums:
            if item != val:
                nums[k] = item
                k += 1
        return k
