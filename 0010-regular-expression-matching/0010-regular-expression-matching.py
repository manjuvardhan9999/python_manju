class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # dp[i][j] means: does s[:i] match p[:j]
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Empty string matches empty pattern
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c* at the start
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    # Current chars match → take the diagonal
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # Two possibilities:
                    # 1. Treat '*' as zero occurrences → dp[i][j-2]
                    # 2. Treat '*' as one or more occurrences → dp[i-1][j] if preceding matches
                    dp[i][j] = dp[i][j - 2] or (
                        dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.')
                    )

        return dp[m][n]
