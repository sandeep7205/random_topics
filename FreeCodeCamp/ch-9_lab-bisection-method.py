# Implement the Bisection Method
#
# The bisection method (also known as the binary search method) is used
# to find the root of a real-valued function by repeatedly dividing an
# interval into two halves until the desired tolerance is achieved.
#
# In this lab, implement a function named square_root_bisection() to
# calculate the square root of a given number.
#
# Function Requirements:
#
# 1. Define a function named square_root_bisection with three parameters:
#    - square_target: The number whose square root needs to be calculated.
#    - tolerance: The acceptable error margin (set a default value).
#    - maximum: The maximum number of iterations (set a default value).
#
# 2. If square_target is negative, raise a ValueError with the message:
#    "Square root of negative number is not defined in real numbers"
#
# 3. If square_target is 0 or 1:
#    - Print: "The square root of [number] is [number]"
#    - Return the number itself.
#
# 4. For any other positive number:
#    - Use the bisection method to calculate its approximate square root.
#    - Print: "The square root of [square_target] is approximately [root]"
#    - Return the calculated square root.
#
# 5. If the algorithm does not converge within the maximum iterations:
#    - Print: "Failed to converge within [maximum] iterations"
#    - Return None.
#
# Example:
# If the tolerance is 0.01, keep dividing the interval in half until
# the difference between the upper and lower bounds is less than or
# equal to the specified tolerance.
#
# Restrictions:
# - Do not import any modules.
# - Use the bisection method to calculate the square root.
#
# Test Cases:
# - square_root_bisection(0) should return 0.
# - square_root_bisection(1) should return 1.
# - square_root_bisection(0.001, 1e-7, 50) should return approximately 0.0316228.
# - square_root_bisection(0.25, 1e-7, 50) should return approximately 0.5.
# - square_root_bisection(81, 1e-3, 50) should return approximately 9.
# - square_root_bisection(225, 1e-3, 100) should return approximately 15.
# - square_root_bisection(225, 1e-5, 100) should return approximately 15.
# - square_root_bisection(225, 1e-7, 100) should return approximately 15.
# - square_root_bisection(225, 1e-7, 10) should return None.





def square_root_bisection(number, tolerance=0.01, max_iterations=100):

    # STEP 1: Validate the input.
    # A negative number does not have a real square root.
    if number < 0:
        raise ValueError("Square root of negative number is not defined in real numbers")

    # STEP 2: Handle special cases.
    # The square root of 0 is 0, and the square root of 1 is 1.
    # No bisection calculation is needed for these numbers.
    if number in [0, 1]:
        print(f"The square root of {number} is {number}")
        return number

    # STEP 3: Initialize the search boundaries.
    # low starts at 0.
    # If number > 1, its square root is between 0 and number.
    # If number < 1, its square root is between 0 and 1.
    low = 0
    high = number if number > 1 else 1

    # STEP 4: Start the bisection process.
    # Repeat the calculation until the required tolerance is achieved
    # or the maximum number of iterations is reached.
    for i in range(max_iterations):

        # STEP 5: Calculate the midpoint of the current interval.
        mid = (low + high) / 2

        # STEP 6: Compare the square of the midpoint with the target.
        # If mid * mid is greater than number, midpoint is too large.
        # Keep the left half by updating high.
        if mid * mid > number:
            high = mid

        # If mid * mid is smaller than or equal to number,
        # midpoint is too small or is the exact root.
        # Keep the right half by updating low.
        else:
            low = mid

        # STEP 7: Check the convergence condition.
        # If the interval width is within the acceptable tolerance,
        # calculate the midpoint of the UPDATED interval.
        if (high - low) <= tolerance:

            # Calculate the final approximate square root.
            root = (low + high) / 2

            # Display the approximate square root.
            print(f"The square root of {number} is approximately {root}")

            # Return the calculated square root.
            return root

    # STEP 8: Handle failure to converge.
    # If the loop finishes without meeting the tolerance,
    # display the failure message and return None.
    print(f"Failed to converge within {max_iterations} iterations")
    return None
    
    
    
    

