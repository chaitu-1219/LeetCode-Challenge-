from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Result list to store all unique triplets that sum to zero
        res = []
        
        # Step 1: Sort the array first.
        # Sorting is essential because:
        #   - It lets us use the two-pointer technique (efficient O(n^2) instead of O(n^3)).
        #   - It groups duplicates together so we can easily skip them.
        nums.sort()

        # Step 2: Outer loop fixes the first element nums[i].
        # We treat nums[i] as the "anchor" and find two other numbers
        # (nums[j], nums[k]) that sum to -nums[i].
        for i in range(len(nums)):
            # Skip duplicate values for the anchor.
            # After the first occurrence of a value at i, any later occurrence
            # would only produce duplicate triplets, so we skip them.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Two-pointer setup:
            #   j starts right after i (left pointer)
            #   k starts at the very end of the array (right pointer)
            j = i + 1
            k = len(nums) - 1

            # Step 3: Shrink the window with the two pointers.
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                # If the sum is too large, the only way to decrease it is to
                # move the right pointer left (toward smaller values).
                if total > 0:
                    k -= 1
                # If the sum is too small, move the left pointer right
                # (toward larger values) to increase the total.
                elif total < 0:
                    j += 1
                # If the sum equals zero, we found a valid triplet.
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    # Move j forward to look for other combinations.
                    j += 1

                    # Skip duplicate values for j so we don't record the same
                    # triplet more than once. Check bounds first to avoid
                    # an IndexError.
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        
        # Return all found unique triplets.
        return res


# Standard test harness for running the solution directly
def main():
    solution = Solution()
    
    # Test cases: (input list, expected output)
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([], []),
        ([1, 2, -2, -1], []),
    ]
    
    for i, (nums, expected) in enumerate(test_cases, 1):
        # Make a copy since threeSum sorts the list in place
        result = solution.threeSum(nums.copy())
        status = "PASS" if result == expected else "FAIL"
        print(f"Test {i} [{status}]:")
        print(f"  Input:    {nums}")
        print(f"  Expected: {expected}")
        print(f"  Got:      {result}")
        print()


if __name__ == "__main__":
    main()
