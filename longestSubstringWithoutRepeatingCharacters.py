class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ""
        max_len = 0
        for i in s:
            if i not in substring:
                substring += i
            else:
                if (substring.find(i)+1 == len(substring)):
                    substring = i
                else:
                    substring = substring[substring.find(i)+1:] + i
            if (max_len < len(substring)): max_len = len(substring)
        return max_len
