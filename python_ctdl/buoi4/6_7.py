from collections import deque
# Hàm kiểm tra xem hai xâu có khác nhau đúng một ký tự không
def is_one_letter_diff(s1, s2):
    diff_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            diff_count += 1
        if diff_count > 1:
            return False
    return diff_count == 1
# Hàm tìm đường đi ngắn nhất bằng BFS
def bfs(start, target, words):
    queue = deque([(start, 0)])  # Lưu trữ (xâu hiện tại, bước đi)
    visited = set([start])  # Đánh dấu các xâu đã thăm
    
    while queue:
        current, steps = queue.popleft()
        
        # Nếu tìm thấy xâu target, trả về số bước
        if current == target:
            return steps
        
        # Duyệt qua tất cả các xâu trong từ điển
        for word in words:
            if word not in visited and is_one_letter_diff(current, word):
                visited.add(word)
                queue.append((word, steps + 1))
    return -1  # Nếu không tìm thấy, trả về -1 (không có đường đi)
# Hàm xử lý từng test case
def solve():
    T = int(input())  # Số lượng test cases
    for _ in range(T):
        # Đọc n, s, t
        n, s, t = input().split()
        n = int(n)
        
        # Đọc danh sách các xâu trong từ điển S
        words = set(input().split())
        
        # Tìm số bước đi ngắn nhất từ s đến t
        result = bfs(s, t, words)
        print(result)

# Chạy chương trình
solve()

