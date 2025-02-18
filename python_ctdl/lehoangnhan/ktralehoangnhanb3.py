def word_count(file_path):
    word_freq = {}  # Dictionary để lưu số lần xuất hiện của từ

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:  # Đọc từng dòng trong file
            words = line.strip().lower().split()  # Chuyển thành chữ thường, tách thành danh sách từ
            for word in words:
                word_freq[word] = word_freq.get(word, 0) + 1  # Cập nhật số lần xuất hiện

    return dict(sorted(word_freq.items()))  # Sắp xếp từ điển theo bảng chữ cái
file_path = "c:\\Users\\Admin\\Downloads\\P1_data.txt"

print(word_count(file_path))
