def findKthLargest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]


print(findKthLargest([8, 7, 2, 3, 4, 1, 5, 6, 9, 0], 3))
# 7
# O(1) Complexity
