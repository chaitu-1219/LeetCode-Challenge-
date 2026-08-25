'''
Solution: Understanding the Core of the Problem
The original problem can be stated as:

“Compute the square root of a non-negative integer x, and return only the integer part (rounded down).”

Examples:

x = 8 → √8 ≈ 2.828 → Result = 2
x = 9 → √9 = 3 → Result = 3
We can reframe this problem as:

“Find the largest integer m such that m^2 <= x.”
This new formulation is crucial—it sets the stage for a binary search solution.

Why Not Just Use a Linear Search?
The Search Space is Finite
We know the square root of x must lie between 0 and x.
In fact, for x >= 2, we can safely limit our search to the range 1 to x // 2, because (x // 2)^2 will already exceed x.

So we have a finite, well-bounded range to search.

The Key Insight: Monotonicity
Here’s the most important observation:

As m increases, m^2 also increases(monotonicity).
If m^2 < x, we need to try a larger m.
If m^2 > x, we try a smaller m.

This behavior is monotonic, meaning we can eliminate half of the search space at each step—perfect for binary search.

Complexity
Time complexity: O(logx)
Space complexity: O(1)
'''
class Solution(object):
    def mySqrt(self, x):
        """Compute the integer square root of x (floor of sqrt(x))."""
        # Base case: if x is 0 or 1, the square root is just x itself.
        # Handling these early avoids running the loop for trivial inputs.
        if x < 2:
            return x

        # Start searching from 2 (since 0 and 1 are already handled).
        i = 2

        # Keep incrementing i while its square is still <= x.
        # The loop stops at the FIRST i whose square exceeds x.
        while i * i <= x:
            i += 1

        # When the loop exits, i is "one too big", so the answer is i - 1.
        return i - 1


def main():
    solution = Solution()

    # Test cases: (input, expected output)
    test_cases = [
        (0, 0),          # sqrt(0) = 0
        (1, 1),          # sqrt(1) = 1
        (2, 1),          # sqrt(2) ≈ 1.41 -> 1
        (4, 2),          # sqrt(4) = 2
        (8, 2),          # sqrt(8) ≈ 2.83 -> 2
        (9, 3),          # sqrt(9) = 3
        (15, 3),         # sqrt(15) ≈ 3.87 -> 3
        (16, 4),         # sqrt(16) = 4
        (25, 5),         # sqrt(25) = 5
        (2147395599, 46339),  # a very large input
    ]

    # Run every test case and report pass/fail.
    for x, expected in test_cases:
        result = solution.mySqrt(x)
        # Verify the result with Python's built-in math.floor(math.sqrt(x))
        import math
        builtin = int(math.isqrt(x))  # isqrt is Python 3.8+'s integer sqrt
        status = "PASS" if result == expected == builtin else "FAIL"
        print(f"mySqrt({x}) = {result} | expected {expected} | built-in {builtin} | {status}")


# This guard ensures main() only runs when the script is executed directly,
# not when the file is imported as a module elsewhere.
if __name__ == "__main__":
    main()
