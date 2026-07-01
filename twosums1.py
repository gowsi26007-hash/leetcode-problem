class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in seen:
                return [seen[difference], i]

            seen[nums[i]] = i