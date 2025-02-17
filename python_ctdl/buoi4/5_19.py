def stock_span(N, prices):
    # Kết quả sẽ lưu trữ nhịp chứng khoán của các ngày
    span = [0] * N
    stack = []
    
    for i in range(N):
        # Tính toán nhịp chứng khoán cho ngày i
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()  # Loại bỏ các ngày có giá nhỏ hơn hoặc bằng giá ngày i
        if stack:
            span[i] = i - stack[-1]
        else:
            span[i] = i + 1  # Nếu không có ngày nào có giá nhỏ hơn hoặc bằng thì nhịp là i+1
        stack.append(i)  # Thêm ngày i vào stack
    
    return span

def solve():
    T = int(input())  # Số bộ test
    for _ in range(T):
        N = int(input())  # Số ngày
        prices = list(map(int, input().split()))  # Giá chứng khoán các ngày
        span = stock_span(N, prices)
        print(" ".join(map(str, span)))  # In kết quả cho mỗi test

# Chạy chương trình
solve()
