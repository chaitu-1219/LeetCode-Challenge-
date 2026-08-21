from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # If the list is empty, there is no common prefix
        if not strs:
            return ""

        # Sort the strings alphabetically
        strs.sort()

        # Get the first string
        first = strs[0]

        # Get the last string
        last = strs[-1]

        # Store the common prefix
        ans = ""

        # Compare characters up to the length
        # of the shorter string
        for i in range(min(len(first), len(last))):

            # If characters are different,
            # the common prefix ends here.
            if first[i] != last[i]:
                break

            # Add matching character to answer
            ans += first[i]

        # Return the common prefix
        return ans


# Main method
if __name__ == "__main__":

    # Ask the user for number of strings
    n = int(input("Enter number of strings: "))

    # Create empty list
    strs = []

    # Read strings
    print("Enter the strings:")

    for _ in range(n):
        strs.append(input())

    # Create Solution object
    obj = Solution()

    # Find longest common prefix
    result = obj.longestCommonPrefix(strs)

    # Display result
    print("Longest Common Prefix:", result)
