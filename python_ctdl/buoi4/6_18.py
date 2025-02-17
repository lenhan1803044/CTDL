from collections import deque

# Hàm quay miếng ghép theo chiều kim đồng hồ (chuyển vị trí)
def rotate(state, index):
    state = list(state)
    # Quay theo chiều kim đồng hồ 90 độ (có thể quay miếng ghép tại vị trí index)
    if index == 0:
        state[0], state[1], state[2], state[3] = state[3], state[0], state[1], state[2]
    elif index == 1:
        state[3], state[4], state[5], state[0] = state[0], state[3], state[4], state[5]
    return tuple(state)

def bfs(start, target):
    if start == target:
        return 0

    # Đoạn queue lưu trữ trạng thái và số bước
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    while queue:
        current_state, steps = queue.popleft()
        # Tiến hành các phép quay
        for i in range(6):
            next_state = rotate(current_state, i)
            if next_state == target:
                return steps + 1
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + 1))

    return -1
def solve():
    T = int(input())  # Số bộ test
    for _ in range(T):
        # Đọc trạng thái ban đầu và đích
        start = tuple(map(int, input().split()))
        target = tuple(map(int, input().split()))
        
        # Tìm số phép biến đổi ít nhất từ start đến target
        result = bfs(start, target)
        print(result)

# Chạy chương trình
solve()
