class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        l, r = 0, len(nums) - 1
        pairs = []

        while l < r:
            if nums[l] + nums[r] == target:
                pairs.append([nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while r > l and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1

        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        result = []
        seen = set()
        for i, num in enumerate(sorted_nums):
            triples = [[num] + pair for pair in self.twoSum(sorted_nums[i + 1:], 0-num)]
            for triple in triples:
                if len(triple) == 3 and tuple(sorted(triple)) not in seen:
                    result.append(triple)
                    seen.add(tuple(sorted(triple)))
        return result