"""
BISECTION METHOD — CORE MATHEMATICAL FORMULAS
(For solving different types of equations)

1. GENERAL EQUATION (WHAT WE WANT TO SOLVE)

   Every equation must be converted into:

       f(x) = 0

   Examples:

   Linear equation:
       2*x - 10 = 0

   Quadratic equation:
       x**2 - 25 = 0

   Cubic equation:
       x**3 - 8 = 0

   Square root:
       x**2 - 25 = 0

   Trigonometric equation:
       sin(x) - 0.5 = 0

   Exponential equation:
       2**x - 8 = 0

   Logarithmic equation:
       log(x) - 1 = 0


2. INITIAL INTERVAL (LOWER AND UPPER LIMIT)

   Choose two values:

       a = lower limit
       b = upper limit

   The function values at these two points must have
   opposite signs:

       f(a) * f(b) < 0

   This means a root exists between a and b,
   provided the function is continuous in that interval.


3. MIDPOINT FORMULA (FIND THE MIDDLE VALUE)

       c = (a + b) / 2

   Where:
       a = lower limit
       b = upper limit
       c = middle value


4. CHECK THE MIDDLE VALUE

   Calculate:

       f(c)

   Three possible conditions:

   A. Exact root found:

       f(c) == 0

       Root = c

   B. Root exists in the left half:

       f(a) * f(c) < 0

       Update:
           b = c

   C. Root exists in the right half:

       f(c) * f(b) < 0

       Update:
           a = c


5. STOPPING CONDITION (TOLERANCE)

   Tolerance means how accurate the answer should be.

   Interval-based stopping condition:

       (b - a) / 2 <= tolerance

   Function-based stopping condition:

       abs(f(c)) <= tolerance
   
   
   Check the difference between the upper and lower limits:

     (b - a) <= tolerance


   If the difference is smaller than or equal to the
   allowed tolerance, stop the calculation.

   Example:
     a = 4.99
     b = 5.00
     tolerance = 0.01

     b - a = 0.01

     Since (b - a) <= tolerance:
	 The required accuracy is achieved.
	 Stop the loop and return the midpoint.

   NOTE:
     (b - a) / 2 <= tolerance checks the maximum
     distance from the midpoint to the actual root.

     (b - a) <= tolerance checks the total width
     of the remaining interval.

     
   You can use either condition depending on
   the accuracy requirement of your problem.


6. MAXIMUM ITERATIONS

   Maximum iterations define how many times the
   algorithm is allowed to repeat.

   Required iterations (theoretical estimate):

       n >= log2((b - a) / tolerance)

   This tells us approximately how many iterations
   are needed to reach the required interval accuracy.

   If the maximum iterations are reached without
   satisfying the stopping condition:

       Print failure message
       Return None


7. ERROR CALCULATION

   Absolute function error:

       error = abs(f(c))

   Interval error:

       error = (b - a) / 2

   Both help measure how close the approximation is
   to the actual root.


8. DIFFERENT EQUATIONS — EXAMPLES

   Linear:
       f(x) = 2*x - 10

   Quadratic:
       f(x) = x**2 - 25

   Cubic:
       f(x) = x**3 - 8

   Square root:
       f(x) = x**2 - N

   Fourth power:
       f(x) = x**4 - 16

   Trigonometric:
       f(x) = sin(x) - 0.5

   Exponential:
       f(x) = 2**x - 8

   Logarithmic:
       f(x) = log(x) - 1


9. IMPORTANT RULES

   - The function must be continuous in the selected interval.
   - The starting interval must have opposite signs at its ends.
   - Always calculate the midpoint.
   - Keep the half-interval where the sign changes.
   - Repeat until the required accuracy is reached.
   - Stop if the maximum iteration count is reached.
   - Bisection finds a root inside the selected interval,
     but it does not guarantee finding every root.


10. COMPLETE ALGORITHM IN SIMPLE FORM

    Step 1: Define the function f(x).
    Step 2: Choose lower limit a and upper limit b.
    Step 3: Check whether f(a) and f(b) have opposite signs.
    Step 4: Calculate midpoint c = (a + b) / 2.
    Step 5: Check whether c is the root.
    Step 6: Select the half-interval containing the root.
    Step 7: Check the tolerance.
    Step 8: Repeat until the answer is accurate enough.
    Step 9: Return the approximate root.
"""


