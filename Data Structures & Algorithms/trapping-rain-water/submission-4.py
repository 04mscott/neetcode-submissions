class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [height[0]]
        suffix = height[-1:]
        num_heights = len(height)
        
        for h in height[1:]:
            prefix.append(max(h, prefix[-1]))

        for h in reversed(height[1:]):
            suffix.append(max(h, suffix[-1]))
        suffix.reverse()

        area = 0
        for i in range(num_heights):
            value = min(prefix[i], suffix[i]) - height[i]
            if value > 0:
                area += value

        return area