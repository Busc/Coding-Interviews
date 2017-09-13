# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return 0
        # 需要比较：当前值、当前和、最大和
        for i in range(len(array)):
            if i == 0:
                greatSum = array[0]
                currSum = array[0]
            else:
                # 当前和小于当前值时当前和被抛弃
                if currSum <= 0:
                    currSum = array[i]
                else:
                    currSum += array[i]
            # 当前和大于最大和时最大和更新
            if currSum > greatSum:
                greatSum = currSum
        return greatSum
