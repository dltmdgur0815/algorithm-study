def insertion_sort(values, key=lambda value: value, reverse=False):
    result = list(values)
    for i in range(1, len(result)):
        current = result[i]
        current_key = key(current)
        j = i - 1
        while j >= 0:
            previous_key = key(result[j])
            if reverse:
                move = previous_key < current_key
            else:
                move = previous_key > current_key
            if not move:
                break
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current
    return result
