class Solution:
    def climbStairs(self, n: int) -> int:
        # Step 1: Base cases.
        # With 1 step: 1 way (1)
        # With 2 steps: 2 ways (1+1, 2)
        # With 3 steps: 3 ways (1+1+1, 1+2, 2+1)
        # In all these cases, the answer equals n itself.
        if n <= 3:
            return n

        # Step 2: Set up the "sliding window".
        # Instead of storing the whole Fibonacci-like sequence, we only
        # keep the two most recent results plus a variable for the current one.
        #
        # prev1 = ways to reach step 3 = 3
        # prev2 = ways to reach step 2 = 2
        # cur   = the answer being computed for the current step
        prev1 = 3
        prev2 = 2
        cur = 0

        # Step 3: Iterate from step 4 up to step n.
        # range(3, n) produces 3, 4, ..., n-1.
        # Notice it runs (n - 3) times total, computing steps 4 through n.
        for _ in range(3, n):
            # Step 4: The number of ways to reach the current step is the
            # sum of ways to reach the two previous steps.
            # (Your last move was either a 1-step from n-1 or a 2-step from n-2.)
            cur = prev1 + prev2

            # Step 5: Slide the window forward.
            # The old "n-1" becomes the new "n-2"...
            prev2 = prev1

            # ...and the newly computed answer becomes the new "n-1".
            prev1 = cur

        # Step 6: After the loop, cur holds the answer for step n.
        return cur


def main():
    # A small helper to make the output readable.
    def describe(n, result):
        return f"n={n:>2}  ->  {result:>3} ways"

    # Create an instance of the solution.
    sol = Solution()

    # Test the base cases and a few larger values.
    test_values = [1, 2, 3, 4, 5, 6, 7, 10, 20, 35]

    print("Climbing Stairs - number of distinct ways to reach the top")
    print("-" * 45)
    for n in test_values:
        result = sol.climbStairs(n)
        print(describe(n, result))


# Standard Python entry point: the program starts executing here.
if __name__ == "__main__":
    main()
