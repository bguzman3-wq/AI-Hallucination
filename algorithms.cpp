#include <cstdint>
#include <iostream>

// ALG09
std::uint32_t fib(int n) {
std::uint32_t a = 0;
std::uint32_t b = 1;

for (int i = 0; i < n; i++) {
    std::uint32_t temp = a + b;
    a = b;
    b = temp;
}

return a;

}

// ALG10
int insertionSortCount(int A[], int n) {
int comparisons = 0;

for (int i = 1; i < n; i++) {
    int key = A[i];
    int j = i - 1;

    while (j >= 0 && (++comparisons, A[j] > key)) {
        A[j + 1] = A[j];
        j--;
    }

    A[j + 1] = key;
}

return comparisons;

}

int main() {
    // ALG09
    std::cout << "ALG09" << std::endl;
    std::cout << "fib(50): " << fib(50) << std::endl;
    std::cout << std::endl;

    // ALG10
    std::cout << "ALG10" << std::endl;
    int A[] = {5, 3, 8, 4, 2};
    int comparisons = insertionSortCount(A, 5);
    std::cout << "Comparisons: " << comparisons << std::endl;
    std::cout << "Sorted array: ";

    for (int x : A) {
        std::cout << x << " ";
    }
    std::cout << std::endl;

    return 0;
}