def prefix_to_infix(expression):
    stack = []
    
    # Duyệt từ phải sang trái
    for char in reversed(expression):
        if char.isalpha():  # Nếu là toán hạng (A-Z)
            stack.append(char)
        else:  # Nếu là toán tử
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = f"({op1}{char}{op2})"
            stack.append(new_expr)

    return stack[0]

# Đọc số lượng bộ test
T = int(input().strip())

for _ in range(T):
    expression = input().strip()
    print(prefix_to_infix(expression))
