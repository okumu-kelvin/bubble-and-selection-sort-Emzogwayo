def selection_sort(arr):
    n = len(arr)

    # Outer loop: we go through each position in the array
    for i in range(n):

        # Assume the current index is the position of the smallest element
        min_idx = i

        # Inner loop: find the smallest element in the remaining unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j # Update index of smallest element

        # Swap the smallest found element with the one at position i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
