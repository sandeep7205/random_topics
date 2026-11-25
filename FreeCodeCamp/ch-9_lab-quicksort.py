

# ============================================================
# IMPLEMENT THE QUICKSORT ALGORITHM
# ============================================================

# OBJECTIVE:
# Implement the Quicksort algorithm and pass all the lab tests.


# USER STORIES:
#
# 1. Define a function named quick_sort to implement the
#    Quicksort algorithm.
#
# 2. The quick_sort function should:
#    - Accept a list of integers as input.
#    - Return a NEW list sorted from least to greatest.
#    - NOT modify the original input list.
#
#
# ALGORITHM REQUIREMENTS:
#
# 1. Choose a pivot value from the input list.
#    - Use either the first or the last element as the pivot.
#
# 2. Partition the input list into THREE sublists:
#    - left_list: Elements smaller than the pivot.
#    - mid_list: Elements equal to the pivot.
#    - right_list: Elements greater than the pivot.
#
# 3. Recursively call quick_sort to sort:
#    - left_list
#    - right_list
#
# 4. Concatenate the three lists to produce the final result:
#    - Sorted left_list
#    - mid_list
#    - Sorted right_list
#
#
# RESTRICTIONS:
#
# - Do NOT import any modules.
# - Do NOT use the built-in sorted() function.
# - Do NOT use the list.sort() method.
#
#
# TEST CASES:
#
# 1. quick_sort([]) should return []
#
# 2. quick_sort([20, 3, 14, 1, 5])
#    Expected: [1, 3, 5, 14, 20]
#
# 3. quick_sort([83, 4, 24, 2])
#    Expected: [2, 4, 24, 83]
#
# 4. quick_sort([4, 42, 16, 23, 15, 8])
#    Expected: [4, 8, 15, 16, 23, 42]
#
# 5. quick_sort([87, 11, 23, 18, 18, 23, 11, 56, 87, 56])
#    Expected: [11, 11, 18, 18, 23, 23, 56, 56, 87, 87]
#
#
# VALIDATION CHECKLIST:
#
# [ ] Function is named quick_sort.
# [ ] Function accepts exactly one parameter.
# [ ] Empty list returns an empty list.
# [ ] Original input list remains unchanged.
# [ ] All test cases return correctly sorted lists.
# [ ] No modules are imported.
# [ ] No built-in sorting methods are used.


# ======================================================================================================================================================================================


# ==================================================
# QUICKSORT ALGORITHM - BASIC STEPS
# ==================================================

#  Quicksort is a divide-and-conquer algorithm that sorts around a "pivot". It picks a pivot element, then partitions the array so everything smaller comes before it and everything larger comes after - which locks the pivot into its final sorted position. It then recurses on the left and right partitions. This visualization uses the Lomuto scheme with the last element as pivot. Press play to watch the partitioning and pivot placement.

# Quicksort is usually the fastest general-purpose sort in practice thanks to good cache behavior and in-place partitioning, averaging O(n log n). Its worst case is O(n²) (e.g. an already-sorted array with a poor pivot choice), which good pivot strategies like median-of-three or randomization avoid.



# 1. CHOOSE A PIVOT
#    Select an element from the list.
#    Use either the first or last element as the pivot.

# 2. CREATE THREE PARTITIONS
#    - Left: Elements smaller than the pivot.
#    - Middle: Elements equal to the pivot.
#    - Right: Elements greater than the pivot.

# 3. DISTRIBUTE ELEMENTS
#    Iterate through the input list.
#    Compare each element with the pivot.
#    Add it to the appropriate partition.

# 4. RECURSION
#    Call quick_sort() recursively on:
#    - Left partition
#    - Right partition

# 5. BASE CONDITION
#    If the list has 0 or 1 elements,
#    return the list because it is already sorted.

# 6. COMBINE
#    Concatenate all three partitions:
#    Sorted Left + Middle + Sorted Right.

# ==================================================
# KEY CONCEPT: DIVIDE AND CONQUER
# ==================================================
# Divide   -> Split the list around the pivot.
# Conquer  -> Recursively sort smaller partitions.
# Combine  -> Join the sorted partitions.













