"""
Title: Swap Two Numbers Using Tuple Unpacking
Author: Rushikesh Padaki
Date: 10 July 2025

Description:
Swaps the values of two user-provided integers using Python's tuple unpacking.
- Prompts the user to enter values for x and y.
- Displays the values before swapping.
- Swaps the values using tuple unpacking without using a temporary variable.
- Displays the values after swapping.

Algorithm:
1. Prompt the user to enter an integer value for x.
2. Prompt the user to enter an integer value for y.
3. Display the values of x and y before swapping.
4. Swap the values using the statement: x, y = y, x.
5. Display the values of x and y after swapping.

Time Complexity:
- O(1) (Constant time operations)

Space Complexity:
- O(1) (Uses constant additional space internally, no explicit temporary variable)

Sample Execution:

Case 1: User enters x = 7, y = 3
Output:
Enter a value for x: 7
Enter a value for y: 3
Before Swapping:
x =  7
y =  3
After Swapping:
x =  3
y =  7

Case 2: User enters x = -12, y = 9
Output:
Enter a value for x: -12
Enter a value for y: 9
Before Swapping:
x =  -12
y =  9
After Swapping:
x =  9
y =  -12
"""

x = int(input('Enter a value for x: '))
y = int(input('Enter a value for y: '))

print('Before Swapping:')
print('x = ', x)
print('y = ', y)

x, y = y, x

print('After Swapping:')
print('x = ', x)
print('y = ', y)
