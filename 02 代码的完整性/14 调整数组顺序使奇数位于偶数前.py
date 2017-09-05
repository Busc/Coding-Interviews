class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = filter(lambda x: x % 2 == 1, array)
        even = filter(lambda x: x % 2 == 0, array)
        return odd+even