def count_chars(s):
    s = s.replace(" ", "")  # Loại bỏ khoảng trắng
    return {char: s.count(char) for char in sorted(set(s))}

# Test
print(count_chars("bird"))  # {'b': 1, 'i': 1, 'r': 1, 'd': 1}
print(count_chars("game"))     # {'g': 1, 'a': 1, 'm': 1,'e': 1}
