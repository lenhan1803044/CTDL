from collections import deque
# Hàm BFS tìm đường đi ngắn nhất
def bfs(M, N, A):
    # Các phép di chuyển có thể có
    directions = [(0, 1), (1, 0)]  # Di chuyển ngang hoặc dọc
    # Khởi tạo một ma trận visited để đánh dấu các ô đã được thăm
    visited = [[False] * N for _ in range(M)]
    # Queue lưu trữ các vị trí và số bước (x, y, bước)
    queue = deque([(0, 0, 0)])  # Bắt đầu từ (0, 0) với 0 bước
    visited[0][0] = True  
    while queue:
        x, y, steps = queue.popleft()    
        # Nếu đã đến (M-1, N-1), tức là A[M][N], trả về số bước
        if x == M - 1 and y == N - 1:
            return steps 
        # Di chuyển đến các vị trí mới
        # 1. Di chuyển sang phải
        if y + A[x][y] < N and not visited[x][y + A[x][y]]:
            visited[x][y + A[x][y]] = True
            queue.append((x, y + A[x][y], steps + 1))   
        # 2. Di chuyển xuống dưới
        if x + A[x][y] < M and not visited[x + A[x][y]][y]:
            visited[x + A[x][y]][y] = True
            queue.append((x + A[x][y], y, steps + 1))    
    # Nếu không thể đến được (M-1, N-1), trả về -1
    return -1
# Hàm giải quyết bài toán
def solve():
    T = int(input())  # Số lượng test cases
    for _ in range(T):
        # Đọc dữ liệu mỗi test case
        M, N = map(int, input().split())
        A = [list(map(int, input().split())) for _ in range(M)]
        
        # Tìm số bước ít nhất từ (0, 0) đến (M-1, N-1)
        result = bfs(M, N, A)
        
        # In kết quả cho mỗi test case
        print(result)

# Chạy chương trình
solve()
