class Solution(object):
    def twoSum(self, numbers, target):
        currentSum = ''
        lp = 0
        rp = len(numbers) - 1
        while currentSum != target:
            currentSum = numbers[lp] + numbers[rp]
            if currentSum > target:
                rp -= 1
            
            elif currentSum < target:
                lp += 1
        
        return([lp + 1, rp + 1])
