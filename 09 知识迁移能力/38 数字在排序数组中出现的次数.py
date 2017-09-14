# -*- coding:utf-8 -*-
class Solution:
    # 地板除没错，但是用移位就会出错，不知道是什么原因
    def GetFirstK_rec(self, data, k, start, end):
        if start <= end:
            mid = start + (end - start) // 2
            if k < data[mid]:
                # k完全位于前半段
                end = mid - 1
            elif k > data[mid]:
                # k完全位于后半段
                start = mid + 1
            else:
                # 第一个k出现在前半段或者就是mid
                if mid == 0 or k != data[mid-1]:
                    return mid
                else:
                    end = mid - 1
        else:
            return -1
        return self.GetFirstK_rec(data, k, start, end)

    def GetLastK_loop(self, data, k, start, end):
        while start <= end:
            mid = start + (end - start) // 2
            if k < data[mid]:
                end = mid - 1
            elif k > data[mid]:
                start = mid + 1
            else:
                # 最后一个k出现在后半段或者就是mid
                if mid == len(data)-1 or k != data[mid+1]:
                    return mid
                else:
                    start = mid + 1
        return -1

    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        start = 0
        end = len(data) - 1
        firstK = self.GetFirstK_rec(data, k, start, end)
        lastK = self.GetLastK_loop(data, k, start, end)
        if firstK != -1 and lastK != -1:
            return lastK - firstK + 1
        return 0