def solve(S):
    # Dãy số cần sắp xếp
    stack = []
    result = []
    
    # Duyệt qua từng ký tự trong chuỗi S
    for i in range(len(S) + 1):
        # Đẩy số vào stack
        stack.append(i + 1)
        
        # Nếu gặp ký tự 'I' hoặc hết dãy, xử lý stack
        if i == len(S) or S[i] == 'I':
            while stack:
                result.append(str(stack.pop()))
    
    # Trả về kết quả là chuỗi số nối lại
    return ''.join(result)

# Đọc số lượng bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    S = input().strip()
    print(solve(S))
