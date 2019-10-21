def solve_rodCut(prices, lengths, capacity):
  lengthCount = len(lengths)
  n = capacity
  # base checks
  if n <= 0 or lengthCount == 0 or len(prices) != lengthCount:
    return 0

  dp = [[-1 for _ in range(n+1)] for _ in range(lengthCount)]

  # process all rod lengths for all prices
  for i in range(lengthCount):
    for length in range(n+1):
      p1, p2 = 0, 0
      if lengths[i] <= length:
        p1 = prices[i] + dp[i][length - lengths[i]]
      if i > 0:
        p2 = dp[i - 1][length]
      dp[i][length] = max(p1, p2)

  # maximum price will be at the bottom-right corner.
  return dp[lengthCount - 1][n]
    # dp = [[-1 for _ in range(capacity+1)] for _ in range(len(lengths))]
    # return solve_rodCut_mem(dp, prices, lengths, capacity, 0)
    #return solve_rodCut_rec(prices, lengths, capacity, 0)

def solve_rodCut_mem(dp, prices, lengths, capacity, currentIndex):
    n = len(prices)
    total_capacity1=0
    total_capacity2 = 0
    if (n==0 or capacity <=0 or len(lengths) != n or currentIndex == n):
        return 0

    if dp[currentIndex][capacity] == -1:
        if lengths[currentIndex] <= capacity:
            total_capacity1 = prices[currentIndex] + solve_rodCut_mem(dp, prices, lengths, capacity-lengths[currentIndex], currentIndex)

        total_capacity2= solve_rodCut_mem(dp, prices, lengths, capacity, currentIndex+1)

        dp[currentIndex][capacity] = max(total_capacity1,total_capacity2)
    return dp[currentIndex][capacity]

def solve_rodCut_rec(prices, lengths, capacity, currentIndex):
    n = len(prices)
    total_capacity1=0
    total_capacity2 = 0
    if (n==0 or capacity <=0 or len(lengths) != n or currentIndex == n):
        return 0

    if lengths[currentIndex] <= capacity:
        total_capacity1 = prices[currentIndex] + solve_rodCut_rec(prices, lengths, capacity-lengths[currentIndex], currentIndex)

    total_capacity2 = solve_rodCut_rec(prices, lengths, capacity, currentIndex+1)

    return max(total_capacity1,total_capacity2)

def main():
  print(solve_rodCut([2, 6, 7, 10, 13], [1, 2, 3, 4, 5], 5))


main()
