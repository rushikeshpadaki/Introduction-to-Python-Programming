"""
Title: Addition of Two User-Input Floating Point Numbers
Author: Rushikesh Padaki
Date: 09 July 2025

Description:
A Python program to add two floating-point numbers entered by the user and display the result.
- Demonstrates taking user input using the input() function.
- Converts string inputs to floating-point numbers using the float() function.
- Performs addition using the '+' operator.
- Displays the formatted output using the print() function with the format() method.

Algorithm:
1. Prompt the user to enter the first number using input() and store it in variable num1.
2. Prompt the user to enter the second number using input() and store it in variable num2.
3. Convert num1 and num2 from string to float using the float() function.
4. Add the two floating-point numbers and store the result in the variable total.
5. Display the formatted result using the print() function and the format() method.

Time Complexity:
- O(1): The program performs a constant-time addition operation.

Space Complexity:
- O(1): The program uses a constant amount of space to store variables.

Sample Execution:

Case 1: Adding two floating-point numbers
Input:
Enter first number: 5.2
Enter second number: 4.8
Output:
The sum of 5.2 and 4.8 is 10.0

Case 2: Adding two integer inputs (converted to float)
Input:
Enter first number: 3
Enter second number: 7
Output:
The sum of 3 and 7 is 10.0
"""

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

total = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, total))
