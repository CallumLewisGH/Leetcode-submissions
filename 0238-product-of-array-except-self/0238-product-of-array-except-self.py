class Solution(object):
    def productExceptSelf(self, nums):
        prelist = []
        for num in range(len(nums)):
            prelist.append(1)
        
        prefix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            prelist[i] = prefix
            

        postlist = []
        for num in range(len(nums)):
            postlist.append(1)

        postfix = 1
        for i in range(len(nums) -1, -1, -1,):
            postfix *= nums[i]
            postlist[i] = postfix
        
        prelist.insert(0, 1)
        postlist.append(1)

        retList = []
        for i in range(len(nums)):
            retList.append(prelist[i] * postlist[i+1])
        
        return retList