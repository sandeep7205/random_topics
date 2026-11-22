
def binary_search(search_list, value):
    """
        Search for a value in a sorted list using Binary Search.

        Binary Search repeatedly divides the search range into half
        until the target value is found or no elements remain.

        Args:
            search_list (list): A list of elements sorted in ascending order.
            value (int): The value to search for.

        Returns:
            tuple: 
                - A list containing the middle values checked during the search.
                - A message indicating the index where the value was found.

            If the value is not found, returns an empty list and
            a "Value not found" message.

        Example:
            binary_search([1, 2, 3, 4, 5], 3)

            Output:
            ([3], 'Value found at index 2')

        Note:
            - The input list must be sorted in ascending order.
            - Time Complexity: O(log n)
            - Space Complexity: O(log n) in this implementation,
            because path_to_target stores the values checked.
    """
  
    # Stores the elements checked during the search
    path_to_target = []

    # Set the starting and ending indexes of the search range
    low = 0
    high = len(search_list) - 1

    # Continue searching while there are elements left to check
    while low <= high:

        # Find the middle index of the current search range
        mid = (low + high) // 2

        # Get the value at the middle index
        value_at_middle = search_list[mid]

        # Keep track of the value we checked
        path_to_target.append(value_at_middle)

        # If the middle value matches the target, return the search path and index
        if value == value_at_middle:
            return path_to_target, (f'Value found at index {mid}')

        # If the target is greater, search the right half
        elif value > value_at_middle:
            low = mid + 1

        # If the target is smaller, search the left half
        else:
            high = mid - 1

    # Return an empty search path if the target is not found
    return [], "Value not found"


# Example 1: Search for 3 in a sorted list
print(binary_search([1, 2, 3, 4, 5], 3))

# Example 2: Search for 4 in a sorted list
print(binary_search([1, 2, 3, 4, 5, 9], 4))

# Example 3: Search for 10, which is not present in the list
print(binary_search([1, 3, 5, 9, 14, 22], 10))
