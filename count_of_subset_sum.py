def count_subsets(num, sum):
  dp = [[-1 for i in range(sum+1)]for j in range(len(num))]
  return count_subsets_recursive(num, sum, 0)
  return count_subset_topD(dp, num, sum, 0)


##Recursive solution
def count_subsets_recursive(num, sum, currentIndex):
  # base checks
  if sum == 0:
    return 1
  n = len(num)
  if n == 0 or currentIndex >= n:
    return 0
  sum1 = 0
  if num[currentIndex] <=sum:
      sum1 = count_subsets_recursive(num, sum-num[currentIndex], currentIndex+1)
  sum2 = count_subsets_recursive(num, sum, currentIndex+1)

  return sum1+sum2

#### Top-Down solution
def count_subset_topD(dp, num, sum, currentIndex):
  if sum == 0:
    return 1
  n = len(num)
  if n==0 or currentIndex>=n:
    return 0
  if dp[currentIndex][sum] == -1:
    sum1 = 0
    if num[currentIndex] <= sum:
      sum1 = count_subset_topD(dp, num, sum - num[currentIndex], currentIndex+1)
    sum2 = count_subset_topD(dp, num, sum, currentIndex+1)
  dp[currentIndex][sum] = sum1+sum2
  return dp[currentIndex][sum]

  ### Bottom-up solution
  def count_subsets(num, sum):
    dp = [[0 for i in range(sum+1)]for j in range(len(num))]
    n = len(num)
    for i in range(0,n):
      dp[i][0] = 1
    for i in range(0, sum+1):
      dp[0][i] = 1 if num[0] == i

    for i in range(1, n):
      for j in range(1, sum+1):
        dp[i][j] = dp[i-1][j]
        if j>=num[i]:
          dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
      return dp[n-1][sum]
  ####

  #### Challenged Bottom-up solution
  def count_subsets(num, sum):
  n = len(num)
  dp = [0 for i in range(sum+1)]
  dp[0] = 1
  for i in range(1, sum+1):
    dp[i] = 1 if num[0] == i else 0
  for i in range(1, n):
    for j in range(sum,0,-1):
      if j >= num[i]:
        dp[j] = dp[j] + dp[j-num[i]]
return dp[sum]
  ####

def main():
  print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
  print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
