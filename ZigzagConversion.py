class Solution:
    def convert(self, s: str, numRows: int) -> str:

        # If there is only one row,
        # zigzag conversion is unnecessary.
        if numRows == 1:
            return s

        # If number of rows is greater than or equal
        # to string length, no conversion is required.
        if numRows >= len(s):
            return s

        # Current row index
        idx = 0

        # Direction of movement
        # 1  = moving down
        # -1 = moving up
        direction = 1

        # Create an empty list for each row
        rows = [[] for _ in range(numRows)]

        # Process every character
        for char in s:

            # Add character to current row
            rows[idx].append(char)

            # If we reach the first row,
            # change direction to downward.
            if idx == 0:
                direction = 1

            # If we reach the last row,
            # change direction to upward.
            elif idx == numRows - 1:
                direction = -1

            # Move to the next row
            idx += direction

        # Convert every row list into a string
        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        # Join all rows together
        return ''.join(rows)


# Main method
if __name__ == "__main__":

    # Read string
    s = input("Enter string: ")

    # Read number of rows
    numRows = int(input("Enter number of rows: "))

    # Create Solution object
    obj = Solution()

    # Perform zigzag conversion
    result = obj.convert(s, numRows)

    # Display result
    print("Zigzag converted string:", result)
