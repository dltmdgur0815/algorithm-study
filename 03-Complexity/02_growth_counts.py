def count_operations(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be a nonnegative integer')
    linear = pairs = 0
    for _ in range(n):
        linear += 1
    for i in range(n):
        for _ in range(i + 1, n):
            pairs += 1
    return linear, pairs
