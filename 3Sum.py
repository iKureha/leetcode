class Solution:
    def threeSum(self, nums):
        solution = []
        nums.sort()

        temp_sum = 0
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            l, r = i+1, len(nums)-1
            while (l < r):
                # print(nums[i], nums[l], nums[r])
                temp_sum = nums[i] + nums[l] + nums[r]
                if (temp_sum > 0):
                    r -= 1
                elif (temp_sum < 0):
                    l += 1
                else:
                    solution.append([nums[i], nums[l], nums[r]])
                    while (l < r) and (nums[l] == nums[l+1]):
                        l += 1
                    while (l < r) and (nums[r] == nums[r-1]):
                        r -= 1
                    l += 1
                    r -= 1
                        

        return solution
