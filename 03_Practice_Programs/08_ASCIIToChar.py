"""
Title: Find Character from ASCII Value
Author: Rushikesh Padaki
Date: 10 July 2025

Description:
Finds and displays the character corresponding to a user-provided ASCII value.
- Prompts the user to enter a valid ASCII value (integer).
- Uses the built-in chr() function to find the character associated with the ASCII value.
- Displays the ASCII value along with its corresponding character.

Algorithm:
1. Prompt the user to enter an integer representing the ASCII value.
2. Use the chr() function to find the character corresponding to the entered ASCII value.
3. Display the ASCII value and its corresponding character.

Time Complexity:
- O(1) (Constant time for computation)

Space Complexity:
- O(1) (Constant space usage)

Sample Execution:

Case 1: User enters ASCII value = 65
Output:
Enter a valid ASCII Value: 65
The character associated with the ASCII value '65' is  A

Case 2: User enters ASCII value = 122
Output:
Enter a valid ASCII Value: 122
The character associated with the ASCII value '122' is  z
"""

ascii_value = int(input('Enter a valid ASCII Value: '))

print("The character associated with the ASCII value '" + str(ascii_value) + "' is ", chr(ascii_value))
