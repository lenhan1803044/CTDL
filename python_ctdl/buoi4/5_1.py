def has_redundant_parentheses(expression):
    stack = []
    for ch in expression:
        if ch == ')':
            top = stack.pop()
            has_operator = False
            while top != '(':
                if top in '+-*/':
                    has_operator = True
                top = stack.pop()
            if not has_operator:
                return "Yes"  # Dư thừa
        else:
            stack.append(ch)
    return "No"  # Không dư thừa

# Đọc số lượng bộ test
T = int(input())
for _ in range(T):
    expression = input().strip()
    print(has_redundant_parentheses(expression))