class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0
        
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # Step 1: Skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Check if we've reached the end
        if i == n:
            return 0
        
        # Step 2: Check for sign
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        # Step 3: Read digits and convert
        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res * 10 + digit
            
            if sign * res <= INT_MIN:
                return INT_MIN
            if sign * res >= INT_MAX:
                return INT_MAX
            
            i += 1

        '''
        For "1234":
            res = 0
            '1': res = 0 * 10 + 1 = 1
            '2': res = 1 * 10 + 2 = 12
            '3': res = 12 * 10 + 3 = 123
            '4': res = 123 * 10 + 4 = 1234'''
        
        # Step 4: Apply sign and return
        return res * sign
