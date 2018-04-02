class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums = sorted(nums)
        length = len(nums)
        if (length % 2 == 0):
            median = (nums[int(length/2)] + nums[int(length/2)-1]) / 2
        else:
            median = nums[int(length/2)]
        return median
