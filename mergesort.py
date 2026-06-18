"""Implementation of the merge sort algorithm with a small demonstration."""

import matplotlib.pyplot as plt


def merge_sort(array):
    """Sort a list in ascending order in place using merge sort.
    
    Merge sort is a divide-and-conquer algorithm: the list is split into two
    halves, each half is sorted recursively, and the two sorted halves are
    then merged back together.

    Args:
        array: The list to sort. It is modified in place.
    """
    
    # Base case: a list with 0 or 1 element is already sorted
    if len(array) <= 1:
        return
        
    # 1. Divide: split the list into a left and a right half.    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # 2. Conquer: sort each half recursively
    merge_sort(left)
    merge_sort(right)

    # 3. Merge: combine the two sorted halves back into array
    left_index = 0
    right_index = 0
    merge_index = 0

    # Repeatedly take the smaller front element of the two halves
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            array[merge_index] = left[left_index]
            left_index += 1
        else:
            array[merge_index] = right[right_index]
            right_index += 1
        merge_index += 1

    # Copy any remaining elements from the left half
    while left_index < len(left):
        array[merge_index] = left[left_index]
        left_index += 1
        merge_index += 1

    while right_index < len(right):
        array[merge_index] = right[right_index]
        right_index += 1
        merge_index += 1


if __name__ == "__main__":

    my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    unsorted_list = my_list.copy()   # create a copy
    merge_sort(my_list)               # sort in place

    # Create a plot for a comparison (before and after)
    fig, (ax_before, ax_after) = plt.subplots(1, 2, figsize=(10, 4))

    ax_before.bar(range(len(unsorted_list)), unsorted_list, color="steelblue")
    ax_before.set_title("Before sorting")
    ax_before.set_xlabel("Index")
    ax_before.set_ylabel("Value")

    ax_after.bar(range(len(my_list)), my_list, color="seagreen")
    ax_after.set_title("After merge sort")
    ax_after.set_xlabel("Index")
    ax_after.set_ylabel("Value")

    fig.suptitle("Merge sort result")
    fig.tight_layout()
    plt.show()  
