class Solution:
    def NumberOf1(self, n):
        # write code here
        return sum([(n >> i & 1) for i in range(32)])
        # 负数：补码 = 反码 + 1
