# countup() – Adds numbers after the recursive call
def countup(number):
    """
    Create a list of numbers from 1 up to the given number.

    Uses recursion to reach the base case first,
    then adds numbers while returning from recursive calls.
    """

    # Base case: Stop recursion when the number is less than 1
    if number < 1:
        return []

    # Recursive call: Get the list of numbers from 1 to number - 1
    count_list = countup(number - 1)

    # Add the current number to the end of the list
    count_list.append(number)

    # Return the updated list
    return count_list


print(countup(5))




#countdown() – Adds numbers before the recursive result
def countdown(number):
    """
    Create a list of numbers from the given number down to 1.

    Adds the current number first, then combines it
    with the result of the recursive call.
    """

    # Base case: Stop recursion when the number is less than 1
    if number < 1:
        return []

    # Create a list containing the current number
    count_list = [number]

    # Recursive call: Get the remaining numbers and add them to the list
    count_list += countdown(number - 1)

    # Return the combined list
    return count_list


print(countdown(5))
