
# --------------------------------------------------
# 1. Employee name and address
# --------------------------------------------------

first_name = 'John'
last_name = 'Doe'

# Combine first name and last name with a space
full_name = first_name + ' ' + last_name

# Create an address and append apartment details
address = '123 Main Street'
address += ', Apartment 4B'


# --------------------------------------------------
# 2. Employee age and personal information
# --------------------------------------------------

employee_age = 28

# Convert the integer age into a string before concatenating
employee_info = full_name + ' is ' + str(employee_age) + ' years old'

print(employee_info)


# --------------------------------------------------
# 3. Employee experience
# --------------------------------------------------

years_experience = 5
experience_years = 5

# Convert experience into a string and build an information message
experience_info = 'Experience: ' + str(experience_years) + ' years'

print(experience_info)


# --------------------------------------------------
# 4. Employee position and salary
# --------------------------------------------------

position = 'Data Analyst'
salary = 75000

# Use an f-string to combine variables and text easily
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'

print(employee_card)


# --------------------------------------------------
# 5. Extract information from employee code
# --------------------------------------------------

employee_code = 'DEV-2026-JD-001'

# Extract the department code (characters at index 0 to 2)
department = employee_code[0:3]
print(department)

# Extract the year code (characters at index 4 to 7)
year_code = employee_code[4:8]
print(year_code)

# Extract employee initials (characters at index 9 to 10)
initials = employee_code[9:11]
print(initials)

# Extract the last three characters using negative indexing
last_three = employee_code[-3:]
print(last_three)
