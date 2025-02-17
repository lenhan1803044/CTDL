def print_binary_numbers(n):
    for i in range(1, n+1):
        print(bin(i)[2:], end=" ")  # Chuyển sang nhị phân và in ra

def solve():
    T = int(input())  # Số bộ test
    for _ in range(T):
        n = int(input())  # Đọc số n cho mỗi test
        print_binary_numbers(n)
        print()  # Dòng trống sau mỗi test

# Chạy chương trình
solve()
