def levenshtein_distance(token1, token2):
    # Tạo một ma trận để lưu trữ khoảng cách
    dp = [[0] * (len(token2) + 1) for _ in range(len(token1) + 1)]
    
    # Khởi tạo các giá trị ban đầu
    for i in range(len(token1) + 1):
        dp[i][0] = i
    for j in range(len(token2) + 1):
        dp[0][j] = j

    # Tính khoảng cách Levenshtein
    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # Không cần biến đổi
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,    # Xóa
                               dp[i][j - 1] + 1,    # Thêm
                               dp[i - 1][j - 1] + 1)  # Thay thế

    return dp[len(token1)][len(token2)]

# Ví dụ sử dụng
assert levenshtein_distance("hi", "hello") == 4.0
print(levenshtein_distance("hi", "hello"))  # Kết quả: 4