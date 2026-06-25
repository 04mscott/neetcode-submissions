class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        longest = 1
        curr = 1

        nums_sorted = sorted(set(nums))
        prev = nums_sorted[0]
        for num in nums_sorted[1:]:
            if num == prev + 1:
                curr += 1
            else:
                curr = 1
            if curr > longest:
                longest = curr
            prev = num
        return longest