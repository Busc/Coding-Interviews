# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        length = len(A)
        B = [1] * length
        for i in range(1, length):
            B[i] = B[i-1] * A[i-1]
        temp = 1
        for i in range(length-2, -1, -1):
            temp *= A[i+1]
            B[i] *= temp
        return B