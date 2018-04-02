class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
            temp = target - i
            if (temp != i or nums.count(i) > 1):
                if (temp in nums):
                    if (nums.count(i) > 1):
                        result = [nums.index(i), nums.index(i, nums.index(i)+1)]
                    else:
                        result = [nums.index(i), nums.index(temp)]
                    break
        return result
