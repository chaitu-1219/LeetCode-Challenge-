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
            candidate = haystack[i:i + len(needle)]

            # Step 4: Compare the extracted slice to the needle.
            # If they are equal, we found the match, so return 'i'.
            if candidate == needle:
                return i

        # Step 5: If the loop finishes without any match,
        # the needle is not present. Return -1.
        return -1


def main():
    solution = Solution()

    # Test case 1: needle found in the middle
    print(f"strStr('sadbutsad', 'sad') = {solution.strStr('sadbutsad', 'sad')}")  # Expected: 0

    # Test case 2: needle not present
    print(f"strStr('leetcode', 'leeto') = {solution.strStr('leetcode', 'leeto')}")  # Expected: -1

    # Test case 3: needle found not at the start
    print(f"strStr('hello', 'll') = {solution.strStr('hello', 'll')}")  # Expected: 2

    # Test case 4: empty needle (conventionally returns 0)
    print(f"strStr('abc', '') = {solution.strStr('abc', '')}")  # Expected: 0

    # Test case 5: empty haystack with non-empty needle
    print(f"strStr('', 'a') = {solution.strStr('', 'a')}")  # Expected: -1

    # Test case 6: needle longer than haystack
    print(f"strStr('ab', 'abc') = {solution.strStr('ab', 'abc')}")  # Expected: -1

    # Test case 7: needle present multiple times (returns first occurrence)
    print(f"strStr('aaa', 'a') = {solution.strStr('aaa', 'a')}")  # Expected: 0

    # Test case 8: needle at the very end
    print(f"strStr('abcdef', 'def') = {solution.strStr('abcdef', 'def')}")  # Expected: 3


if __name__ == "__main__":
    main()
