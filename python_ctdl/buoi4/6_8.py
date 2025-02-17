# Hàm kiểm tra nếu tất cả các chữ số của số K đều khác nhau và nhỏ hơn hoặc bằng 5
def is_valid(K):
    str_K = str(K)
    seen = set()
    for ch in str_K:
        if ch in seen or int(ch) > 5:  # Nếu chữ số đã xuất hiện hoặc chữ số lớn hơn 5
            return False
        seen.add(ch)
    return True

# Hàm xử lý từng test case
def solve():
    T = int(input())  # Số lượng test cases
    for _ in range(T):
        L, R = map(int, input().split())  # Đọc L và R
        count = 0
        for K in range(L, R + 1):  # Duyệt qua tất cả các số từ L đến R
            if is_valid(K):
                count += 1
        print(count)

# Chạy chương trình
solve()
