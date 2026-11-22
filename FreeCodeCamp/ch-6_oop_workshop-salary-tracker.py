
class Employee:
    """
    Represents an employee with a name, job level, and salary.
    Validates employee details and manages salary and promotions.
    """

    # Class variable: Stores the minimum salary for each employee level
    _base_salaries = {
        'trainee': 1000,
        'junior': 2000,
        'mid-level': 3000,
        'senior': 4000,
    }

    def __init__(self, name, level):
        """Initialize an employee with a name and job level."""

        # Make sure name and level are strings
        if not (isinstance(name, str) and isinstance(level, str)):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")

        # Check whether the given level exists in the salary dictionary
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")

        # Store employee details using private attributes
        self._name = name
        self._level = level

        # Set the starting salary based on the employee's level
        self._salary = Employee._base_salaries[level]

    def __str__(self):
        """Return a user-friendly string representation of the employee."""
        return f'{self.name}: {self.level}'

    def __repr__(self):
        """Return a developer-friendly representation of the employee."""
        return f"Employee('{self.name}', '{self.level}')"

    @property
    def name(self):
        """Get the employee's name."""
        return self._name

    @name.setter
    def name(self, new_name):
        """Update the employee's name after validating its type."""

        # Make sure the new name is a string
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")

        # Update the employee's name
        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    @property
    def level(self):
        """Get the employee's current job level."""
        return self._level

    @level.setter
    def level(self, new_level):
        """Promote the employee to a higher level and update their salary."""

        # Check whether the new level is valid
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")

        # Prevent selecting the same level again
        if new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")

        # Prevent an employee from moving to a lower level
        if Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError("Cannot change to lower level.")

        # Display the promotion message
        print(f"'{self.name}' promoted to '{new_level}'.")

        # Update the employee's salary based on the new level
        self.salary = Employee._base_salaries[new_level]

        # Update the employee's job level
        self._level = new_level

    @property
    def salary(self):
        """Get the employee's current salary."""
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        """Update the salary after checking its type and minimum value."""

        # Make sure the salary is a number
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")

        # Salary must be greater than the minimum salary for the current level
        if new_salary <= Employee._base_salaries[self.level]:
            raise ValueError(
                f'Salary must be higher than minimum salary '
                f'${Employee._base_salaries[self.level]}.'
            )

        # Update the employee's salary
        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')


# Create an employee with the name Charlie Brown and trainee level
charlie_brown = Employee('Charlie Brown', 'trainee')

# Display the employee's name and level using __str__()
print(charlie_brown)

# Display the employee's current salary
print(f'Base salary: ${charlie_brown.salary}')

# Promote the employee from trainee to junior
# The salary is automatically updated based on the new level
charlie_brown.level = 'junior'
