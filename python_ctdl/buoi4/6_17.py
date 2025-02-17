from collections import deque
# Hàm chuyển đổi từ ký tự cột (a-h) và số hàng (1-8) thành tọa độ (x, y)
def position_to_coordinates(pos):
    column, row = pos[0], pos[1]
    # Cột 'a' -> 0, 'b' -> 1, ..., 'h' -> 7
    # Hàng '1' -> 0, '2' -> 1, ..., '8' -> 7
    return (ord(column) - ord('a'), int(row) - 1)
# Hàm BFS tìm đường đi ít nhất
def bfs(start, end):
    # Các hướng di chuyển của quân mã
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1),
             (1, 2), (1, -2), (-1, 2), (-1, -2)]   
    # Queue cho BFS, lưu trữ (x, y, bước)
    queue = deque([(start[0], start[1], 0)]) 
    # Đánh dấu các ô đã thăm
    visited = [[False] * 8 for _ in range(8)]
    visited[start[0]][start[1]] = True
    while queue:
        x, y, steps = queue.popleft()  
        # Nếu đã đến vị trí đích
        if (x, y) == end:
            return steps 
        # Thử tất cả các hướng di chuyển
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))
    
    return -1
# Hàm giải quyết bài toán
def solve():
    T = int(input())  # Số lượng test cases
    for _ in range(T):
        start, end = input().split()
        start_coords = position_to_coordinates(start)
        end_coords = position_to_coordinates(end)
        
        # Tìm số bước ít nhất từ start đến end
        result = bfs(start_coords, end_coords)
        
        # In kết quả
        print(result)

# Chạy chương trình
solve()
