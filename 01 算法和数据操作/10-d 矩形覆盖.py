class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        elif number == 1:
            return 1
        elif number == 2:
            return 2
        else:
            val1, val2 = 1, 2
            for i in range(3, number+1):
                val1, val2 = val2, val1+val2
            return val2
