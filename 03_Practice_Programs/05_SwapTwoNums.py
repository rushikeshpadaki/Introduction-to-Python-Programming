"""
Title: Swap Two Numbers
Author: Rushikesh Padaki
Date: 10 July 2025

Description:
Swaps the values of two user-provided integers.
- Prompts the user to enter values for x and y.
- Displays the values before swapping.
- Swaps the values using a temporary variable.
- Displays the values after swapping.

Algorithm:
1. Prompt the user to enter an integer value for x.
2. Prompt the user to enter an integer value for y.
3. Display the values of x and y before swapping.
4. Store the value of x in a temporary variable.
5. Assign the value of y to x.
6. Assign the value stored in the temporary variable to y.
7. Display the values of x and y after swapping.

Time Complexity:
- O(1) (Constant time operations)

Space Complexity:
- O(1) (Uses constant additional space for a temporary variable)

Sample Execution:

Case 1: User enters x = 10, y = 20
Output:
Enter a value for x: 10
Enter a value for y: 20
Before Swapping:
x =  10
y =  20
After Swapping:
x =  20
y =  10

Case 2: User enters x = -5, y = 15
Output:
Enter a value for x: -5
Enter a value for y: 15
Before Swapping:
x =  -5
y =  15
After Swapping:
x =  15
y =  -5
"""

x = int(input('Enter a value for x: '))
y = int(input('Enter a value for y: '))

print('Before Swapping:')
print('x = ', x)
print('y = ', y)

temp = x
x = y
y = temp

print('After Swapping:')
print('x = ', x)
print('y = ', y)
