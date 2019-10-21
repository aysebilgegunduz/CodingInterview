def find_target_subsets(num, s):
    total_sum = sum(num)
    if total_sum<s and (s+total_sum)%2 == 1:
        return 0

    count_subsets(num, int((s+total_sum)/2))

def count_subsets(num, s):
    n = len(num)
    dp = [[0 for i in range(0, s+1)]for j in range(n)]

    for i in range(0,n):
        dp[i][0] = 1
    for i in range(0, s+1):
        dp[0][i] = if num[0] == i

    for i in range(1, n):
        for j in range(1, s+1):
            dp[i][j] = dp[i-1][j]
            if j >= num[i]:
                dp[i][j] = dp[i-1][j-num[i]]
    return dp[n-1][s]
##### Optimized Count_Subest ######

def count_subsets_o(num,s):
    n = len(num)
    dp[0 for i in range(0,s+1)]
    dp[0]=1
    for i in range(0, s+1):
        dp[i] = 1 if num[0] == i
    for i in range(1, n):
        for j in range(1, s+1):
            if j >= num[i]:
                dp[j] = dp[j-num[i]]
    return dp[s]


def main():
  print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
  print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
