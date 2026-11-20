def linear_search(values, target):
    comparisons = 0
    for index, value in enumerate(values):
        comparisons += 1
        if value == target:
            return index, comparisons
    return -1, comparisons

def binary_search(values, target):
    left, right, comparisons = 0, len(values) - 1, 0
    while left <= right:
        middle = (left + right) // 2
        comparisons += 1
        if values[middle] == target:
            return middle, comparisons
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1, comparisons
