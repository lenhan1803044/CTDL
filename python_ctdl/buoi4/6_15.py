from collections import deque
# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Hàm tạo danh sách tất cả các số nguyên tố 4 chữ số
def generate_primes():
    primes = []
    for num in range(1000, 10000):
        if is_prime(num):
            primes.append(str(num))
    return primes
# Hàm BFS tìm đường đi ngắn nhất
def bfs(S, T, primes_set):
    # BFS với queue lưu trữ (số hiện tại, số bước)
    queue = deque([(S, 0)])  # bắt đầu từ số S với 0 bước
    visited = set([S])  # dấu các số đã được thăm
    while queue:
        current, steps = queue.popleft()
        # Nếu đã đến được đích, trả về số bước
        if current == T:
            return steps       
        # Thử thay đổi từng chữ số của current
        for i in range(4):
            for digit in "0123456789":
                # Nếu chữ số thay đổi không giống chữ số cũ, ta thử
                if digit != current[i]:
                    new_number = current[:i] + digit + current[i+1:]
                    if new_number in primes_set and new_number not in visited:
                        visited.add(new_number)
                        queue.append((new_number, steps + 1))
    return -1  # Nếu không thể tìm được đường đi
# Hàm giải quyết bài toán
def solve():
    primes_set = set(generate_primes())  # Tạo danh sách các số nguyên tố 4 chữ số
    T = int(input())  # Số lượng test case
    for _ in range(T):
        S, T = input().split()  # Đọc cặp số S và T
        result = bfs(S, T, primes_set)  # Tìm đường đi ngắn nhất từ S đến T
        print(result)
# Chạy chương trình
solve()
