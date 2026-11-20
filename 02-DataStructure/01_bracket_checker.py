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

def check_code_brackets(text):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    quote = None
    quote_start = None
    escaped = False
    for index, char in enumerate(text):
        if quote is not None:
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char == quote:
                quote = None
            continue
        if char in "\"'":
            quote = char
            quote_start = index
        elif char in '([{':
            stack.append((char, index))
        elif char in pairs:
            if not stack or stack[-1][0] != pairs[char]:
                return False, index
            stack.pop()
    if quote is not None:
        return False, quote_start
    return (False, stack[-1][1]) if stack else (True, None)
