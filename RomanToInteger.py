class Solution:
    def romanToInt(self, s: str) -> int:

        # Dictionary containing Roman numeral values
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Store the final result
        res = 0

        # Go through each character except the last one
        for i in range(len(s) - 1):

            # Get current Roman numeral value
            current = roman[s[i]]

            # Get next Roman numeral value
            next_value = roman[s[i + 1]]

            # If current value is smaller than next value,
            # subtract the current value
            if current < next_value:
                res -= current

            # Otherwise add the current value
            else:
                res += current

        # The last character is always added
        res += roman[s[-1]]

        # Return final integer
        return res


# Main method
if __name__ == "__main__":

    # Read Roman numeral
    s = input("Enter Roman numeral: ").upper()

    # Create Solution object
    obj = Solution()

    # Convert Roman numeral to integer
    result = obj.romanToInt(s)

    # Display result
    print("Integer value:", result)
