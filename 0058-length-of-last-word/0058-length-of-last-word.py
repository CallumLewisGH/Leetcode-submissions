class Solution(object):
    def lengthOfLastWord(self, s): 
        wordLength = 0
        for i in range(1,len(s)):
            index = len(s) - i

            if s[index] != " ":
                wordLength += 1

            elif wordLength != 0:
                return wordLength


