def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():  # Nếu là số, đẩy vào stack
            stack.append(int(char))
        else:  # Nếu là toán tử, lấy hai phần tử trên cùng stack
            op2 = stack.pop()
            op1 = stack.pop()
            
            if char == '+':
                stack.append(op1 + op2)
            elif char == '-':
                stack.append(op1 - op2)
            elif char == '*':
                stack.append(op1 * op2)
            elif char == '/':
                stack.append(op1 // op2)  # Chia lấy phần nguyên

    return stack[0]

# Đọc số lượng bộ test
T = int(input().strip())

for _ in range(T):
    expression = input().strip()
    print(evaluate_postfix(expression))
