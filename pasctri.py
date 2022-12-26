class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [[]] * numRows
        l[0] = [1]
        for i in range(1, numRows): #i is current row
            rowList = [0] * (i + 1)
            for j in range(i + 1): #j is index in current row
                left = 0
                right = 0
                lastRow = l[i - 1]
                if j > 0:
                    left = lastRow[j - 1]
                if j < len(lastRow):
                    right = lastRow[j]
                rowList[j] = left + right
            l[i] = rowList
        return l
