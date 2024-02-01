class Solution(object):
    def romanToInt(self, s):
        translator = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0

        for pos,i in enumerate(s):
            if pos == len(s)-1:
                i = translator[i]
                total += i
                continue

            if i == "I" and (s[pos+1] == "V" or s[pos+1] == "X"):
                i = translator[i]
                total -= i
                
            elif i == "X" and (s[pos+1] == "L" or s[pos+1] == "C"):
                i = translator[i]
                total -= i
                
            elif i == "C" and (s[pos+1] == "D" or s[pos+1] == "M"):
                i = translator[i]
                total -= i

            else:
                i = translator[i]
                total += i

            print(total)
        
        return total