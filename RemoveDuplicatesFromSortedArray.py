class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Slow pointer = position for the next unique value.
        # Start at index 1 because nums[0] is always kept (nothing before it to duplicate).
        i = 1

        # Fast pointer j scans through the rest of the array.
        for j in range(1, len(nums)):
            # Compare current element with the last kept unique value.
            if nums[j] != nums[i - 1]:
                # It's a new unique value → place it at the slow pointer's position.
                nums[i] = nums[j]
                i += 1  # Advance slow pointer only for unique values.

        # i = count of unique elements; only nums[0:i] is valid.
        return i


def main():
    # Test case 1: array with duplicates.
    nums1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    sol = Solution()
    k1 = sol.removeDuplicates(nums1)
    print("nums1 after:", nums1[:k1])   # Expected: [0, 1, 2, 3, 4]
    print("k1 =", k1)                  # Expected: 5

    # Test case 2: array with no duplicates.
    nums2 = [1, 2, 3]
    k2 = sol.removeDuplicates(nums2)
    print("nums2 after:", nums2[:k2])   # Expected: [1, 2, 3]
    print("k2 =", k2)                  # Expected: 3

    # Test case 3: all elements are the same.
    nums3 = [7, 7, 7]
    k3 = sol.removeDuplicates(nums3)
    print("nums3 after:", nums3[:k3])   # Expected: [7]
    print("k3 =", k3)                  # Expected: 1


# Entry point: runs only when this file is executed directly.
if __name__ == "__main__":
    main()
