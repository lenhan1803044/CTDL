#include <vector>
#include <algorithm>
using namespace std;

int median_of_three(vector<int>& arr, int low, int high) {
    int mid = low + (high - low) / 2;
    if (arr[low] > arr[mid])
        swap(arr[low], arr[mid]);
    if (arr[low] > arr[high])
        swap(arr[low], arr[high]);
    if (arr[mid] > arr[high])
        swap(arr[mid], arr[high]);
    return mid;
}

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; ++j) {
        if (arr[j] < pivot) {
            ++i;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

int partition_median(vector<int>& arr, int low, int high) {
    int median = median_of_three(arr, low, high);
    swap(arr[median], arr[high]);
    return partition(arr, low, high);
}

void quickSort_median(vector<int>& arr, int low, int high) {
    if (low < high) {
        int p = partition_median(arr, low, high);
        quickSort_median(arr, low, p - 1);
        quickSort_median(arr, p + 1, high);
    }
}
