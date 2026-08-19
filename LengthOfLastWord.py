class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        Returns the length of the last word in the given string.
        A word is a sequence of non-space characters.
        """
        # 1. Start 'end' at the last character of the string
        end = len(s) - 1

        # 2. Skip any trailing spaces so 'end' lands on the
        #    last letter of the last word (e.g. "Hello World   ")
        while s[end] == " ":
            end -= 1

        # 3. Copy 'end' into 'start' so we can walk backwards
        start = end

        # 4. Move 'start' leftward through all consecutive
        #    non-space characters (the letters of the last word).
        #    It stops when it hits a space OR runs off the
        #    beginning of the string (start becomes -1).
        while start >= 0 and s[start] != " ":
            start -= 1

        # 5. 'start' now sits one index before the word's first
        #    letter, so 'end - start' gives the word's length.
        #    e.g. end=18, start=13  ->  18 - 13 = 4  ("moon")
        return end - start


def main():
    """Test the lengthOfLastWord method with several cases."""
    solution = Solution()

    # Test case 1: normal sentence with no trailing spaces
    s1 = "Hello World"
    print(f"Input:  '{s1}'")
    print(f"Output: {solution.lengthOfLastWord(s1)}")  # Expected: 5 (World)
    print()

    # Test case 2: sentence with trailing spaces
    s2 = "   fly me to the moon  "
    print(f"Input:  '{s2}'")
    print(f"Output: {solution.lengthOfLastWord(s2)}")  # Expected: 4 (moon)
    print()

    # Test case 3: single word, no spaces at all
    s3 = "luffy"
    print(f"Input:  '{s3}'")
    print(f"Output: {solution.lengthOfLastWord(s3)}")  # Expected: 5 (luffy)
    print()

    # Test case 4: single word with leading and trailing spaces
    s4 = "   hello   "
    print(f"Input:  '{s4}'")
    print(f"Output: {solution.lengthOfLastWord(s4)}")  # Expected: 5 (hello)


# Standard Python entry point that runs when the script is executed
if __name__ == "__main__":
    main() 
