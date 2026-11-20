def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(values):
    if len(values) <= 1:
        return list(values)
    middle = len(values) // 2
    left = merge_sort(values[:middle])
    right = merge_sort(values[middle:])
    return merge(left, right)

def count_inversions(values):
    if len(values) <= 1:
        return list(values), 0
    middle = len(values) // 2
    left, left_count = count_inversions(values[:middle])
    right, right_count = count_inversions(values[middle:])
    result = []
    count = left_count + right_count
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += len(left) - i
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result, count
