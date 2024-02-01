class Solution(object):
    def threeSum(self, nums):
        retList = []
        nums.sort()

        for position, i in enumerate(nums):

            if position > 0 and i == nums[position - 1]:
                continue

            lp,rp = position + 1, len(nums) - 1

            while lp < rp:
                threeSum = i + nums[lp] + nums[rp]
                if threeSum > 0:
                    rp -= 1
                    
                elif threeSum < 0:
                    lp += 1
                    
                else:
                    retList.append([i,nums[lp],nums[rp]])
                    lp += 1
                    rp -= 1
                    while nums[lp] == nums[lp - 1] and lp < rp:
                        lp += 1
       
        return retList                