from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # res will store all valid combinations of parentheses
        res = []

        # dfs is a recursive function that builds a valid string character by character.
        #   openP  -> number of '(' currently placed
        #   closeP -> number of ')' currently placed
        #   s      -> the string built so far
        def dfs(openP: int, closeP: int, s: str) -> None:
            # BASE CASE: A valid complete string is formed when we have used
            # exactly n open and n close parentheses (2*n total characters),
            # AND the counts are equal (which guarantees it's balanced).
            if openP == closeP and openP + closeP == n * 2:
                res.append(s)   # save this valid string
                return          # stop recursing down this path

            # RECURSIVE CASE 1: Add an opening '('.
            # We can only add an opening bracket if we haven't already used all n of them.
            if openP < n:
                dfs(openP + 1, closeP, s + "(")

            # RECURSIVE CASE 2: Add a closing ')'.
            # We can only add a closing bracket if we currently have more open than
            # close brackets (otherwise the parentheses would be mismatched).
            if closeP < openP:
                dfs(openP, closeP + 1, s + ")")

        # Kick off the recursion starting with 0 open, 0 close, and an empty string.
        dfs(0, 0, "")

        return res


# ---- main method to test the solution ----
def main():
    sol = Solution()
    for n in [1, 2, 3]:
        result = sol.generateParenthesis(n)
        print(f"n = {n} -> {result}")


if __name__ == "__main__":
    main()
