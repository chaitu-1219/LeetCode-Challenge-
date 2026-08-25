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
