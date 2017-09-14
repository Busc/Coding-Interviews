# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) != 5:
            return False
        # 排序
        numbers.sort()
        # 0的个数
        numZero = 0
        #for i in range(0,2):
        for i in range(0, 5):
            if numbers[i] == 0:
                numZero += 1
        # 统计空缺数目
        numBlank = 0
        for i in range(numZero, 4):
            # 出现了对子
            if numbers[i+1] == numbers[i]:
                return False
            numBlank += numbers[i+1]-numbers[i]-1
            if numBlank > numZero:
                return False
        return True




