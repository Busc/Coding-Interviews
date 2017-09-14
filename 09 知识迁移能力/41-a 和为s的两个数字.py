# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        length = len(array)
        if length <= 2:
            return []
        low, high = 0, length-1
        while low < high:
            sumTwo = array[low] + array[high]
            if sumTwo < tsum:
                low += 1
            elif sumTwo > tsum:
                high -= 1
            else:
                return [array[low], array[high]]
        return []