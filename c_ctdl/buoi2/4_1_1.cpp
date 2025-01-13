#include <iostream>
#include <vector>
#include <chrono> // Thư viện <chrono>

using namespace std;
using namespace std::chrono;

// Hàm Merge Sort
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    vector<int> L(n1), R(n2);
    
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        } else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}

void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

int main() {
    // Tạo mảng ngẫu nhiên
    vector<int> arr = {5, 2, 9, 1, 5, 6};

    // Bắt đầu đo thời gian
    auto start = high_resolution_clock::now();

    // Gọi thuật toán Merge Sort
    mergeSort(arr, 0, arr.size() - 1);

    // Kết thúc đo thời gian
    auto end = high_resolution_clock::now();

    // Tính toán thời gian đã trôi qua (tính bằng mili giây)
    auto duration = duration_cast<milliseconds>(end - start).count();

    // In kết quả
    cout << "Kết quả Merge Sort: ";
    for (int x : arr) cout << x << " ";
    cout << endl;
    cout << "Thoi gian thuc thi (ms) = " << duration << " ms" << endl;

    return 0;
}

