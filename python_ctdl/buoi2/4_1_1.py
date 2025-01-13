import time

# Hàm Merge Sort đã được cài đặt ở Tiết 3
def merge(arr, left, mid, right):
    # Triển khai hàm merge như đã học
    n1 = mid - left + 1
    n2 = right - mid
    L = arr[left:left+n1]
    R = arr[mid+1:mid+1+n2]

    i, j = 0, 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)
        merge_sort(arr, mid+1, right)
        merge(arr, left, mid, right)

if __name__ == "__main__":
    # Tạo mảng ngẫu nhiên
    arr = [5, 2, 9, 1, 5, 6]

    # Bắt đầu đo thời gian
    start = time.time()

    # Gọi thuật toán Merge Sort
    merge_sort(arr, 0, len(arr)-1)

    # Kết thúc đo thời gian
    end = time.time()

    # Tính toán thời gian đã trôi qua (tính bằng mili giây)
    elapsed_ms = (end - start) * 1000

    # In kết quả
    print("Kết quả Merge Sort:", arr)
    print("Thời gian thực thi (ms):", elapsed_ms, "ms")