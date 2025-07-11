"""
Title: Word Removal from Text
Author: Rushikesh Padaki
Date: 11 July 2025

Description:
This program removes all occurrences of a specified word from the input text provided by the user.
- The user is prompted to enter a block of text.
- The user is then prompted to enter a word that they wish to remove from the entered text.
- The program uses the 'replace()' method to remove all exact matches of the specified word from the text.
- The resulting text is displayed after the removal.

Algorithm:
1. Prompt the user to enter a block of text.
2. Prompt the user to enter the word to be removed from the text.
3. Use the 'replace()' function to replace the specified word with an empty string.
4. Display the updated text after the word removal.

Time Complexity:
- O(N) where N is the length of the text.

Space Complexity:
- O(N) for storing the text after replacement.

Sample Execution:

Case 1: Removing a word
Input:
Enter some text: 
I like to code in Python because Python is powerful.
Enter a word to be removed from the text: 
Python
Output:
Text after word replacement: I like to code in  because  is powerful.

Case 2: Removing a word not present
Input:
Enter some text: 
Welcome to programming.
Enter a word to be removed from the text: 
Python
Output:
Text after word replacement: Welcome to programming.
"""

print('Enter some text: ')
text = input()

print('Enter a word to be removed from the text: ')
word = input()

text = text.replace(word, '')

print('Text after word replacement: ' + text)
