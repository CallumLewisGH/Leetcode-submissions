class Solution(object):
    def isValidSudoku(self, board):
        subSudoku = []

        for i in range(9):
            tempLine = board[i][:]
            for nums in tempLine:
                if nums != '.':
                    tempLine.remove(nums)
                    if nums in tempLine:
                        return False
                

        for i in range(9):
            tempLine = []
            for n in range(9):
                tempLine.append(board[n][i])
        

            for nums in tempLine:
                if nums != '.':
                    tempLine.remove(nums)
                    if nums in tempLine:
                        return False
            


        squareStartList = [0,0,0,3,0,6, 3,0,3,3,3,6, 6,0,6,3,6,6,]
        for num in range(len(squareStartList)/2):
            squareStart1 = squareStartList[0]
            squareStart2 = squareStartList[1]
  
            for x in range(0, 3):
                for y in range(0, 3):
                    subSudoku.append(board[squareStart1 + x][squareStart2 + y])
            squareStartList.remove(squareStart1)
            squareStartList.remove(squareStart2)
            
            
            for i in range(9):
                for i in range(1,10):
                    if str(i) in subSudoku: 
                        tempLine = subSudoku[:]                               
                        tempLine.remove(str(i))    
                        if str(i) in tempLine:
                            return False

            
            subSudoku = []

        return True