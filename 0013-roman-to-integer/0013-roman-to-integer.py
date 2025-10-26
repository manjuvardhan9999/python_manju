class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Traverse from right to left
        for char in reversed(s):
            value = roman[char]
            
            # If a smaller value comes before a larger one, subtract it
            if value < prev_value:
                total -= value
            else:
                total += value
            
            prev_value = value
        
        return total
