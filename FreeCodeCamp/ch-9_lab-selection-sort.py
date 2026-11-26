
"""
SELECTION SORT ALGORITHM — SIMPLE EXPLANATION

1. WHAT IS SELECTION SORT?

   - Selection Sort is a sorting algorithm.
   - It arranges list elements from smallest to largest.
   - It repeatedly finds the smallest number from the
     unsorted part of the list.
   - It swaps that number with the first unsorted element.
   - It continues until the entire list is sorted.


2. HOW DOES IT WORK?

   Example:

       numbers = [33, 1, 89, 2, 67]

   Step 1:
       Find the smallest number in the entire list.

       Smallest = 1

       Swap 1 with 33.

       [1, 33, 89, 2, 67]

   Step 2:
       Ignore the first sorted element.
       Find the smallest number in the remaining list.

       Smallest = 2

       Swap 2 with 33.

       [1, 2, 89, 33, 67]

   Step 3:
       Find the smallest number in the remaining list.

       Smallest = 33

       Swap 33 with 89.

       [1, 2, 33, 89, 67]

   Step 4:
       Find the smallest number in the remaining list.

       Smallest = 67

       Swap 67 with 89.

       [1, 2, 33, 67, 89]

   Final Result:

       [1, 2, 33, 67, 89]


3. HOW TO FIND THE SMALLEST NUMBER?

   - Assume the first unsorted element is the smallest.
   - Compare it with every remaining element.
   - If a smaller number is found, update the smallest
     element's index.
   - Continue until the end of the unsorted portion.


4. HOW DOES SWAPPING WORK?

   - Once the smallest element is found, swap it with
     the first unsorted element.

   Example:

       numbers = [33, 1, 89]

       smallest_index = 1
       current_index = 0

       Swap:

       numbers[current_index], numbers[smallest_index] = (
           numbers[smallest_index], numbers[current_index]
       )

       Result:

       [1, 33, 89]


5. AVOID UNNECESSARY SWAPS

   - Check whether the smallest element is already
     in the correct position.
   - If both indexes are the same, do not swap.

       if smallest_index != current_index:
           # Perform the swap


6. TIME COMPLEXITY

   Best Case:
       O(n²)

   Average Case:
       O(n²)

   Worst Case:
       O(n²)

   Explanation:
       The algorithm repeatedly compares elements
       to find the smallest number.


7. SPACE COMPLEXITY

   O(1)

   Explanation:
       Sorting happens inside the original list.
       No additional list is required.


8. IMPORTANT RULES

   - Define a function named selection_sort.
   - The function should accept one list parameter.
   - Sort numbers from smallest to largest.
   - Modify the original list directly (in-place).
   - Return the same sorted list.
   - Find the minimum element in the unsorted portion.
   - Swap it with the first unsorted element.
   - Avoid unnecessary swaps.
   - Do not use sort() or sorted().
   - Do not import any modules.
   - Do not use methods that add or remove list items.


9. COMPLETE ALGORITHM IN SIMPLE STEPS

   Step 1: Start from the first position of the list.

   Step 2: Assume the current element is the smallest.

   Step 3: Compare it with all remaining elements.

   Step 4: Find the index of the smallest element.

   Step 5: Check whether swapping is necessary.

   Step 6: Swap the smallest element with the current element.

   Step 7: Move to the next position.

   Step 8: Repeat until the list is sorted.

   Step 9: Return the sorted list.


REMEMBER:

   Selection Sort = Find Smallest + Swap + Repeat

   Every iteration places one smallest remaining element
   into its correct position.
"""


# 1. Outer loop:
#    Move through each position in the list.
#
#    for i in range(len(numbers)):
#
# 2. Assume current position is the minimum:
#
#    min_index = i
#
# 3. Inner loop:
#    Search for the smallest element in the remaining list.
#
#    for j in range(i + 1, len(numbers)):
#
# 4. Compare elements:
#
#    if numbers[j] < numbers[min_index]:
#        min_index = j
#
# 5. Swap only when necessary:
#
#    if min_index != i:
#        numbers[i], numbers[min_index] = (
#            numbers[min_index], numbers[i]
#        )
#
# 6. Return the original sorted list:
#
#    return numbers






def selection_sort(arr):
    # Get the total number of elements in the list
    arr_count = len(arr)

    # Outer loop: Move through each position in the list
    for i in range(arr_count):

        # Assume the current position contains the smallest element
        small_i = i

        # Inner loop: Search for the smallest element
        # in the remaining unsorted portion of the list
        for j in range((i + 1), arr_count):

            # Compare the current element with the smallest found so far
            if arr[j] < arr[small_i]:

                # Update the index if a smaller element is found
                small_i = j

        # Check if the smallest element is already in the correct position
        if small_i != i:

            # Swap the current element with the smallest element
            # Python allows swapping two values in a single statement
            arr[i], arr[small_i] = arr[small_i], arr[i]

    # Return the sorted list (the original list is modified in-place)
    return(arr)


# Example: Sort the list from smallest to largest
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))

# Expected Output:
# [3, 5, 12, 15, 16, 23, 72, 99, 567]
