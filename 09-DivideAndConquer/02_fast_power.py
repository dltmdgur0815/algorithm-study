def recursive_power(base, exponent):
    if not isinstance(exponent, int) or exponent < 0:
        raise ValueError('exponent must be a nonnegative integer')
    if exponent == 0:
        return 1
    half = recursive_power(base, exponent // 2)
    if exponent % 2 == 0:
        return half * half
    return half * half * base

def iterative_power(base, exponent):
    if not isinstance(exponent, int) or exponent < 0:
        raise ValueError('exponent must be a nonnegative integer')
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result
