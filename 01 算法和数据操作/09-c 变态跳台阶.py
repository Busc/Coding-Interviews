class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number <=0:
            return 0
        #else:
        #    return pow(2,number-1)
        stepWay = [0]
        for i in range(1, number+1):
            stepWay.append(sum(stepWay[0:i])+1)
        return stepWay[number]
