import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = nums[-1:]

        length = len(nums)

        for i in range(1, length):
            prefix.append(prefix[i-1] * nums[i])

        for i in range(length - 2, -1, -1):
            prev = suffix[0]
            suffix.insert(0, prev * nums[i])

        output = []
        for i in range(length):
            pre = 1 if i == 0 else prefix[i-1]
            suf = 1 if i == length - 1 else suffix[i+1]
            output.append(pre * suf)
        return output