import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(math.prod(
                [num for idx, num in enumerate(nums) if idx != i]
            ))
        return output