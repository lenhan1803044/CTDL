def generate_lucky_numbers(current_number, max_length, lucky_numbers):
    if len(current_number) > max_length:
        return
    if len(current_number) > 0:
        lucky_numbers.append(int(current_number))
    generate_lucky_numbers(current_number + '6', max_length, lucky_numbers)
    generate_lucky_numbers(current_number + '8', max_length, lucky_numbers)

def solve():
    T = int(input())  # Đọc số lượng test cases
    for _ in range(T):
        N = int(input())  # Đọc số N cho mỗi test case
        lucky_numbers = []
        
        # Sinh tất cả các số lộc phát có từ 1 đến N chữ số
        generate_lucky_numbers('', N, lucky_numbers)
        
        # Sắp xếp các số lộc phát theo thứ tự giảm dần
        lucky_numbers.sort(reverse=True)
        
        # In ra kết quả cho mỗi test case
        print(len(lucky_numbers))
        print(" ".join(map(str, lucky_numbers)))

# Chạy chương trình
solve()
