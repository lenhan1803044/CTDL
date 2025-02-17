def min_operations(S, T):
    steps = 0
    while T > S:
        if T % 2 == 0:
            T //= 2  # Nếu T là chẵn, chia T cho 2 (ngược với thao tác (b))
        else:
            T += 1  # Nếu T là lẻ, cộng 1 (ngược với thao tác (a))
        steps += 1

    # Sau khi T <= S, ta chỉ cần dùng các thao tác (a) để trừ S đến T
    steps += S - T  # Từ T giảm xuống S bằng các thao tác (a)

    return steps

def solve():
    T = int(input())  # Số bộ test
    for _ in range(T):
        S, T = map(int, input().split())  # Đọc S và T cho mỗi test
        print(min_operations(S, T))  # In ra số bước tối thiểu

# Chạy chương trình
solve()
