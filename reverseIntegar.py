class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minus = 0
        if (x < 0):
            minus = 1
            x = abs(x)
        temp = list(str(x))
        temp.reverse()
        result = int("".join(temp))
        if (minus == 1):
            result = 0 - result
        if (result > 2 ** 31 or result < 1 + -1 * 2 **31 ):
            result = 0
        return result