def quick_sort(arr):

    # BASE CASE:
    # If the list has 0 or 1 elements, it is already sorted.
    # No further recursion is needed.
    if len(arr) <= 1:
        return arr

    # Choose the last element as the pivot.
    # The pivot is the value used to divide the list.
    pivot = arr[len(arr) - 1]

    # Create three empty lists to divide the elements:
    left_list = []   # Elements smaller than the pivot
    right_list = []  # Elements greater than the pivot
    mid_list = []    # Elements equal to the pivot

    # Iterate through every element in the original list.
    for element in arr:

        # If the element equals the pivot,
        # add it to the middle list.
        if element == pivot:
            mid_list.append(element)

        # If the element is smaller than the pivot,
        # add it to the left list.
        elif element < pivot:
            left_list.append(element)

        # If the element is greater than the pivot,
        # add it to the right list.
        else:
            right_list.append(element)

    # RECURSION + COMBINATION:
    # Recursively sort the left and right lists.
    # The middle list does not need sorting because
    # all its elements are equal to the pivot.
    #
    # Combine all three lists:
    # 1. Sorted smaller elements
    # 2. Elements equal to the pivot
    # 3. Sorted greater elements
    return quick_sort(left_list) + mid_list + quick_sort(right_list)


# Test the quick_sort function
print(quick_sort([8, 3, 1, 7, 0, 10, 2]))













# ==========================================
# PYTHONIC IMPLEMENTATION (LIST COMPREHENSIONS)
# ==========================================

def quick_sort(arr):

    # BASE CASE:
    # If the list contains 0 or 1 elements,
    # it is already sorted, so return it.
    if len(arr) <= 1:
        return arr

    # Choose the middle element as the pivot.
    # // performs integer division.
    # Example: 5 // 2 = 2 (index 2).
    pivot = arr[len(arr) // 2]

    # PARTITIONING:
    # Create three separate lists using list comprehensions.

    # Store all elements smaller than the pivot.
    left = [x for x in arr if x < pivot]

    # Store all elements equal to the pivot.
    # This also handles duplicate values.
    middle = [x for x in arr if x == pivot]

    # Store all elements greater than the pivot.
    right = [x for x in arr if x > pivot]

    # RECURSION + COMBINATION:
    # Recursively sort the left and right lists.
    # The middle list is already sorted because
    # all its elements have the same value.
    #
    # Combine the results:
    # Sorted Left + Middle + Sorted Right.
    return quick_sort(left) + middle + quick_sort(right)


# EXAMPLE USAGE:

# Original unsorted list.
numbers = [10, 7, 8, 9, 1, 5]

# Call quick_sort() and store the returned sorted list.
# The original numbers list remains unchanged.
sorted_numbers = quick_sort(numbers)

# Display the sorted result.
print(sorted_numbers)  # Output: [1, 5, 7, 8, 9, 10]














# ==========================================
# IN-PLACE IMPLEMENTATION (MEMORY EFFICIENT)
# ==========================================

# PARTITION FUNCTION:
# This function places the pivot in its correct
# sorted position and separates smaller and larger elements.

def partition(arr, low, high):

    # Choose the last element as the pivot.
    pivot = arr[high]

    # Initialize a pointer just before the starting index.
    # This pointer tracks the position of smaller elements.
    i = low - 1

    # Iterate through the list from low to high - 1.
    # We exclude the pivot because it is stored at arr[high].
    for j in range(low, high):

        # Check whether the current element is
        # smaller than or equal to the pivot.
        if arr[j] <= pivot:

            # Move the smaller-element pointer one position forward.
            i += 1

            # Swap the current element with the element at index i.
            # This moves smaller elements towards the left side.
            arr[i], arr[j] = arr[j], arr[i]

    # After the loop, place the pivot in its correct position.
    # Swap the pivot with the element immediately after index i.
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    # Return the pivot's final sorted position.
    return i + 1


# QUICK SORT FUNCTION:
# This function recursively sorts the list using partition().
# Unlike the previous implementation, it modifies the original list.

def quick_sort_inplace(arr, low, high):

    # BASE CONDITION:
    # Continue sorting only when the partition
    # contains at least two elements.
    if low < high:

        # Partition the list and get the pivot's final position.
        pi = partition(arr, low, high)

        # RECURSION:
        # Sort the elements on the left side of the pivot.
        quick_sort_inplace(arr, low, pi - 1)

        # Sort the elements on the right side of the pivot.
        quick_sort_inplace(arr, pi + 1, high)


# EXAMPLE USAGE:

# Original unsorted list.
numbers = [10, 7, 8, 9, 1, 5]

# Call quick_sort_inplace().
# low = 0 represents the first index.
# high = len(numbers) - 1 represents the last index.
quick_sort_inplace(numbers, 0, len(numbers) - 1)

# Display the sorted original list.
print(numbers)  # Output: [1, 5, 7, 8, 9, 10]
