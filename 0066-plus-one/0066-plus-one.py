class Solution(object):
    def plusOne(self, digits):
        index = len(digits) - 1
        digits[index] += 1

        while digits[index] == 10:
            if index != 0:
                digits[index-1] += 1
                digits[index] = 0
                index -= 1
            else:
                digits[index] = 1
                digits.append(0)
        
        return digits


            