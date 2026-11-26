
"""
LUHN ALGORITHM — SIMPLE EXPLANATION

1. WHAT IS THE LUHN ALGORITHM?

   - The Luhn Algorithm is used to check whether a number
     is valid or invalid.
   - It is commonly used to validate credit card numbers.
   - It uses a mathematical calculation called Modulus 10
     (Mod 10) to verify the number.


2. HOW DOES IT WORK?

   Example:

       card_number = "453914889"

   Step 1: Start from the RIGHT side.

       - Ignore the last digit initially.
       - The last digit is called the check digit.
       - Move from right to left.
       - Double every second digit.

   Step 2: Double every second digit.

       Original:
           4  5  3  9  1  4  8  8  9

       After doubling:
           4 10  3 18  1  8  8 16  9

   Step 3: If a doubled number is greater than 9,
           subtract 9 from it.

       10 - 9 = 1
       18 - 9 = 9
       16 - 9 = 7

       Result:
           4  1  3  9  1  8  8  7  9

   Step 4: Add all the digits.

       4 + 1 + 3 + 9 + 1 + 8 + 8 + 7 + 9 = 50

   Step 5: Check whether the total is divisible by 10.

       total % 10 == 0

       If the remainder is 0:
           Return "VALID!"

       Otherwise:
           Return "INVALID!"


3. WHAT IS THE CHECK DIGIT?

   - The check digit is the last digit of the card number.
   - It is used to verify whether the complete number
     passes the Luhn calculation.
   - Do not double the check digit.


4. HOW TO HANDLE SPACES AND DASHES?

   Card numbers may contain spaces or dashes.

   Examples:

       "4111-1111-1111-1111"
       "4111 1111 1111 1111"

   Remove spaces and dashes before performing
   the Luhn calculation.

   This makes the calculation easier.


5. IMPORTANT PYTHON OPERATIONS

   Convert string into a list of digits:

       digits = [int(digit) for digit in card_number]

   Reverse the list:

       digits.reverse()

   Check every second digit:

       for i in range(1, len(digits), 2):

   Double a digit:

       digits[i] *= 2

   Subtract 9 if the result is greater than 9:

       if digits[i] > 9:
           digits[i] -= 9

   Calculate the total:

       total = sum(digits)

   Check whether the total is divisible by 10:

       total % 10 == 0


6. FUNCTION REQUIREMENTS

   - Define a function named verify_card_number.
   - It should accept one parameter: card_number.
   - Remove spaces and dashes from the card number.
   - Convert the remaining digits into integers.
   - Reverse the digits to start checking from the right.
   - Double every second digit, excluding the check digit.
   - Subtract 9 if a doubled digit is greater than 9.
   - Add all the digits.
   - Check whether the total is divisible by 10.
   - Return "VALID!" if the number passes.
   - Otherwise, return "INVALID!".


7. EXAMPLE TEST CASES

   Input:
       verify_card_number("453914889")

   Output:
       "VALID!"

   Input:
       verify_card_number("4111-1111-1111-1111")

   Output:
       "VALID!"

   Input:
       verify_card_number("453914881")

   Output:
       "INVALID!"

   Input:
       verify_card_number("1234 5678 9012 3456")

   Output:
       "INVALID!"


8. COMPLETE ALGORITHM IN SIMPLE STEPS

   Step 1: Receive the card number.
   Step 2: Remove spaces and dashes.
   Step 3: Convert each digit into an integer.
   Step 4: Reverse the digits.
   Step 5: Skip the first digit (check digit).
   Step 6: Double every second digit.
   Step 7: Subtract 9 from doubled digits greater than 9.
   Step 8: Add all the digits.
   Step 9: Divide the total by 10 and check the remainder.
   Step 10: Return VALID! or INVALID!.


REMEMBER:

   Luhn Algorithm = Double + Adjust + Add + Check

   If total % 10 == 0:
       VALID!

   Otherwise:
       INVALID!
"""



