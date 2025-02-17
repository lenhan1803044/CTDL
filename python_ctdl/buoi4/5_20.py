def decode_string(s):
    stack = []
    num = 0
    current_str = ""
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)  # Xử lý nhiều chữ số
        elif char == '[':
            # Lưu lại số lần lặp và xâu con hiện tại
            stack.append((num, current_str))
            num = 0
            current_str = ""
        elif char == ']':
            # Giải mã xâu con trong ngoặc vuông
            prev_num, prev_str = stack.pop()
            current_str = prev_str + current_str * prev_num
        else:
            current_str += char  # Thêm ký tự vào xâu hiện tại
            
    return current_str

def solve():
    T = int(input())  # Số bộ test
    for _ in range(T):
        s = input().strip()  # Xâu mã hóa
        result = decode_string(s)
        print(result)

# Chạy chương trình
solve()
