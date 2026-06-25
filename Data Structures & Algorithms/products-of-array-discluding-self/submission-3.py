class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]

        length = len(nums)

        for i in range(1, length):
            prefix.append(prefix[-1] * nums[i-1])

        for i in range(length - 2, -1, -1):
            suffix.append(suffix[-1] * nums[i+1])

        suffix.reverse()

        return [p * s for p, s in zip(prefix, suffix)]