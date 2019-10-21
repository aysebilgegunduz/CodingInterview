"""
The problem is from educative.io -
Grokking Dynamic Programming Patterns for Coding Interviews Course
Given an infinite supply of ‘n’ coin denominations
and a total money amount, we are asked to find the minimum number
of coins needed to make up that amount.

Denominations: {1,2,3}
Total amount: 11
Output: 4
Explanation: We need minimum four coins {2,3,3,3} to make a total of '11'
Problem Statement
Given a number array to represent different coin denominations
and a total amount ‘T’, we need to find the minimum number of
coins needed to make change for ‘T’. We can assume an infinite
supply of coins, therefore, each coin can be chosen multiple times.
"""
import math

def count_change(denominations, total):
    #dp = [[-1 for _ in range(total+1)] for _ in range(len(denominations))]
    #------recursive solution--------#
    #result = count_change_recursive(denominations, total, 0)

    #------Top-down memoisation solution--------#
    #result = count_change_memo(dp, denominations,total,0)
    #return -1 if result == math.inf else result
    #-------Bottom-up solution----------#
    """time and space complexity of O(C*T)O(C∗T), where ‘C’
    represents total coin denominations and ‘T’ is the total amount that we want to make change."""
    dp = [[math.inf for _ in range(total+1)] for _ in range(len(denominations))]
    n = len(denominations)
    # populate the total=0 columns, as we don't need any coin to make zero total
    for i in range(n):
        dp[i][0] = 0
    for i in range(n):
        for j in range(1, total+1):
            if i>0:
                dp[i][t] = dp[i-1][j]
            if j >= denominations[i]:
                 if dp[i][j - denominations[i]] != math.inf:
                     dp[i][j] = min(dp[i][j], dp[i][j-denominations[i]]+1)
    return -1 if dp[n-1][total] == math.inf else dp[n-1][total]


def count_change_memo(dp, denominations, total, currentIndex):
    #base check
    if total == 0:
        return 0
    n = len(denominations)
    if n == 0 or currentIndex >= n:
        return math.inf
    #check if we already processed the subproblem
    if dp[currentIndex][total] == -1:
        count1 = math.inf
        if denominations[currentIndex] <= total:
            res = count_change_memo(dp, denominations, total-denominations[currentIndex], currentIndex)
            if res!= math.inf:
                count1 = res+1
        count2 = count_change_memo(dp, denominations, total, currentIndex+1)
        dp[currentIndex][total] = min(count1,count2)
    return dp[currentIndex][total]
def count_change_recursive(denominations, total, currentIndex):
    #base check
    if total == 0:
        return 0

    n = len(denominations)
    if n == 0 or currentIndex >= n:
        return math.inf

    count1 = math.inf
    if denominations[currentIndex] <= total:
        res = count_change_recursive(denominations, total-denominations[currentIndex], currentIndex)
        if res !=math.inf:
            count1 = res+1
    count2 = count_change_recursive(denominations, total, currentIndex+1)
    return min(count1, count2)

def main():
  print(count_change([1, 2, 3], 5))
  print(count_change([1, 2, 3], 11))
  print(count_change([1, 2, 3], 7))
  print(count_change([3, 5], 7))


main()
