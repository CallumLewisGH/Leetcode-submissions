class Solution(object):
    def removeDuplicates(self, nums):
        #Looked up but i understand it
        k = 1
        for index in range(1, len(nums)):
            if nums[index] != nums[index - 1]:
                nums[k] = nums[index]
                k += 1
        return k
     