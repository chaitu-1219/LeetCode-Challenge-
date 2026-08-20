from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Adds 1 to a number represented as a list of digits.

        The array holds a number's digits in order, e.g. [1,2,3] = 123.
        This method adds one and returns the result as a list of digits.

        Args:
            digits: A list of integers, each between 0 and 9.

        Returns:
            A list of integers representing the input number plus one.
        """

        # Step 1: Iterate through the digits from RIGHT to LEFT.
        # We process the least significant digit first, just like
        # adding 1 by hand on paper. The loop starts at the last
        # index (len-1) and stops at index 0 (range's -1 stops
        # before reaching -1, so we end exactly at the first digit).
        for i in range(len(digits) - 1, -1, -1):

            # Step 2: Check if adding 1 to this digit causes a "carry".
            # - If digits[i] + 1 is NOT 10, no carry is needed.
            #   Example: digit 3 + 1 = 4, which stays a single digit.
            #   We can add 1 here and we're done — no other digit
            #   is affected, so we return the updated list immediately.
            if digits[i] + 1 != 10:
                digits[i] += 1   # add 1 to the current digit in place
                return digits    # job finished, hand back the result

            # Step 3: If we reach here, digits[i] is 9 (since 9+1 = 10).
            # Adding 1 turns this position into 0, and the extra "1"
            # must be carried over to the next digit on the left.
            digits[i] = 0

            # Step 4: Handle the special case of an ALL-NINES number.
            # If we've carried all the way to the very first digit
            # (index 0) and it also became 0, then every existing
            # digit rolled over. We need a NEW leading digit 1 in front.
            # Example: [9,9] -> we set both to 0, then prepend 1 -> [1,0,0].
            if i == 0:
                return [1] + digits

            # Step 5: If i is NOT 0, we don't return yet. The loop
            # automatically moves one step LEFT (i becomes i-1) and
            # repeats. There, Step 2 checks whether the carry can be
            # absorbed (digit < 9) or whether it must keep rolling
            # over (digit == 9). This repeats until the carry lands
            # or we overflow at index 0.

    # ------------------------------------------------------------
    # main() — a small demo driver to test the method above.
    # ------------------------------------------------------------
def main():
    # Create an instance of the Solution class (the method is
    # an instance method, so we need an object to call it on).
    solution = Solution()

    # Step A: Define a few test inputs.
    # Each list represents a number where the digits are in order.
    test_cases = [
        [1, 2, 3],   # represents 123
        [4, 3, 2, 1] # represents 4321
    ]

    # Step B: Loop over each test case and run plusOne on it.
    for nums in test_cases:
        # Step C: Call plusOne and print the result nicely.
        # We convert the list to a string for clean, readable output.
        # For [1,2,3]: "123 + 1 = 124" and prints "[1, 2, 4]".
        print(f"{nums} + 1 = {solution.plusOne(nums)}")

    # Step D: Test the trickiest case — an all-nines number.
    print(f"{[9, 9]} + 1 = {solution.plusOne([9, 9])}")  # expect [1, 0, 0]


# Standard Python guard: only run main() when this script is
# executed directly (not when it is imported as a module).
if __name__ == "__main__":
    main()
