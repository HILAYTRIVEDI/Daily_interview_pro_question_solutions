from collections import Counter


def majority_element(my_list):
    ct = Counter(my_list)
    max_value = max(ct.values())
    return sorted(key for key, value in ct.items() if value == max_value)


print(majority_element([3, 5, 3, 3, 2, 4, 3]))
