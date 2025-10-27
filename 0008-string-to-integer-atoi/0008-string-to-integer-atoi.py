class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0

        # Step 2: Check for optional sign
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        # Step 3: Convert digits to integer
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            else:
                break  # Stop reading at the first non-digit character

        # Apply sign
        num *= sign

        # Step 4: Clamp to 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num
