class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # using hash table to reduce time complexity
        
        tempDict = {}
        for i in range(0, len(nums)):
            
            if nums[i] in tempDict.keys():
                return [tempDict[nums[i]], i]
            
            tempDict[target - nums[i]] = i
