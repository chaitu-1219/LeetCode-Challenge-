class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers cannot be palindromes
        # Example: -121 != 121-
        if x < 0:
            return False

        # Store the original number
        xcopy = x

        # Variable used to store the reversed number
        reverse = 0

        # Continue until all digits are processed
        while x > 0:

            # Get the last digit
            digit = x % 10

            # Add the digit to the reversed number
            reverse = reverse * 10 + digit

            # Remove the last digit from x
            x //= 10

        # Compare reversed number with original number
        return reverse == xcopy


# Main method
if __name__ == "__main__":

    # Read number from user
    x = int(input("Enter a number: "))

    # Create Solution object
    obj = Solution()

    # Check palindrome
    result = obj.isPalindrome(x)

    # Display result
    print("Is palindrome:", result)
