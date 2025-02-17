def find_next_greater_frequency(n, arr):
    # Đếm số lần xuất hiện của từng phần tử trong mảng
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Kết quả sẽ được lưu trữ ở đây
    ans = [-1] * n
    
    # Sử dụng stack để tìm phần tử gần nhất có tần suất xuất hiện lớn hơn
    stack = []
    
    # Duyệt mảng từ phải sang trái
    for i in range(n - 1, -1, -1):
        while stack and freq[stack[-1]] <= freq[arr[i]]:
            stack.pop()  # Xóa các phần tử có tần suất nhỏ hơn hoặc bằng phần tử hiện tại
        if stack:
            ans[i] = stack[-1]  # Phần tử trên đỉnh stack có tần suất lớn hơn phần tử hiện tại
        stack.append(arr[i])  # Thêm phần tử hiện tại vào stack
    
    return ans

def solve():
    T = int(input())  # Số lượng bộ test
    for _ in range(T):
        n = int(input())  # Số phần tử trong mảng
        if n == 0:
            print()
            continue
        arr = list(map(int, input().split()))  # Mảng A[]
        ans = find_next_greater_frequency(n, arr)
        print(" ".join(map(str, ans)))  # In kết quả cho mỗi test

# Chạy chương trình
solve()
