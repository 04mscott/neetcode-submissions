class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        longest = 1
        curr = 1

        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                prev = num
                while prev + 1 in num_set:
                    curr += 1
                    prev += 1
                longest = max(longest, curr)
            curr = 1

        return longest