# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        left, right = 0, len(rotateArray)-1
        # 考虑到数组本身就是有序的情况
        mid = 0
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                return rotateArray[right]
            mid = (right + left) // 2
            if rotateArray[left] == rotateArray[mid] and rotateArray[right] == rotateArray[mid]:
                # 无法判断最小值在哪一段
                return self.orderSearch(rotateArray, left, right)
            if rotateArray[mid] >= rotateArray[left]:
                # 最小值位于后半段
                left = mid
            elif rotateArray[mid] <= rotateArray[right]:
                # 最小值位于前半段或者就是mid
                right = mid

    def orderSearch(self, rotateArray, firstInd, lastInd):
        minNum = rotateArray[firstInd]
        for i in range(firstInd+1, lastInd+1):
            if minNum > rotateArray[i]:
                minNum = rotateArray[i]
        return minNum
