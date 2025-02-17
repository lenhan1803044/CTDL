from collections import deque

# Hàm BFS để tìm số bước ít nhất từ (a, b) đến (c, d)
def bfs(N, grid, start, end):
    # Mảng di chuyển: 4 hướng (trái, phải, lên, xuống)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Tạo một mảng để lưu thông tin đã thăm
    visited = [[False] * N for _ in range(N)]
    
    # Queue để duyệt BFS (lưu trữ (x, y, steps))
    queue = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    while queue:
        x, y, steps = queue.popleft()
        # Nếu đã đến đích, trả về số bước
        if (x, y) == end:
            return steps
        # Duyệt qua tất cả 4 hướng
        for dx, dy in directions:
            nx, ny = x, y
            # Tiến hành di chuyển theo hướng (dx, dy) cho tới khi gặp vật cản
            while 0 <= nx + dx < N and 0 <= ny + dy < N and grid[nx + dx][ny + dy] == '.':
                nx += dx
                ny += dy
                # Nếu chưa thăm ô này thì thêm vào queue
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, steps + 1))
    return -1  # Trường hợp không thể đến đích (không tồn tại đường đi)

# Hàm xử lý các test case
def solve():
    T = int(input())  # Số lượng test cases
    for _ in range(T):
        N = int(input())  # Kích thước bảng N x N
        grid = [input().strip() for _ in range(N)]  # Bảng
        a, b, c, d = map(int, input().split())  # Tọa độ điểm xuất phát (a, b) và đích (c, d)
        
        # Tìm số bước ít nhất từ (a, b) đến (c, d)
        result = bfs(N, grid, (a, b), (c, d))
        print(result)

# Chạy chương trình
solve()
