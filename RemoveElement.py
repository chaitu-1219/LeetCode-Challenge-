from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Removes all occurrences of 'val' from the array in-place.
        
        Time complexity: O(n) - single pass through the array
        Space complexity: O(1) - only uses a constant amount of extra space
        
        Approach: Two-pointer technique
        - 'k' is a slow pointer that tracks where the next valid element should go
        - 'i' is a fast pointer that scans through the entire array
        """
        # k is the index where the next different-from-val element will be placed.
        # It also ends up being the count of elements that are NOT equal to val.
        k = 0

        # i (the fast pointer) scans every element in the array once.
        for i in range(len(nums)):
            
            # If the current element (at position i) is NOT equal to val,
            # we want to keep it. So we copy it to the front of the array
            # at position 'k' (the slow pointer's current location).
            if nums[i] != val:
                
                # Copy the valid element to the current 'k' position.
                nums[k] = nums[i]
                
                # Move the slow pointer forward so the next valid element
                # goes into the next slot.
                k += 1
            # If nums[i] == val, we simply skip it (do nothing).
            # The fast pointer 'i' still advances via the loop; the slow
            # pointer 'k' stays put, effectively "overwriting" the val later.

        # After the loop, all elements not equal to val are at indexes 0..k-1.
        # The rest of the array content beyond index k is irrelevant per the
        # problem's rules (we only need the first k elements to be correct).
        return k


def main():
    """
    Test cases to verify the removeElement method works correctly.
    """
    solution = Solution()

    # ---- Test Case 1: Basic case ----
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    # Expected: k = 2, and the first 2 elements of nums1 are [2, 2]
    print(f"Test 1 - nums: {nums1}, val: {val1}, k: {k1}")
    print(f"  First {k1} elements: {nums1[:k1]}")  # Output: [2, 2]
    print(f"  Passed: {k1 == 2 and nums1[:k1] == [2, 2]}")
    print()

    # ---- Test Case 2: Remove a value appearing multiple times ----
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    # Expected: k = 5, first 5 elements are [0, 1, 3, 0, 4]
    print(f"Test 2 - nums: {nums2}, val: {val2}, k: {k2}")
    print(f"  First {k2} elements: {nums2[:k2]}")  # Output: [0, 1, 3, 0, 4]
    print(f"  Passed: {k2 == 5 and nums2[:k2] == [0, 1, 3, 0, 4]}")
    print()

    # ---- Test Case 3: Empty array ----
    nums3 = []
    val3 = 1
    k3 = solution.removeElement(nums3, val3)
    # Expected: k = 0
    print(f"Test 3 - nums: {nums3}, val: {val3}, k: {k3}")
    print(f"  Passed: {k3 == 0}")
    print()

    # ---- Test Case 4: No matches (val not present) ----
    nums4 = [4, 5, 6]
    val4 = 9
    k4 = solution.removeElement(nums4, val4)
    # Expected: k = 3, array unchanged
    print(f"Test 4 - nums: {nums4}, val: {val4}, k: {k4}")
    print(f"  Passed: {k4 == 3 and nums4 == [4, 5, 6]}")
    print()

    # ---- Test Case 5: All elements match val ----
    nums5 = [7, 7, 7]
    val5 = 7
    k5 = solution.removeElement(nums5, val5)
    # Expected: k = 0
    print(f"Test 5 - nums: {nums5}, val: {val5}, k: {k5}")
    print(f"  Passed: {k5 == 0}")
    print()

    # ---- Test Case 6: Single element that doesn't match ----
    nums6 = [1]
    val6 = 2
    k6 = solution.removeElement(nums6, val6)
    # Expected: k = 1
    print(f"Test 6 - nums: {nums6}, val: {val6}, k: {k6}")
    print(f"  Passed: {k6 == 1 and nums6[:k6] == [1]}")


# Entry point of the script - this runs when the file is executed directly.
if __name__ == "__main__":
    main()
