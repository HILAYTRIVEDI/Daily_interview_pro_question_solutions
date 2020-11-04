from itertools import chain, combinations


def generateAllSubsets(nums):
    s = list(nums)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


print(list(generateAllSubsets([1, 2, 3])))
# [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
