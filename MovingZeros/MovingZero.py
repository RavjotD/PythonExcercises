#MoveZerostoEnd
#Problem: number of ints in array, move all zeros found to end of array, keep same order.

# Use pointer technique to push elements to the front of array.
# Start by moving non-zero valued ints to the front of index.A[count].
# iterate second loop to swap 0 from the last to indexes that need to be replaced.
# Whatever elements are left, those should be equal to zero within the range.
def MoveZeros(A):
    counter = 0
    n = len(A)
    for x in range(n):
        if A[x] != 0:
            A[counter] = A[x]
            counter += 1
    for x in range(counter,n):
        A[x] = 0
    return A