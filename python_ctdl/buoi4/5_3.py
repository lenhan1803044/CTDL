def process_expression(expression):
    result = []
    sign = 1  # 1 for positive, -1 for negative
    for i, char in enumerate(expression):
        if char == '(':
            # Check if the previous character is '-', which means we invert the signs in the parentheses
            if result and result[-1] == '-':
                sign = -sign  # Flip the sign
            else:
                sign = 1  # Keep the sign as is
        elif char == ')':
            # Reset the sign after closing a parenthesis
            sign = 1
        elif char == '+' or char == '-':
            # Add the sign based on the current sign state
            if sign == -1 and char == '+':
                result.append('-')
            elif sign == -1 and char == '-':
                result.append('+')
            else:
                result.append(char)
        else:
            result.append(char)
    
    return ''.join(result)

# Input handling
T = int(input())

for _ in range(T):
    expression = input().strip()
    print(process_expression(expression))

