from collections import deque

def max_sliding_window(num_list, k):
    if not num_list or k == 0:
        return []
    
    n = len(num_list)
    result = []
    dq = deque()  # Lưu chỉ số của các phần tử có thể là max trong cửa sổ
    
    for i in range(n):
        # Loại bỏ phần tử ngoài phạm vi cửa sổ k
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Loại bỏ phần tử nhỏ hơn phần tử hiện tại
        while dq and num_list[dq[-1]] < num_list[i]:
            dq.pop()
        
        dq.append(i)  # Thêm chỉ số của phần tử hiện tại vào deque

        # Khi cửa sổ có đủ k phần tử, thêm giá trị lớn nhất vào kết quả
        if i >= k - 1:
            result.append(num_list[dq[0]])

    return result

# Test
num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
print(max_sliding_window(num_list, k))

