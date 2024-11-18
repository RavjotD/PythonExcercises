# Selection Sort
# Check for smallest minimum value between elements in a array.
# Processes a swap until all smallest valued elements are swapped in order from smallest to largest.

def SelectionSort(A):
    size = len(A)
    # for first iteration check of array array, instalize a minimum varaible for each check
    for x in range(size):
        minimal = x
        # for iteration of every value of in front of x index in array, condition to comparae smalleer valued elements.
        # Swap occures if conditional is true, return sorted array
        for j in range( x + 1, size):
            if A[j] < A[minimal]:
                minimal = j
        A[x], A[minimal] = A[minimal], A[x]
    return A
