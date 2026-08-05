from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Step 1: Sort the array so we can use the two-pointer technique
        # A sorted array lets us move pointers logically (left makes sums bigger, right makes them smaller)
        nums.sort()
        
        # Step 2: Initialize our best answer with the first three numbers
        # This is just a starting guess; we'll improve it as we scan
        result = nums[0] + nums[1] + nums[2]

        # Step 3: Fix the first number. We stop 2 early so left and right always have room.
        for i in range(len(nums) - 2):
            # left starts right after i, right starts at the end of the array
            left, right = i + 1, len(nums) - 1

            # Step 4: Shrink the window from both ends to try every pair for this fixed i
            while left < right:
                # Current sum of the three chosen numbers
                total = nums[i] + nums[left] + nums[right]

                # Step 5: If this sum is closer to target than our best so far, update result
                # abs(target - total) measures how "off" the sum is from the target
                if abs(target - total) < abs(target - result):
                    result = total

                # Step 6: Decide how to adjust the pointers
                if total == target:
                    # Perfect match found — can't get any closer, so return immediately
                    return target
                elif total < target:
                    # Sum is too small → move left right to pick a bigger number
                    left += 1
                else:
                    # Sum is too big → move right left to pick a smaller number
                    right -= 1

        # Step 7: After checking all combinations, return the closest sum found
        return result


def main():
    # --- Test cases ---
    test_cases = [
        ([-1, 2, 1, -4], 1),        # expected: 2  (-1 + 2 + 1 = 2)
        ([0, 0, 0], 1),             # expected: 0
        ([1, 1, 1, 0], -100),       # expected: 2  (1 + 1 + 0 = 2, closest to -100)
        ([-1, 2, 1, -4], -100),     # expected: -3 (-4 + 0 + 1... actually -4+2-1 = -3)
        ([1, 1, -1, -1, 3], -1),    # expected: -1 (perfect match)
    ]

    sol = Solution()

    for nums, target in test_cases:
        result = sol.threeSumClosest(nums, target)
        print(f"nums={nums}, target={target:>4}  →  closest sum = {result}")


if __name__ == "__main__":
    main()
