from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        # Edge case: Empty list
        if not strs:
            return ""

        # Sort the list alphabetically
        strs.sort()

        # Get the first and last strings
        first = strs[0]
        last = strs[-1]

        # Compare characters of first and last strings
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]

        return ans


# Driver Code
if __name__ == "__main__":
    n = int(input("Enter the number of strings: "))

    strs = []
    print("Enter the strings:")
    for _ in range(n):
        strs.append(input())

    obj = Solution()
    result = obj.longestCommonPrefix(strs)

    print("Longest Common Prefix:", result)
