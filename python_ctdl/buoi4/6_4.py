def is_BDN(x):
    # Hàm kiểm tra xem số x có phải là số BDN không
    return all(c in '01' for c in str(x))

def find_BDN_of_N(N):
    # Sinh các số BDN từ nhỏ đến lớn và kiểm tra
    M = 1
    while True:
        P = M * N
        if is_BDN(P):
            return P
        M += 1

def solve():
    T = int(input())  # Số bộ test
    for _ in range(T):
        N = int(input())  # Đọc số N
        print(find_BDN_of_N(N))  # In ra số BDN nhỏ nhất của N

# Chạy chương trình
solve()
