# Định nghĩa độ ưu tiên của toán tử
def precedence(op):
    if op == '^':
        return 3
    if op in "*/":
        return 2
    if op in "+-":
        return 1
    return 0

# Hàm chuyển đổi trung tố -> hậu tố
def infix_to_postfix(expression):
    stack = []  # Stack lưu toán tử
    output = []  # Kết quả đầu ra

    for char in expression:
        if char.isalpha():  # Nếu là toán hạng (A-Z)
            output.append(char)
        elif char == '(':  # Nếu là dấu mở ngoặc
            stack.append(char)
        elif char == ')':  # Nếu là dấu đóng ngoặc
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Loại bỏ '(' khỏi stack
        else:  # Nếu là toán tử
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)

    # Đưa các toán tử còn lại trong stack vào kết quả
    while stack:
        output.append(stack.pop())

    return "".join(output)

# Đọc số lượng bộ test
T = int(input().strip())

for _ in range(T):
    expression = input().strip()
    print(infix_to_postfix(expression))
