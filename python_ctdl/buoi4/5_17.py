def longest_valid_parentheses(s):
    stack = [-1]  # Khởi tạo stack với giá trị -1 giúp tính toán chiều dài
    max_len = 0  # Biến lưu chiều dài dãy ngoặc đúng dài nhất
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)  # Lưu chỉ số của '(' vào stack
        else:
            stack.pop()  # Pop dấu '(' ra khỏi stack
            if not stack:
                stack.append(i)  # Nếu stack rỗng, push chỉ số của ')'
            else:
                max_len = max(max_len, i - stack[-1])  # Tính chiều dài dãy ngoặc đúng
    return max_len

def solve():
    T = int(input())  # Đọc số lượng bộ test
    for _ in range(T):
        s = input().strip()  # Đọc xâu S
        print(longest_valid_parentheses(s))  # In kết quả cho mỗi bộ test

# Chạy chương trình
solve()
