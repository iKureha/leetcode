class Solution:
    def isPalindrome(self, x):
        result = False
        if (x >= 0):
            temp = list(str(x))
            temp.reverse()
            if (str(x) == "".join(temp)):
                result = True
        return result
        
