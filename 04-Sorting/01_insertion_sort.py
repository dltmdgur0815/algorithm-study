def insertion_sort(values, key=lambda value: value):
    result = list(values)
    for i in range(1, len(result)):
        current = result[i]
        current_key = key(current)
        j = i - 1
        while j >= 0 and key(result[j]) > current_key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result
