class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        lp = 0
        rp = len(x)-1

        while rp > lp:
            if x[lp] != x[rp]:
                return False
            lp += 1
            rp -= 1
        
        return True