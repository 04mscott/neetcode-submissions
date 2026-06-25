class Solution:
    def trap(self, height: List[int]) -> int:
        total_area = 0
        for curr_height in range(max(height), 0, -1):
            indices = [i for i, x in enumerate(height) if x >= curr_height]
            prev = indices[0]
            for idx in indices[1:]:
                total_area += idx - prev - 1
                prev = idx
        return total_area