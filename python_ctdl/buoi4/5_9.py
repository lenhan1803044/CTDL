def postfix_to_prefix(expression):
    stack = []
    
    # Duyệt từ trái sang phải
    for char in expression:
        if char.isalpha():  # Nếu là toán hạng (A-Z)
            stack.append(char)
        else:  # Nếu là toán tử
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = f"{char}{op1}{op2}"
            stack.append(new_expr)

    return stack[0]

# Đọc số lượng bộ test
T = int(input().strip())

for _ in range(T):
    expression = input().strip()
    print(postfix_to_prefix(expression))
