from typing import List

def kSumSubset(numArray: List[int], k: int) -> bool:
    # write your code here ^_^
    dp = [False for _ in range(k + 1)]
    dp[0] = True
    for num in numArray:
        for j in range(k, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
    return dp[k]

# Test the function
numArray = [1, 3, 7, 5]
k = 7
print(kSumSubset(numArray, k))  # Output should be True
