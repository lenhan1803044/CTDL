def normalize_expression(expr):
    stack = [1]  # Stack để lưu dấu hiện tại, 1 là dương, -1 là âm
    result = []
    sign = 1  # Dấu mặc định là dương

    i = 0
    while i < len(expr):
        if expr[i] == '+':  # Dấu `+` không ảnh hưởng, bỏ qua
            i += 1
        elif expr[i] == '-':  # Dấu `-` thì đảo dấu
            sign *= -1
            i += 1
        elif expr[i] == '(':  # Gặp dấu `(` thì lưu dấu hiện tại vào stack
            stack.append(stack[-1] * sign)
            sign = 1  # Reset lại dấu sau khi xử lý ngoặc
            i += 1
        elif expr[i] == ')':  # Gặp dấu `)` thì khôi phục dấu trước đó
            stack.pop()
            i += 1
        else:  # Gặp toán hạng (chữ cái thường)
            if stack[-1] * sign == 1:
                result.append('+' + expr[i])
            else:
                result.append('-' + expr[i])
            sign = 1  # Reset lại dấu sau khi gán cho toán hạng
            i += 1

    return ''.join(result)

# Đọc số lượng bộ test
T = int(input().strip())

for _ in range(T):
    P1 = input().strip()
    P2 = input().strip()

    # Chuẩn hóa hai biểu thức và so sánh
    if normalize_expression(P1) == normalize_expression(P2):
        print("YES")
    else:
        print("NO")
