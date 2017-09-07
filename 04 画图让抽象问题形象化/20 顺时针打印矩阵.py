# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return []
        vals = []
        origin = 0
        rows = len(matrix)
        cols = len(matrix[0])
        while rows > origin * 2 and cols > origin * 2:
            # endCol = cols-origin-1
            # endRow = rows-origin-1
            # left--right(must)
            vals += matrix[origin][origin:cols-origin]
            # up--down
            if origin+1 != rows-origin:
                for i in range(origin+1, rows-origin):
                    vals.append(matrix[i][cols-origin-1])
            # right--left
            if cols-origin-2 != origin-1 and rows-origin-1 != origin:
                for i in range(cols-origin-2, origin-1, -1):
                    vals.append(matrix[rows-origin-1][i])
            # down--up
            if rows-origin-2 != origin and origin != cols-origin-1:
                for i in range(rows-origin-2, origin, -1):
                    vals.append(matrix[i][origin])
            origin += 1
        return vals