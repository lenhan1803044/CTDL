def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def apply_operator(operands, operator):
    right = operands.pop()
    left = operands.pop()
    if operator == '+':
        operands.append(left + right)
    elif operator == '-':
        operands.append(left - right)
    elif operator == '*':
        operands.append(left * right)
    elif operator == '/':
        operands.append(left // right)

def evaluate_expression(expression):
    operands = []  # stack for numbers
    operators = []  # stack for operators
    
    i = 0
    while i < len(expression):
        char = expression[i]
        
        if char.isdigit():  # If the character is a number
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            operands.append(num)
            continue
        
        elif char == ' ':
            i += 1
            continue
        
        elif char == '(':  # If the character is '('
            operators.append(char)
        
        elif char == ')':  # If the character is ')'
            while operators and operators[-1] != '(':
                apply_operator(operands, operators.pop())
            operators.pop()  # pop '('
        
        else:  # If the character is an operator
            while (operators and precedence(operators[-1]) >= precedence(char)):
                apply_operator(operands, operators.pop())
            operators.append(char)
        
        i += 1
    
    while operators:  # Apply remaining operators
        apply_operator(operands, operators.pop())
    
    return operands[0]

# Đọc số lượng bộ test
T = int(input().strip())

for _ in range(T):
    expression = input().strip()
    print(evaluate_expression(expression))
