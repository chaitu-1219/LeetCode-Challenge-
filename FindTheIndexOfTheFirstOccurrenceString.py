class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Finds the index of the first occurrence of 'needle' in 'haystack'.
        Returns -1 if 'needle' is not part of 'haystack'.

        Args:
            haystack: The string to search within.
            needle: The substring to look for.

        Returns:
            The starting index of the first match, or -1 if not found.
        """

        # Step 1: Quick sanity check.
        # If the haystack is shorter than the needle, the needle
        # can never fit inside, so no match is possible. Return -1 early.
        if len(haystack) < len(needle):
            return -1

        # Step 2: Slide a window over every possible starting position.
        # We iterate 'i' from 0 to the last index of the haystack.
        for i in range(len(haystack)):

            # Step 3: Extract a slice of the haystack that is exactly
            # the same length as the needle, starting at index 'i'.
            # Example: if needle is 2 chars long and i=2,
            # we grab haystack[2] and haystack[3].
            candidate = haystack[i:i + len(needle)]

            # Step 4: Compare the extracted slice to the needle.
            # If they are equal, we found the match, so return 'i'.
            if candidate == needle:
                return i

        # Step 5: If the loop finishes without any match,
        # the needle is not present. Return -1.
        return -1


def main():
    """Main entry point to test the strStr method with examples."""

    # Create an instance of the Solution class.
    solver = Solution()

    # Test case 1: needle found in the middle of haystack.
    haystack1, needle1 = "hello", "ll"
    result1 = solver.strStr(haystack1, needle1)
    print(f"strStr('{haystack1}', '{needle1}') = {result1}")  # Expected: 2

    # Test case 2: needle found at the very beginning.
    haystack2, needle2 = "sadbutsad", "sad"
    result2 = solver.strStr(haystack2, needle2)
    print(f"strStr('{haystack2}', '{needle2}') = {result2}")  # Expected: 0

    # Test case 3: needle not present.
    haystack3, needle3 = "leetcode", "leeto"
    result3 = solver.strStr(haystack3, needle3)
    print(f"strStr('{haystack3}', '{needle3}') = {result3}")  # Expected: -1

    # Test case 4: empty needle (edge case -> returns 0).
    haystack4, needle4 = "abc", ""
    result4 = solver.strStr(haystack4, needle4)
    print(f"strStr('{haystack4}', '{needle4}') = {result4}")  # Expected: 0

    # Test case 5: needle longer than haystack (early -1 branch).
    haystack5, needle5 = "a", "aa"
    result5 = solver.strStr(haystack5, needle5)
    print(f"strStr('{haystack5}', '{needle5}') = {result5}")  # Expected: -1


# This standard Python idiom runs main() only when the script
# is executed directly (not when it's imported as a module).
if __name__ == "__main__":
    main()
