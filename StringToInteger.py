class Solution:
    def myAtoi(self, s: str) -> int:

        # 32-bit signed integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Length of the string
        n = len(s)

        # Start from index 0
        i = 0

        # Default sign is positive
        sign = 1

        # Result number
        res = 0

        # ------------------------------------------------
        # STEP 1: Skip leading spaces
        # ------------------------------------------------

        while i < n and s[i] == ' ':
            i += 1

        # If string contains only spaces
        if i == n:
            return 0

        # ------------------------------------------------
        # STEP 2: Check the sign
        # ------------------------------------------------

        if s[i] == '+':
            sign = 1
            i += 1

        elif s[i] == '-':
            sign = -1
            i += 1

        # ------------------------------------------------
        # STEP 3: Read all consecutive digits
        # ------------------------------------------------

        while i < n and s[i].isdigit():

            # Convert character into integer
            digit = int(s[i])

            # Build the number
            res = res * 10 + digit

            # Apply sign temporarily
            current = res * sign

            # ------------------------------------------------
            # STEP 4: Check 32-bit integer overflow
            # ------------------------------------------------

            if current > INT_MAX:
                return INT_MAX

            if current < INT_MIN:
                return INT_MIN

            # Move to next character
            i += 1

        # ------------------------------------------------
        # STEP 5: Return final number
        # ------------------------------------------------

        return res * sign


# Main method
if __name__ == "__main__":

    # Read input string
    s = input("Enter a string: ")

    # Create Solution object
    obj = Solution()

    # Convert string to integer
    result = obj.myAtoi(s)

    # Display result
    print("Converted integer:", result)
