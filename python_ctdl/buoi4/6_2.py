from collections import deque

def find_smallest_multiple(n):
    queue = deque(["9"])  # Bắt đầu với số 9
    while queue:
        num = queue.popleft()  # Lấy số đầu tiên trong hàng đợi
        if int(num) % n == 0:
            return num  # Số chia hết cho n
        queue.append(num + "0")  # Thêm số 0 vào
        queue.append(num + "9")  # Thêm số 9 vào

def solve():
    T = int(input())  # Số bộ test
    for _ in range(T):
        n = int(input())  # Đọc số N
        print(find_smallest_multiple(n))

# Chạy chương trình
solve()
