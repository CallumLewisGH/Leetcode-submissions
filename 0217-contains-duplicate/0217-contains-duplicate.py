class Solution(object):
    def containsDuplicate(self, nums):
        List = {}
        for i in nums:
            if i in List:
                return True
            else:
                List[i] = ''
        return False
