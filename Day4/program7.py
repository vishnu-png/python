def countVowelStrings(n):
    dp = [[0] * 5 for _ in range(n)]

    for i in range(5):
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(5):
            dp[i][j] = sum(dp[i - 1][j:])


    return sum(dp[n - 1])

n = 2
print(countVowelStrings(n))  # Output: 15
