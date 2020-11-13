def maxNonAdjacentSum(nums):
    maxsum = 0
    for i in range(0, len(nums)):
        for j in range(i+2, len(nums)):
            if(maxsum < nums[i]+nums[j]):
                maxsum = nums[i]+nums[j]
    return maxsum


print(maxNonAdjacentSum([3, 4, 1, 1]))
# 5
# max sum is 4 (index 1) + 1 (index 3)

print(maxNonAdjacentSum([2, 1, 2, 7, 3]))
# 9
# max sum is 2 (index 0) + 7 (index 3)
