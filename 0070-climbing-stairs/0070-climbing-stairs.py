class Solution(object):
    def climbStairs(self, n):
        num1 = 0
        num2 = 1
        for i in range(n):
            total = num1 + num2
            num1 = num2
            num2 = total
            

        
        return total