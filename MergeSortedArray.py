class Solution(object):
    def merge(self, nums1, m, nums2, n):
        # ── SETUP: three pointers working from the back ─────────────
        # We fill nums1 from its END backwards. Why? Because writing
        # from the front would overwrite valid nums1 elements before
        # they get compared. Merging largest-first avoids that problem.

        # i = index of the last valid element in nums1 (goes leftward)
        i = m - 1

        # j = index of the last element in nums2 (goes leftward)
        j = n - 1

        # k = index where we write the next merged element.
        # It starts at the very end of nums1's total capacity.
        k = m + n - 1

        # ── MAIN LOOP ────────────────────────────────────────────────
        # We keep merging as long as nums2 still has elements to place.
        # Once j < 0, nums2 is exhausted and any leftover nums1 elements
        # are already in their correct sorted spots — no extra work needed.
        while j >= 0:

            # COMPARE the biggest unplaced elements from each array.
            # Two situations where we take from nums1:
            #   1) nums1 still has elements (i >= 0)
            #   2) nums1's current element is strictly larger than nums2's
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]  # place the bigger nums1 value at spot k
                i -= 1               # move i left to the next nums1 element

            # Otherwise we take from nums2. This covers:
            #   - nums1 is exhausted (i < 0)
            #   - nums2's element is >= nums1's element (tie → take nums2)
            # Breaking ties toward nums2 also naturally stops the loop
            # when nums1 runs dry.
            else:
                nums1[k] = nums2[j]  # place the nums2 value at spot k
                j -= 1               # move j left to the next nums2 element

            # After placing a value, move k one spot left so the NEXT
            # merge writes to the next available position from the end.
            k -= 1


# ── Extra reusable helper: prints merge result nicely ──────────────
def run_case(nums1, m, nums2, n, label=""):
    """Run one merge example and show before/after arrays."""
    original = nums1[:]                     # keep a copy to display later
    solution = Solution()
    solution.merge(nums1, m, nums2, n)      # merge in place
    print(f"{label} case:")
    print(f"  nums1 before: {original}")
    print(f"  nums2:        {nums2}")
    print(f"  merged:       {nums1}\n")


def main():
    # Each test case must satisfy: len(nums1) == m + n
    # (nums1 has empty 0 slots at the end reserved for nums2's elements)

    # Example 1 — given by the LeetCode prompt
    run_case([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, "Example 1")

    # Example 2 — nums1 is empty; everything comes from nums2
    run_case([0], 0, [1], 1, "Empty nums1")

    # Example 3 — nums2 is empty; no merging needed, nums1 unchanged
    run_case([1], 1, [], 0, "Empty nums2")

    # Example 4 — all nums1 elements are larger than all nums2 elements
    run_case([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, "nums1 all bigger")

    # Example 5 — duplicate / equal values across both arrays
    run_case([2, 2, 0, 0], 2, [2, 2], 2, "With duplicates")

    # Example 6 — single element each
    run_case([0], 0, [2], 1, "Single elements")


# ── Entry point ─────────────────────────────────────────────────────
# __name__ equals "__main__" only when this script is executed directly
# (not when imported as a module). This guard lets you safely import
# the Solution class elsewhere without running the demos.
if __name__ == "__main__":
    main()
