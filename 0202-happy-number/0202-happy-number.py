class Solution(object):
    def isHappy(self, n):
        happyList = []
        while n != 1:
            total = 0
                
            for i in str(n):
                total += int(i) ** 2

            n = total

            if n in happyList:
                return False

            else:
                happyList.append(n)
        
        return True