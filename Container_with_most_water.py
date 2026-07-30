class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize: best area so far, left pointer, right pointer
        max_area = 0
        left = 0
        right = len(height) - 1

        # Shrink the window from both ends until pointers meet
        while left < right:
            # Calculate current container's area:
            # width = right - left, height = shorter of the two lines
            current_area = (right - left) * min(height[left], height[right])
            
            # Keep the larger area
            max_area = max(max_area, current_area)

            # Move the pointer at the shorter line inward
            # (keeping it would never yield a larger area)
            if height[left] < height[right]:
                left += 1          # left line is shorter, move it right
            else:
                right -= 1         # right line is shorter or equal, move it left

        return max_area
