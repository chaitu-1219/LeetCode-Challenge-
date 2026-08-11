class Solution:
    def isValid(self, s: str) -> bool:
        """
        Determines whether a string of brackets is valid.

        A string is valid if:
        1. Open brackets must be closed by the same type of bracket.
        2. Open brackets must be closed in the correct order.
        3. Every close bracket has a corresponding open bracket of the same type.

        Time:  O(n)  — single pass through the string
        Space: O(n)  — stack holds up to n open brackets
        """
        # Stack that tracks unmatched opening brackets
        stack = []

        # Maps each closing bracket to its matching opening bracket
        # This lets us check correctness in O(1) per character
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            # If it's an opening bracket (a *value* in the mapping)
            if char in mapping.values():
                stack.append(char)

            # If it's a closing bracket (a *key* in the mapping)
            elif char in mapping.keys():
                # Valid only if the top of the stack is its matching opening bracket
                if not stack or mapping[char] != stack.pop():
                    return False

        # The string is valid only if all brackets were properly closed
        return not stack


def main():
    """Simple test harness to demonstrate the solution."""
    solution = Solution()

    # Test cases: (input, expected_result)
    test_cases = [
        ("()", True),        # simple nested pair
        ("()[]{}", True),    # multiple pairs
        ("(]", False),       # mismatched types
        ("([)]", False),     # wrong nesting order
        ("{[]}", True),      # properly nested
        ("", True),          # empty string is valid
        ("(", False),        # unclosed bracket
        ("}{", False),       # wrong order
    ]

    for s, expected in test_cases:
        result = solution.isValid(s)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | s={s!r:<10} -> got {result}, expected {expected}")


if __name__ == "__main__":
    main()
