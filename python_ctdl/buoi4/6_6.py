import math

def min_operations(N):
    steps = 0
    while N > 1:
        # Kiểm tra nếu N có ước số ngoài 1 và chính nó
        found = False
        for i in range(2, int(math.sqrt(N)) + 1):
            if N % i == 0:
                N = max(i, N // i)  # Áp dụng thao tác (b)
                steps += 1
                found = True
                break
        if not found:  # Nếu không tìm được ước, dùng thao tác (a)
            N -= 1
            steps += 1
    return steps

def solve():
    T = int(input())  # Số lượng test case
    for _ in range(T):
        N = int(input())  # Đọc số N cho mỗi test
        print(min_operations(N))  # In ra kết quả cho mỗi test

# Chạy chương trình
solve()
