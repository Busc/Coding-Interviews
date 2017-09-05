class Solution:
    def Fibonacci(self, n):
        # write code here
        # index from 0
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 39:
            return
        else:
            val1, val2 = 0, 1
            for i in range(2, n+1):
                val1, val2 = val2, val1+val2
            return val2