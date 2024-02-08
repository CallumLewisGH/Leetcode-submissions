class Solution(object):
    def fizzBuzz(self, n):
        outputList = []
        for index in range(1,n+1):
            tempString = ""
            if index % 3 == 0:
                tempString += "Fizz"

            if index % 5 == 0:
                tempString += "Buzz"
            
            if index % 5 != 0 and index % 3 != 0:
                tempString += str(index)
            
            outputList.append(tempString)
            
        return outputList



                    



