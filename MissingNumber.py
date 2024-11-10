class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        nums.sort()

        if nums[0] != 0:
            return 0

        for i in range(n - 1):
            if nums[i + 1] != nums[i] + 1:
                return nums[i] + 1
        
        return n
        