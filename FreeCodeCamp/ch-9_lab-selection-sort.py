# ---------------------------------------------------------
# Selection Sort Algorithm
# ---------------------------------------------------------

# Selection sort is another popular sorting algorithm taught in most computer science courses.

# This algorithm works by repeatedly finding the smallest element from the unsorted portion of the list and swapping it with the first unsorted element. It begins by selecting the minimum value in the entire list and swapping it with the first element. Then it moves to the second position, finds the smallest value in the remaining unsorted elements, and swaps it with the second element. This process continues, moving through the list one element at a time, until the entire list is sorted.

# Selection sort results in a quadratic time complexity in the best, average, and worst case scenarios. The space complexity will be constant O(1) because the sorting is done in place and a constant amount of memory is being used regardless of the size of the list.

# Objective:
# Implement a selection sort algorithm that sorts a list of
# numbers from smallest to largest.

# How Selection Sort Works:
# 1. Start from the first element of the list.
# 2. Assume the current element is the smallest.
# 3. Search the remaining unsorted portion of the list.
# 4. Find the index of the smallest element.
# 5. Swap the smallest element with the first unsorted element.
# 6. Move to the next position and repeat the process.
# 7. Continue until the entire list is sorted.

# Requirements:
# 1. Define a function named selection_sort.
# 2. The function should accept exactly one parameter (a list).
# 3. Sort the list in ascending order (smallest to largest).
# 4. Modify the original list in-place.
# 5. Return the same list after sorting.
# 6. Follow the actual selection sort algorithm.
# 7. Avoid unnecessary swaps when the smallest element
#    is already in its correct position.
# 8. Do not use the built-in sort() method.
# 9. Do not use the sorted() function.
# 10. Do not import any modules.
# 11. Do not use methods that add or remove list elements.

# Example 1:
# Input:  [33, 1, 89, 2, 67, 245]
# Output: [1, 2, 33, 67, 89, 245]

# Example 2:
# Input:  [5, 16, 99, 12, 567, 23, 15, 72, 3]
# Output: [3, 5, 12, 15, 16, 23, 72, 99, 567]

# Example 3:
# Input:  [1, 4, 2, 8, 345, 123, 43, 32, 5643]
# Output: [1, 2, 4, 8, 32, 43, 123, 345, 5643]

# Time Complexity:
# Best Case:    O(n²)
# Average Case: O(n²)
# Worst Case:  O(n²)

# Space Complexity:
# O(1) - Sorting happens in-place and uses constant extra memory.

# ---------------------------------------------------------
# Tests:
# ---------------------------------------------------------

# 1. Check that the function exists.
# 2. Check that the function accepts exactly one parameter.
# 3. Check that no built-in sorting methods are used.
# 4. Check that the function returns the sorted list.
# 5. Check that the original list is modified in-place.
# 6. Check that the selection sort algorithm is followed.
# 7. Check that unnecessary swaps are avoided.
# 8. Check that all provided test cases return correct results.
# 9. Check that the function works with any list of numbers.






