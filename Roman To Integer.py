class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0  # Accumulator to hold the running total
        # Lookup table mapping each Roman symbol to its integer value
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Iterate over adjacent pairs of characters in the string.
        # zip(s, s[1:]) yields (s[0],s[1]), (s[1],s[2]), ..., (s[n-2], s[n-1])
        for a, b in zip(s, s[1:]):
            # Rule: if the current symbol is smaller than the NEXT symbol,
            # it should be SUBTRACTED (handles cases like IV, IX, CM...)
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                # Otherwise, add the current symbol's value normally
                res += roman[a]

        # The last character has no "next" symbol to compare against,
        # so it is always added explicitly.
        return res + roman[s[-1]]
