def solve(n, A):
    # Kết quả là mảng hai chiều để chứa next greater và next smaller
    next_greater = [-1] * n
    next_smaller = [-1] * n
    stack_greater = []
    
    # Bước 1: Tìm next greater cho mỗi phần tử
    for i in range(n - 1, -1, -1):
        while stack_greater and A[stack_greater[-1]] <= A[i]:
            stack_greater.pop()
        if stack_greater:
            next_greater[i] = A[stack_greater[-1]]
        stack_greater.append(i)
    
    # Bước 2: Tìm next smaller cho mỗi phần tử lớn hơn tiếp theo
    for i in range(n):
        if next_greater[i] == -1:
            continue
        stack_smaller = []
        for j in range(i + 1, n):
            if A[j] < next_greater[i]:
                stack_smaller.append(A[j])
        
        if stack_smaller:
            next_smaller[i] = stack_smaller[0]

    return next_smaller

# Đọc số lượng bộ test
T = int(input())

# Xử lý từng bộ test
for _ in range(T):
    # Đọc n và mảng A[]
    n = int(input())
    A = list(map(int, input().split()))
    
    # Giải quyết và in kết quả
    result = solve(n, A)
    print(" ".join(map(str, result)))
