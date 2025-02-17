def min_bracket_reversals(s):
    balance = 0  # Theo dõi trạng thái ngoặc
    changes = 0  # Số lần cần đổi dấu ngoặc
    
    for ch in s:
        if ch == '(':
            balance += 1
        else:  # ch == ')'
            if balance > 0:
                balance -= 1  # Khớp với một '(' trước đó
            else:
                changes += 1  # Đổi ')' thành '('
                balance += 1  # Giờ nó là '('
    
    return changes + balance // 2  # Cộng thêm số lần đổi '(' dư thừa

# Đọc số lượng bộ test
T = int(input().strip())
for _ in range(T):
    s = input().strip()
    print(min_bracket_reversals(s))