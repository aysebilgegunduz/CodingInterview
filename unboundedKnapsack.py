def solve_knapsack(profits, weights, capacity):
    #dp = [[-1 for i in range(capacity+1)]for j in range(len(profits)]

    #return solve_knapsack_rec(profits, weights, capacity, 0)
    #return solve_knapsack_rec(dp, profits, weights, capacity, 0)
    n = len(profits)
    if capacity <=0 or n ==0 and len(weights) != n:
        return 0
    dp = [[-1 for i in range(capacity+1)]for j in range(len(profits)]
    for i in range(n):
        dp[i][0] = 0
    for i in range(n):
        for j in range(1, capacity+1):
            profits1, profits2 = 0, 0
            if weights[i] <= j:
                profits1 = profits[i] + dp[i][j - weights[i]]
            if i >0:
                profits2 = dp[i-1][j]
            dp[i][j] = max(profits1,profits2)
    return dp[n-1][capacity]

def solve_knapsack_mem(dp, profits, weights, capacity, currentIndex):
    n = len(profits)
    if n==0 or capacity <=0 or len(weights) != n or currentIndex == n):
        return 0

    if dp[currentIndex][capacity] == -1:
        if weights[currentIndex] < capacity:
            total_capacity1 = profits[currentIndex] + solve_knapsack_mem(dp, profits, weights, capacity-weights[currentIndex], currentIndex)

        total_capacity2= solve_knapsack_mem(dp, profits, weights, capacity, currentIndex+1)

        dp[currentIndex][capacity] = max(total_capacity1,total_capacity2)
    return dp[currentIndex][capacity]

def solve_knapsack_rec(profits, weights, capacity, currentIndex):
    n = len(profits)
    if n==0 or capacity <=0 or len(weights) != n or currentIndex == n):
        return 0

    if weights[currentIndex] < capacity:
        total_capacity1 = profits[currentIndex] + solve_knapsack_rec(profits, weights, capacity-weights[currentIndex], currentIndex)

    total_capacity2 = solve_knapsack_rec(profits, weights, capacity, currentIndex+1)

    return max(total_capacity1,total_capacity2)

def main():
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
  print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()
