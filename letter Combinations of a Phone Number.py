from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: empty input means no combinations
        if not digits:
            return []

        # Mapping each digit to its possible letters on a phone keypad
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

        def backtrack(idx: int, comb: str) -> None:
            """
            Recursively builds letter combinations.
            
            idx  : current position in the digits string
            comb : the combination built so far (a string)
            
            Base case: when idx reaches the end of digits,
            the current combination is complete — add a copy to results.
            """
            if idx == len(digits):
                res.append(comb[:])
                return

            # Try every letter mapped to the current digit
            for letter in digit_to_letters[digits[idx]]:
                # Recurse to the next digit, appending this letter
                backtrack(idx + 1, comb + letter)

        res = []
        backtrack(0, "")
        return res


if __name__ == "__main__":
    sol = Solution()

    # Test cases
    test_cases = ["23", "", "2", "79"]

    for digits in test_cases:
        result = sol.letterCombinations(digits)
        print(f"digits = {digits!r:6} -> combinations: {result}")
