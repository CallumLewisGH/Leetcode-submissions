class Solution(object):
    def lengthOfLastWord(self, s):  
        count = 1        
        wordList = s.split(" ")
        while True:
            if len(wordList[-count]) != 0:
                return len(wordList[- count])
            count += 1

        

