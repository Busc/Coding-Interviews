class Solution:
    # array 二维列表[][]
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
            if target in array[i]:
                return True
        return False

    def FindGenaral(self, target, array):
        rowNum = len(array)
        colNum = len(array[0])
        row = 0
        col =colNum - 1
        while row<rowNum and col>=0:
            if target == array[row][col]:
                return True
            elif target > array[row][col]:
                row += 1
            else:
                col -= 1
        return False
