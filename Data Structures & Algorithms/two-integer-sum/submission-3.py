class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num = nums[i]
            if target - num in nums[i + 1:]:
                j = i + nums[i + 1:].index(target - num) + 1
                return [i, j]