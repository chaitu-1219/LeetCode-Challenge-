from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Step 1: Sort the array. Sorting enables the two-pointer trick
        # and makes duplicate elements appear consecutively.
        nums.sort()
        res = []  # Stores the resulting unique quadruplets

        # Step 2: Fix the FIRST number of the quadruplet.
        # We stop at len(nums)-3 to guarantee at least 3 elements remain
        # for the other positions.
        for i in range(len(nums) - 3):
            # Skip duplicate starting values for the first number.
            # If nums[i] equals the previous element, we've already
            # considered every quadruplet starting with this value.
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Step 3: Fix the SECOND number of the quadruplet.
            # Starts after i, stops at len(nums)-2 so at least 2 elements
            # remain for the two pointers.
            for j in range(i+1, len(nums) - 2):
                # Skip duplicate starting values for the second number.
                # Edge case: j == i+1 is always allowed because that's a
                # different index even if values match somehow.
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                # Step 4: Set up two pointers for the remaining two numbers.
                # left starts right after j, right starts at the array end.
                left, right = j + 1, len(nums) - 1

                # Step 5: Two-pointer scan.
                # Since the array is sorted, we can adjust the sum:
                #   - too small  -> move left up (increases sum)
                #   - too large  -> move right down (decreases sum)
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if four_sum == target:
                        # Found a valid quadruplet. Add it to results.
                        res.append([nums[i], nums[j], nums[left], nums[right]])

                        # Move both pointers inward.
                        left += 1
                        right -= 1

                        # Skip duplicates for the THIRD number (left side).
                        # Prevent identical quadruplets from being added again.
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # Skip duplicates for the FOURTH number (right side).
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif four_sum < target:
                        # Sum is too small; we need larger numbers, so
                        # advance the left pointer.
                        left += 1
                    else:
                        # Sum is too large; we need smaller numbers, so
                        # retreat the right pointer.
                        right -= 1

        return res


def main():
    """Main method to test the fourSum solution with sample cases."""
    solution = Solution()

    # Test case 1: Standard example from LeetCode
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    result1 = solution.fourSum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")
    print()

    # Test case 2: Another standard example
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    result2 = solution.fourSum(nums2, target2)
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")
    print()

    # Test case 3: Empty or insufficient elements
    nums3 = []
    target3 = 0
    result3 = solution.fourSum(nums3, target3)
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")
    print()

    # Test case 4: Duplicate-heavy array
    nums4 = [0, 0, 0, 0]
    target4 = 0
    result4 = solution.fourSum(nums4, target4)
    print(f"Input: nums = {nums4}, target = {target4}")
    print(f"Output: {result4}")
    print()

    # Test case 5: Negative and positive mix
    nums5 = [-3, -2, -1, 0, 0, 1, 2, 3]
    target5 = 0
    result5 = solution.fourSum(nums5, target5)
    print(f"Input: nums = {nums5}, target = {target5}")
    print(f"Output: {result5}")


# Standard Python idiom: only run main() when this file is executed directly.
if __name__ == "__main__":
    main()
