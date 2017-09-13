# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        length = len(numbers)
        res = numbers[0]
        times = 1
        for i in range(1, length):
            if times == 0:
                res = numbers[i]
                times = 1
            elif numbers[i] == res:
                times += 1
            else:
                times -= 1
        return res if numbers.count(res) * 2 > length else 0