# =====================================================
# Project: Build a Range of Numbers Generator
# Concept: Recursion
# =====================================================

# Objective:
# Create a function named range_of_numbers() that uses
# recursion to generate a list of consecutive numbers
# between start_num and end_num (including both).


# -------------------- User Stories --------------------

# 1. Create a function named range_of_numbers with
#    two parameters:
#    - start_num
#    - end_num

# 2. The function should return a list of consecutive
#    integers starting from start_num and ending at
#    end_num (including both).

#    Example:
#    range_of_numbers(3, 9)
#    Expected output: [3, 4, 5, 6, 7, 8, 9]

# 3. If start_num and end_num are equal, return a list
#    containing only start_num.
#
#    This is the BASE CASE.
#
#    Example:
#    range_of_numbers(5, 5)
#    Expected output: [5]

# 4. For the RECURSIVE CASE:
#    - Call the same function recursively.
#    - Move start_num closer to end_num.
#    - Add the current number to the list returned
#      by the recursive call.

# 5. The function must call itself (recursion).

# 6. Do NOT use:
#    - for loops
#    - while loops
#    - List comprehensions
#    - range() function

# 7. Do NOT use global variables to store the list.
#    Each function call should return its own result.


# -------------------- Test Cases --------------------

# Test 1:
# range_of_numbers(1, 5)
# Expected: [1, 2, 3, 4, 5]

# Test 2:
# range_of_numbers(6, 9)
# Expected: [6, 7, 8, 9]

# Test 3:
# range_of_numbers(4, 4)
# Expected: [4]

# Test 4:
# range_of_numbers(10, 15)
# Expected: [10, 11, 12, 13, 14, 15]

# Test 5:
# Calling range_of_numbers(1, 3) should not affect
# a later call to range_of_numbers(6, 9).


# -------------------- Your Task --------------------

# Step 1: Identify the base case.
# Step 2: Identify the recursive case.
# Step 3: Decide how to move towards the base case.
# Step 4: Return the final list.
# Step 5: Run all test cases and verify the output.


# Write your solution below:




# =====================================================
# Approach 1: Move end_num backwards
# List is built while recursion returns (append).
# Output: [3, 4, 5, 6, 7, 8, 9]
# =====================================================

def range_of_numbers(start_num, end_num):

    # Base case: If start_num is greater than end_num,
    # return an empty list.
    if not (start_num <= end_num):
        return []

    # Base case: When both numbers are equal,
    # return a list containing that number.
    if start_num == end_num:
        return [start_num]

    # Recursive case: Keep decreasing end_num
    # until it reaches start_num.
    numbers_list = range_of_numbers(start_num, end_num - 1)

    # Add the current end_num to the returned list.
    numbers_list.append(end_num)

    # Return the final list.
    return numbers_list


print(range_of_numbers(3, 9))


# =====================================================
# Approach 2: Move start_num forwards
# List is built using list concatenation (prepend).
# Output: [3, 4, 5, 6, 7, 8, 9]
# =====================================================

def range_of_numbers(start_num, end_num):

    # Base case: When both numbers are equal,
    # return a list containing that number.
    if start_num == end_num:
        return [start_num]

    # Recursive case: Keep increasing start_num
    # until it reaches end_num.
    numbers_list = range_of_numbers(start_num + 1, end_num)

    # Add the current start_num at the beginning
    # of the list returned by the recursive call.
    return [start_num] + numbers_list


print(range_of_numbers(3, 9))


# =====================================================
# Approach 3: Move start_num forwards
# List is built while recursion returns (append).
# Output: [9, 8, 7, 6, 5, 4, 3]
# =====================================================

def range_of_numbers(start_num, end_num):

    # Base case: If start_num is greater than end_num,
    # return an empty list.
    if not (start_num <= end_num):
        return []

    # Base case: When both numbers are equal,
    # return a list containing that number.
    if start_num == end_num:
        return [start_num]

    # Recursive case: Keep increasing start_num
    # until it reaches end_num.
    numbers_list = range_of_numbers(start_num + 1, end_num)

    # Add the current start_num to the END of the list.
    # This creates a descending order.
    numbers_list.append(start_num)

    # Return the final list.
    return numbers_list


print(range_of_numbers(3, 9))


# =====================================================
# Approach 4: Move start_num forwards
# List is built using list concatenation (append).
# Output: [9, 8, 7, 6, 5, 4, 3]
# =====================================================

def range_of_numbers(start_num, end_num):

    # Base case: When both numbers are equal,
    # return a list containing end_num.
    if start_num == end_num:
        return [end_num]

    # Recursive case: Keep increasing start_num
    # until it reaches end_num.
    numbers_list = range_of_numbers(start_num + 1, end_num)

    # Add the current start_num at the END of the
    # returned list using list concatenation.
    return numbers_list + [start_num]


print(range_of_numbers(3, 9))
