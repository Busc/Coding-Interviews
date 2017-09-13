# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        uglyNums = [1]
        ind2 = ind3 = ind5 = 0
        for _ in range(1, index):
            uglyNums.append(min(uglyNums[ind2]*2, uglyNums[ind3]*3, uglyNums[ind5]*5))
            if uglyNums[-1] == uglyNums[ind2]*2:
                ind2 += 1
            if uglyNums[-1] == uglyNums[ind3]*3:
                ind3 += 1
            if uglyNums[-1] == uglyNums[ind5]*5:
                ind5 += 1
        return uglyNums[-1]