# 1. Double every second digit:
#    digit = digit * 2
#
# 2. Adjust doubled digits greater than 9:
#    digit = digit - 9
#
# 3. Calculate the sum:
#    total = sum(digits)
#
# 4. Check validity:
#    total % 10 == 0
#
# 5. Final result:
#    VALID! if total % 10 == 0 else INVALID!




# Using list slicing 

def verify_card_number(num_str):
    # Step 1: Remove all spaces and dashes from the card number
    # Example: "4111-1111 1111-1111" becomes "4111111111111111"
    for char in ["-", " "]:
        num_str = num_str.replace(char, "")

    # Store the sum of doubled digits and remaining digits
    right_second_digit = 0
    right_first_digit = 0

    # Step 2: Start from the second digit from the right
    # Move backwards and skip every alternate digit
    # [-2::-2] means start from the second-last digit
    # and move right to left, skipping one digit each time
    for i in num_str[-2::-2]:

        # Convert the character into an integer and double it
        double_num = int(i) * 2

        # Step 3: If the doubled value is greater than 9,
        # add its individual digits together
        if double_num > 9:
            right_second_digit += sum(int(d) for d in str(double_num))
        else:
            # Otherwise, add the doubled value directly
            right_second_digit += double_num

    # Step 4: Add the digits that were not doubled
    # Start from the rightmost digit (check digit)
    # and move backwards, skipping every alternate digit
    for i in num_str[-1::-2]:
        right_second_digit += int(i)

    # Step 5: Calculate the final sum
    total = (right_second_digit + right_first_digit)

    # Step 6: Check whether the total is divisible by 10
    # If the remainder is 0, the card number is valid
    # Otherwise, the card number is invalid
    return "VALID!" if total % 10 == 0 else "INVALID!"


# Example 1: Invalid card number
print(verify_card_number('453914881'))

# Example 2: Valid card number
print(verify_card_number('453914889'))




# Using list slicing (Compact approach)

def verify_card_number(num_str):
    # Remove spaces and dashes
    num_str = num_str.replace("-", "").replace(" ", "")

    # Get digits that need to be doubled
    doubled_digits = num_str[-2::-2]

    # Get digits that should remain unchanged
    unchanged_digits = num_str[-1::-2]

    total = 0

    # Double every second digit
    for digit in doubled_digits:
        value = int(digit) * 2

        # Subtract 9 if the result is greater than 9
        if value > 9:
            value -= 9

        total += value

    # Add the unchanged digits
    total += sum(int(digit) for digit in unchanged_digits)

    # Return the validation result
    return "VALID!" if total % 10 == 0 else "INVALID!"


print(verify_card_number("453914881"))
print(verify_card_number("453914889"))





# Using reverse() and index positions

def verify_card_number(num_str):
    # Remove spaces and dashes
    num_str = num_str.replace("-", "").replace(" ", "")

    # Convert the string into a list of integers
    digits = [int(digit) for digit in num_str]

    # Reverse the list to start from the right
    digits.reverse()

    total = 0

    # Loop through every digit with its index
    for i, digit in enumerate(digits):

        # Double every second digit, excluding the first digit
        if i % 2 == 1:
            digit *= 2

            # Subtract 9 if the doubled value is greater than 9
            if digit > 9:
                digit -= 9

        # Add the digit to the total
        total += digit

    # Check whether the total is divisible by 10
    return "VALID!" if total % 10 == 0 else "INVALID!"


print(verify_card_number("453914881"))
print(verify_card_number("453914889"))



# Using a conditional expression (Compact approach)

def verify_card_number(num_str):
    # Remove spaces and dashes
    num_str = num_str.replace("-", "").replace(" ", "")

    total = 0

    # Start from the right and move towards the left
    for i, digit in enumerate(reversed(num_str)):

        digit = int(digit)

        # Double alternate digits and subtract 9 when needed
        if i % 2:
            digit = digit * 2
            digit = digit - 9 if digit > 9 else digit

        total += digit

    # Check the final sum
    return "VALID!" if total % 10 == 0 else "INVALID!"


print(verify_card_number("453914881"))
print(verify_card_number("453914889"))
