class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Store the length of the string
        n = len(s)

        # Stores the maximum length found so far
        maxLength = 0

        # Set stores unique characters in the current window
        charSet = set()

        # Left pointer of the sliding window
        left = 0

        # Move the right pointer through the string
        for right in range(n):

            # If the current character is not already present
            if s[right] not in charSet:

                # Add the character to the set
                charSet.add(s[right])

                # Calculate current window length
                currentLength = right - left + 1

                # Update maximum length
                maxLength = max(maxLength, currentLength)

            else:
                # Duplicate character found.
                # Remove characters from the left until
                # the duplicate character is removed.
                while s[right] in charSet:

                    # Remove the leftmost character
                    charSet.remove(s[left])

                    # Move left pointer forward
                    left += 1

                # Now add the current character
                charSet.add(s[right])

        # Return the longest substring length
        return maxLength


# Main method
if __name__ == "__main__":

    # Take input from the user
    s = input("Enter a string: ")

    # Create object of Solution class
    obj = Solution()

    # Call the method
    result = obj.lengthOfLongestSubstring(s)

    # Display result
    print("Length of longest substring:", result)
