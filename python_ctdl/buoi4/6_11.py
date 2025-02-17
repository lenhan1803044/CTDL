from collections import deque

# Các hướng di chuyển trong không gian 3 chiều
directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]

def bfs(A, B, C, grid, start, end):
    queue = deque([(start[0], start[1], start[2], 0)])  # (x, y, z, steps)
    visited = set()
    visited.add(start)
    
    while queue:
        x, y, z, steps = queue.popleft()
        
        # Nếu đã đến điểm đích, trả về số bước
        if (x, y, z) == end:
            return steps
        
        # Duyệt qua tất cả các hướng di chuyển
        for dx, dy, dz in directions:
            nx, ny, nz = x + dx, y + dy, z + dz
            
            # Kiểm tra xem (nx, ny, nz) có hợp lệ không và không phải vật cản
            if 0 <= nx < A and 0 <= ny < B and 0 <= nz < C and grid[nx][ny][nz] != '#' and (nx, ny, nz) not in visited:
                visited.add((nx, ny, nz))
                queue.append((nx, ny, nz, steps + 1))
    
    # Nếu không tìm được đường đi
    return -1

def solve():
    T = int(input())  # Số lượng test cases
    for _ in range(T):
        A, B, C = map(int, input().split())  # Kích thước của hình hộp
        grid = []
        start = None
        end = None
        
        # Đọc các lát cắt của hình hộp
        for i in range(A):
            layer = []
            for j in range(B):
                row = list(input().strip())  # Đảm bảo rằng chúng ta chỉ lấy các kí tự
                if len(row) != C:
                    raise ValueError(f"Lỗi kích thước row tại lát cắt {i}, hàng {j}. Kỳ vọng {C} cột nhưng có {len(row)} cột.")
                for k in range(C):
                    if row[k] == 'S':
                        start = (i, j, k)
                    elif row[k] == 'E':
                        end = (i, j, k)
                layer.append(row)
            grid.append(layer)
            if i < A - 1:
                input()  # Đọc dấu xuống dòng giữa các lát cắt
        
        # Kiểm tra nếu không tìm thấy điểm xuất phát hoặc điểm đích
        if start is None or end is None:
            print(-1)
            continue
        
        # Gọi hàm BFS để tìm đường đi ngắn nhất
        result = bfs(A, B, C, grid, start, end)
        print(result)

# Chạy chương trình
solve()
