



"""
=========================================================
PYTHON CERTIFICATION
LAB: IMPLEMENT THE TOWER OF HANOI ALGORITHM
=========================================================

PROBLEM DESCRIPTION:
--------------------
Tower of Hanoi is a mathematical puzzle consisting of:
- Three rods: Start, Auxiliary, Destination.
- N disks of different sizes.
- Initially, all disks are stacked on the Start rod.
- The largest disk is at the bottom.
- The smallest disk is at the top.

GOAL:
-----
Move all disks from the Start rod to the Destination rod.

RULES:
------
1. Move only one disk at a time.
2. Only the top-most disk can be moved.
3. A larger disk cannot be placed on a smaller disk.

OBJECTIVE:
----------
Implement a function named hanoi_solver(n).

The function must:
1. Accept one integer argument representing the number of disks.
2. Solve the puzzle using recursion.
3. Follow the Tower of Hanoi rules.
4. Return a string containing every arrangement.
5. Include the initial arrangement.
6. Put each arrangement on a new line.

MATHEMATICAL FORMULA:
---------------------
Minimum number of moves = 2^n - 1

Examples:
n = 1  ->  1 move
n = 2  ->  3 moves
n = 3  ->  7 moves
n = 4  ->  15 moves
n = 5  ->  31 moves

CORE RECURSIVE LOGIC:
--------------------
To move n disks from Source to Destination:

1. Move n-1 disks from Source to Auxiliary.
2. Move the largest remaining disk from Source to Destination.
3. Move n-1 disks from Auxiliary to Destination.

BASE CASE:
----------
If n <= 0:
    Return without performing any move.

INITIAL ARRANGEMENT:
--------------------
For n = 3:

Start       Auxiliary       Destination

[3, 2, 1]      []                []

EXPECTED OUTPUT:
----------------
[3, 2, 1] [] []
[3, 2] [] [1]
[3] [2] [1]
[3] [2, 1] []
[] [2, 1] [3]
[1] [2] [3]
[1] [] [3, 2]
[] [] [3, 2, 1]

IMPORTANT IMPLEMENTATION DETAILS:
---------------------------------
- Use a list to represent each rod.
- Use list.pop() to remove the top disk.
- Use list.append() to place a disk on another rod.
- Record the arrangement after every move.
- Use str() to convert rod lists into strings.
- Use "\n".join() to combine all arrangements.
- Return the final string.

FUNCTION SIGNATURE:
-------------------
def hanoi_solver(n):

    # Initialize the three rods

    # Store the initial arrangement

    # Define the recursive function

    # Perform recursive disk movements

    # Return all recorded arrangements as a string

=========================================================
"""




def hanoi_solver(disk):

    # Step 1: Create the three rods.
    # The first rod contains all disks, arranged from largest to smallest.
    start = list(range(disk, 0, -1))
    mid = []
    end = []

    # Step 2: Store the initial arrangement and all subsequent moves.
    moves = []
    moves.append(f"{start} {mid} {end}")

    # Step 3: Define a recursive function to move disks.
    def move_disks(n, source, auxiliary, destination):

        # Base case: No disks left to move.
        if n <= 0:
            return

        # Step 4: Move the top n-1 disks from source to auxiliary.
        move_disks(n - 1, source, destination, auxiliary)

        # Step 5: Move the largest remaining disk to destination.
        destination.append(source.pop())

        # Record the current arrangement of all three rods.
        moves.append(f"{start} {mid} {end}")

        # Step 6: Move the n-1 disks from auxiliary to destination.
        move_disks(n - 1, auxiliary, source, destination)

    # Step 7: Start solving the puzzle.
    move_disks(disk, start, mid, end)

    # Step 8: Return all arrangements as a single string.
    return "\n".join(moves)

print(hanoi_solver(2))
print("----------------")
print(hanoi_solver(3))