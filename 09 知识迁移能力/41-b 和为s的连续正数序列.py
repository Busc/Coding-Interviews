# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small, big = 1, 2
        mid = (tsum + 1) // 2
        # 利用currSum减少不必要的计算量
        currSum = small + big
        output = []
        while small < mid:
            if currSum < tsum:
                big += 1
                currSum += big
            elif currSum > tsum:
                currSum -= small
                small += 1
            else:
                output.append(range(small, big+1))
                big += 1
                currSum += big
        return output

