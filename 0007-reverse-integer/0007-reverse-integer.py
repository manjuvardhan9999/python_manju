class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        rev = 0
        while x != 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit
        
        rev *= sign
        
        # 32-bit signed integer range check
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        
        return rev

