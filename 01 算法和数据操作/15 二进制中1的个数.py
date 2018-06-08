class Solution:
    def NumberOf1(self, n):
        # write code here
        # return sum([(n >> i & 1) for i in range(32)])
        # 负数：补码 = 反码 + 1
        # 把一个整数减去1后再和原来的整数做 位与 运算，得到的结果相当于把整数的二进制表示中 最右边的1变成0
        count = 0
        while n:
            n = (n-1) & n
            count += 1
        return count
