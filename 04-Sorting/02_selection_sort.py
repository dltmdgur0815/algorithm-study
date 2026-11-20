def selection_sort(values):
    result = list(values)
    comparisons = 0
    for i in range(len(result) - 1):
        minimum = i
        for j in range(i + 1, len(result)):
            comparisons += 1
            if result[j] < result[minimum]:
                minimum = j
        result[i], result[minimum] = result[minimum], result[i]
    return result, comparisons
