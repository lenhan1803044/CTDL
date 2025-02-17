import re

# Hàm kiểm tra nếu biểu thức hợp lệ
def is_valid_expression(expr):
    try:
        eval(expr)
        return True
    except:
        return False

# Hàm sinh các biểu thức bằng cách xóa ngoặc
def generate_expressions(expr):
    expressions = set()  # Dùng set để tránh trùng lặp
    
    # Duyệt qua biểu thức và tìm cặp ngoặc
    stack = []
    for i, c in enumerate(expr):
        if c == '(':
            stack.append(i)
        elif c == ')':
            open_index = stack.pop()
            # Tạo các biểu thức mới bằng cách loại bỏ ngoặc
            new_expr = expr[:open_index] + expr[open_index + 1:i] + expr[i + 1:]
            if is_valid_expression(new_expr):
                expressions.add(new_expr)
    
    return expressions

# Nhập biểu thức từ người dùng
expr = input().strip()

# Tạo các biểu thức hợp lệ và sắp xếp theo thứ tự từ điển
valid_expressions = generate_expressions(expr)

# In ra tất cả các biểu thức hợp lệ theo thứ tự từ điển
for expr in sorted(valid_expressions):
    print(expr)
