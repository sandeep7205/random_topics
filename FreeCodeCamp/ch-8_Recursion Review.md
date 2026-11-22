# Recursion Review

## 1. Recursion

**Recursion** is a technique in which a function calls itself. Each call works on a smaller version of the original problem until it reaches a **base case** that stops further recursive calls.

## 2. Base Case

The **base case** is the condition that stops recursion.

You should define the base case carefully. Otherwise, the function may keep calling itself until Python raises a `RecursionError`.

## 3. Recursive Case

The **recursive case** is the part of the function that calls itself again with an argument that moves toward the base case.

For example, `number - 1` moves a countdown closer to its stopping condition.

```python
def recursive_countdown(number):
    if number < 1:  # Base case
        return

    print(number)
    recursive_countdown(number - 1)  # Recursive case


recursive_countdown(5)  # Prints 5, 4, 3, 2, 1
```

## 4. Order of Execution

The position of the recursive call determines when the other statements run:

- Code **before** the recursive call runs as the calls go deeper.
- Code **after** the recursive call runs as the calls return.

Moving `print()` after the recursive call makes the function print the numbers in ascending order:

```python
def recursive_countdown(number):
    if number < 1:
        return

    recursive_countdown(number - 1)
    print(number)


recursive_countdown(5)  # Prints 1, 2, 3, 4, 5
```

## 5. Call Stack

The **call stack** is a last-in, first-out (LIFO) data structure Python uses to keep track of active function calls.

Each time a function is called, Python adds a frame for that call to the top of the stack. A frame contains information such as the function's arguments and local variables.

## 6. Resuming Recursive Calls

A function call pauses when it makes a recursive call.

When the base case returns, Python removes that call from the top of the stack. The earlier calls then resume after their recursive calls and return in last-in, first-out order.

```python
def recursive_countdown(number):
    print(f'Function call started for number: {number}')

    if number < 1:
        print('Base case reached')
        return

    print(f'Calling recursive_countdown with number: {number - 1}')
    recursive_countdown(number - 1)

    print(f'Function call completed for number: {number}')


recursive_countdown(3)
```

Output:

```text
Function call started for number: 3
Calling recursive_countdown with number: 2
Function call started for number: 2
Calling recursive_countdown with number: 1
Function call started for number: 1
Calling recursive_countdown with number: 0
Function call started for number: 0
Base case reached
Function call completed for number: 1
Function call completed for number: 2
Function call completed for number: 3
```

The call with `number = 0` reaches the base case and returns first. Then the calls with `1`, `2`, and `3` resume and complete in reverse order.

## 7. Building a List Recursively

Each function call resumes when its recursive call returns. It can then use the value returned by that call.

In the example below:

1. The base case returns an empty list.
2. Each recursive call receives the list returned by the next call.
3. It appends its own number to that list.
4. It returns the updated list.

```python
def countup(number):
    if number < 1:
        return []

    count_list = countup(number - 1)
    count_list.append(number)

    return count_list


print(countup(5))  # [1, 2, 3, 4, 5]
```

For example:

- The call with `number = 0` returns `[]`.
- The call with `number = 1` receives `[]` and returns `[1]`.
- The call with `number = 2` receives `[1]` and returns `[1, 2]`.
- This continues until the call with `number = 5` returns `[1, 2, 3, 4, 5]`.

## 8. Applications of Recursion

Recursion can be used for simple tasks such as:

- Counting down.
- Counting up.
- Building a list of numbers.

It is also useful for problems with an unknown or variable depth, such as traversing a file tree or navigating nested data structures.

## 9. Quick Recap

- **Recursion:** A function calling itself.
- **Base case:** The condition that stops recursion.
- **Recursive case:** The part that calls the function again and moves toward the base case.
- **Call stack:** Tracks active function calls using LIFO order.
- **Going deeper:** Statements before the recursive call execute.
- **Returning:** Statements after the recursive call execute as earlier calls resume.
