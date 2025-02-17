def count_BDN(N):
    # Hàm đếm số BDN nhỏ hơn N
    count = 0
    queue = ['1']  # Khởi đầu với '1' (vì '0' không phải số dương)
    
    while queue:
        num = queue.pop(0)  # Lấy số đầu tiên trong hàng đợi
        if int(num) < N:
            count += 1  # Nếu số nhỏ hơn N, tăng count
            queue.append(num + '0')  # Thêm '0' vào cuối số hiện tại
            queue.append(num + '1')  # Thêm '1' vào cuối số hiện tại
    return count

def solve():
    T = int(input())  # Số bộ test
    for _ in range(T):
        N = int(input())  # Đọc số N
        print(count_BDN(N))  # In ra số lượng số BDN nhỏ hơn N

# Chạy chương trình
solve()
