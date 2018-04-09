class Solution:
    
    def calculate(self, s, left, right):
        result = ""
        while (left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        result = s[left+1:right]
        return result
    
    def longestPalindrome(self, s):
        result = ""
        for i in range(len(s)):
            len1 = self.calculate(s, i, i)
            len2 = self.calculate(s, i, i+1)
            
            if (len(len1) > len(len2)):
                temp = len1
            else:
                temp = len2
            if (len(temp) > len(result)):
                result = temp
            
        return result
        
