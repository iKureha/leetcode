class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if  len(nums) == 0:
            return [-1, -1]
        if target < nums[0]:
            return [-1, -1]
        if target > nums[-1]:
            return [-1, -1]
        
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
            if nums[i] > target:
                break
                
        if result:
            return [result[0], result[-1]]
        else:
            return [-1, -1]
            
        
