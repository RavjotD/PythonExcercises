# Selection Sort
# Check for smallest minimum value that and processes a swap until all elements are swapped in order from smallest to largest.

def SelectionSort(A):
    size = len(A)
    # for each iteration of array
    for x in range(size):
        # x = minimum value
        minimal = x
        # for iteration of every second value in array, first two values need to compare
        # Swap occures of conditional is true, return sorted array
        for j in range( x + 1, size):
            if A[j] < A[minimal]:
                minimal = j
        A[x], A[minimal] = A[minimal], A[x]
    return A
