from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Step 1: Set up two pointers for the search range
        # 'left' starts at the beginning of the array, 'right' at the end
        left = 0
        right = len(nums) - 1

        # Step 2: Loop while the search range is still valid
        # (i.e., left hasn't passed right)
        while left <= right:
            # Step 3: Find the middle index of the current range
            # Integer division ensures it's always a whole number
            mid = (left + right) // 2

            # Step 4: Compare the middle element with the target
            if nums[mid] == target:
                # Case A: Found the target — return its index
                return mid
            elif nums[mid] > target:
                # Case B: Middle value is too large
                # Target must be in the LEFT half, so narrow the range
                # by moving 'right' just below 'mid'
                right = mid - 1
            else:
                # Case C: Middle value is too small
                # Target must be in the RIGHT half, so narrow the range
                # by moving 'left' just above 'mid'
                left = mid + 1
        
        # Step 5: If we exit the loop, target wasn't found
        # 'left' now points to where the target SHOULD be inserted
        # to keep the array sorted
        return left


def main():
    # --- Test 1: Target exists in the array ---
    nums1 = [1, 3, 5, 6]
    target1 = 5
    solution = Solution()
    result1 = solution.searchInsert(nums1, target1)
    print(f"nums = {nums1}, target = {target1} → index {result1}")
    # Expected: 2 (5 is at index 2)

    # --- Test 2: Target should be inserted in the middle ---
    nums2 = [1, 3, 5, 6]
    target2 = 2
    result2 = solution.searchInsert(nums2, target2)
    print(f"nums = {nums2}, target = {target2} → index {result2}")
    # Expected: 1 (2 fits between 1 and 3)

    # --- Test 3: Target should be inserted at the end ---
    nums3 = [1, 3, 5, 6]
    target3 = 7
    result3 = solution.searchInsert(nums3, target3)
    print(f"nums = {nums3}, target = {target3} → index {result3}")
    # Expected: 4 (7 goes after 6, at index 4)

    # --- Test 4: Target should be inserted at the start ---
    nums4 = [1, 3, 5, 6]
    target4 = 0
    result4 = solution.searchInsert(nums4, target4)
    print(f"nums = {nums4}, target = {target4} → index {result4}")
    # Expected: 0 (0 goes before everything, at index 0)


# Only run main() when this file is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()
