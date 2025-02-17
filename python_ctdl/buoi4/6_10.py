from collections import deque

# Hàm BFS để tìm số ngày ít nhất để tất cả hạt nảy mầm
def bfs(R, C, grid):
    queue = deque()
    # Khởi tạo queue với các cây non và đánh dấu chúng đã được xử lý
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 2:
                queue.append((i, j, 0))  # (x, y, ngày)
    
    # Mảng di chuyển (trái, phải, trên, dưới)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Thực hiện BFS
    max_days = 0  # Lưu số ngày tối đa
    while queue:
        x, y, days = queue.popleft()
        
        # Duyệt qua tất cả các hướng
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # Kiểm tra xem vị trí (nx, ny) có hợp lệ và là hạt mầm chưa nảy mầm
            if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == 1:
                grid[nx][ny] = 2  # Đánh dấu hạt đã nảy mầm
                queue.append((nx, ny, days + 1))
                max_days = max(max_days, days + 1)
    
    # Kiểm tra xem có còn hạt mầm nào chưa nảy mầm không
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                return -1  # Nếu có hạt chưa nảy mầm, trả về -1
    
    return max_days

# Hàm xử lý các test case
def solve():
    T = int(input())  # Số lượng test cases
    for _ in range(T):
        R, C = map(int, input().split())  # Kích thước bảng R x C
        grid = [list(map(int, input().split())) for _ in range(R)]  # Bảng
        result = bfs(R, C, grid)  # Tính số ngày ít nhất
        print(result)

# Chạy chương trình
solve()
