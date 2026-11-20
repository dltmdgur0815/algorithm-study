def check_brackets(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for index, char in enumerate(text):
        if char in '([{':
            stack.append((char, index))
        elif char in pairs:
            if not stack or stack[-1][0] != pairs[char]:
                return False, index
            stack.pop()
    return (False, stack[-1][1]) if stack else (True, None)
