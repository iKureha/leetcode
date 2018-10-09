class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        if target > nums[-1]:
            return len(nums)
        if target == nums[-1]:
            return len(nums) - 1
        if target <= nums[0]:
            return 0
       
        for i in range(len(nums)):
            if nums[i] >= target:
                return i   
        
