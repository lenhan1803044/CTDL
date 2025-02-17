def max_valid_length(P):
    stack = [-1]  # Đặt một chỉ số giả -1 vào stack để dễ tính toán
    total_length = 0
    for i, char in enumerate(P):
        if char == '(':
            stack.append(i)  # Đẩy chỉ số dấu mở ngoặc vào stack
        elif char == ')':
            stack.pop()  # Pop dấu ngoặc mở cuối cùng
            if stack:
                length = i - stack[-1]  # Tính độ dài biểu thức đúng
                total_length += length
            stack.append(i)  # Đẩy lại chỉ số dấu đóng ngoặc vào stack
    
    return total_length

def solve():
    T = int(input())  # Số bộ test
    for _ in range(T):
        P = input().strip()  # Biểu thức
        result = max_valid_length(P)
        print(result)

# Chạy chương trình
solve()
