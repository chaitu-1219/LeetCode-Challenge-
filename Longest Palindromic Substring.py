class Solution:
    def longestPalindrome(self, s: str) -> str:
        # If the input string length is 1 or less, it is already a palindrome
        if len(s) <= 1:
            return s
        
        Max_Len = 1  # Initialize the maximum length of palindrome found
        Max_Str = s[0]  # Initialize the longest palindrome substring

        # Iterate over each character in the string as a potential center of a palindrome
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                # Check if the substring is longer than the current longest found
                # and if it is a palindrome
                if j - i + 1 > Max_Len and s[i:j + 1] == s[i:j + 1][::-1]:
                    Max_Len = j - i + 1  # Update the maximum length
                    Max_Str = s[i:j + 1]  # Update the longest palindrome substring

        return Max_Str  # Return the longest palindrome found

def main():
    # Create an instance of the Solution class
    solution = Solution()
    
    # Example input string
    input_string = "babad"
    
    # Call the longestPalindrome method and print the result
    result = solution.longestPalindrome(input_string)
    print(f"The longest palindromic substring in '{input_string}' is: '{result}'")

# Entry point of the program
if __name__ == "__main__":
    main()
