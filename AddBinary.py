class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # carry starts at 0; it will hold a_digit + b_digit + previous carry
        carry = 0
        # res will collect the result digits (in reverse order for now)
        res = []

        # Start from the rightmost (least significant) digit of each string
        idxA, idxB = len(a) - 1, len(b) - 1

        # Loop while there are still digits in a OR b, OR a carry is left over
        while idxA >= 0 or idxB >= 0 or carry == 1:
            # If a still has a digit at this position, add it to the carry
            if idxA >= 0:
                carry += int(a[idxA])  # convert char to int and add
                idxA -= 1              # move left
            # If b still has a digit at this position, add it to the carry
            if idxB >= 0:
                carry += int(b[idxB])  # convert char to int and add
                idxB -= 1              # move left

            # carry % 2 gives the digit to write (0 if sum is even, 1 if odd)
            res.append(str(carry % 2))
            # carry // 2 gives the new carry for the next more-significant column
            carry = carry // 2

        # res was built right-to-left, so reverse it and join into a string
        return "".join(res[::-1])


def main():
    solution = Solution()
    test_cases = [
        ("11", "1"),        # 3 + 1 = 4 -> "100"
        ("1010", "1011"),   # 10 + 11 = 21 -> "10101"
        ("0", "0"),         # 0 + 0 = 0 -> "0"
        ("1", "1"),         # 1 + 1 = 2 -> "10"
        ("1", "0"),         # 1 + 0 = 1 -> "1"
        ("111", "111"),     # 7 + 7 = 14 -> "1110"
        ("101010", "110011"),  # larger case
    ]

    print("Running addBinary test cases:\n")
    all_passed = True
    for i, (a, b) in enumerate(test_cases, 1):
        result = solution.addBinary(a, b)
        expected = bin(int(a, 2) + int(b, 2))[2:]  # verify with Python's built-in
        passed = result == expected
        all_passed = all_passed and passed
        status = "PASS" if passed else "FAIL"
        print(f"Test {i}: addBinary('{a}', '{b}') = '{result}' "
              f"(expected '{expected}') -> {status}")

    print("\nAll tests passed!" if all_passed else "\nSome tests failed!")


if __name__ == "__main__":
    main()
