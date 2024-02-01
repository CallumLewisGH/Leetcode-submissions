class Solution(object):
    def isPalindrome(self, s):
        position = 0
        reVal = 0
        sStripped = []
        for i in s:
            if i.isalpha() == True or i.isnumeric() == True:
                sStripped.append(i.lower())

        for position in range(len(sStripped)/2):
            if sStripped[position] == sStripped[(len(sStripped)-1)-position]:
                reVal += 1
        
        if reVal == len(sStripped)/2:
            return True
        
        else:
            return False
        