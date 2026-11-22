
# --------------------------------------------------
# 1. Initialize variables
# --------------------------------------------------

# Store the initial running total
running_total = 0

# Number of friends sharing the bill
num_of_friends = 4


# --------------------------------------------------
# 2. Store the cost of each food category
# --------------------------------------------------

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21


# --------------------------------------------------
# 3. Calculate the total bill
# --------------------------------------------------

# Add the cost of all food and drinks
running_total = appetizers + main_courses + desserts + drinks

print('Total bill so far:', running_total)


# --------------------------------------------------
# 4. Calculate and add the tip
# --------------------------------------------------

# Calculate a 25% tip based on the bill amount
tip = running_total * 0.25

print('Tip amount:', tip)

# Add the tip to the original bill
running_total += tip

print('Total with tip:', running_total)


# --------------------------------------------------
# 5. Split the bill among friends
# --------------------------------------------------

# Divide the total bill equally among all friends
final_bill = running_total / num_of_friends

print('Bill per person:', final_bill)


# --------------------------------------------------
# 6. Round the final amount
# --------------------------------------------------

# Round each person's share to 2 decimal places
each_pays = round(final_bill, 2)

print(f"Each person pays: {each_pays}")
