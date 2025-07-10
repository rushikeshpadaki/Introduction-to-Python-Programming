"""
Title: Find ASCII Equivalent of a Character
Author: Rushikesh Padaki
Date: 10 July 2025

Description:
Finds and displays the ASCII value of a user-provided character.
- Prompts the user to enter a single character.
- Uses the built-in ord() function to find the ASCII value of the entered character.
- Displays the ASCII value along with the entered character.

Algorithm:
1. Prompt the user to enter a single character.
2. Use the ord() function to find the ASCII value of the entered character.
3. Display the character and its corresponding ASCII value.

Time Complexity:
- O(1) (Constant time for computation)

Space Complexity:
- O(1) (Constant space usage)

Sample Execution:

Case 1: User enters character = A
Output:
Enter a character: A
The ASCII equivalent of the character 'A' is  65

Case 2: User enters character = k
Output:
Enter a character: k
The ASCII equivalent of the character 'k' is  107
"""

Character = input('Enter a character: ')

print("The ASCII equivalent of the character '" + Character + "' is ", ord(Character))
