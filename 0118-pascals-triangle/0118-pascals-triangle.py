class Solution(object):
    def generate(self, numRows):
        triangle = [[1]]
        row = [1]

        for i in range(numRows-1):
            nextRow = []
            row.insert(0, 0)
            row.append(0)

            for pos, i in enumerate(row):
                if pos == 0:
                    continue
                
                currentSum = row[pos] + row[pos-1]
                nextRow.append(currentSum)
            
            row = nextRow
            triangle.append(row[:])
        
        return triangle
        