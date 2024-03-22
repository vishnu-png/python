def isScramble(s1, s2):
    if s1 == s2:
        return True
    if len(s1) != len(s2) or sorted(s1) != sorted(s2):
        return False

    n = len(s1)
    dp = [[[False] * n for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dp[0][i][j] = s1[i] == s2[j]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            for j in range(n - length + 1):
                for k in range(1, length):
                    if (dp[length - k][i][j] and dp[k][i + length - k][j + length - k]) or \
                       (dp[k][i][j + length - k] and dp[length - k][i + k][j]):
                        dp[length][i][j] = True
                        break

    return dp[n][0][0]

s1 = "great"
s2 = "rgeat"
print(isScramble(s1, s2)) 
