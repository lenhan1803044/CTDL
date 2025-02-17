def max_area_histogram(heights):
    stack = []
    max_area = 0
    n = len(heights)
    
    for i in range(n):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * w)
    
    return max_area

def solve():
    T = int(input())  # Đọc số lượng bộ test
    for _ in range(T):
        N = int(input())  # Đọc số lượng cột
        heights = list(map(int, input().split()))  # Đọc các chiều cao cột
        
        # Tính diện tích hình chữ nhật lớn nhất
        result = max_area_histogram(heights)
        print(result)

# Chạy chương trình
solve()
