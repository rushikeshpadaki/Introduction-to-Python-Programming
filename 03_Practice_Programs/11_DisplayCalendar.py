"""
Title: Display Calendar of a Given Month and Year
Author: Rushikesh Padaki
Date: 11 July 2025

Description:
This program displays the calendar of a specific month and year entered by the user.
- The user is prompted to enter the year as an integer.
- The user is prompted to enter the month as an integer (1-12).
- The program uses Python's built-in 'calendar' module to generate and display the month's calendar in a formatted text layout.

Algorithm:
1. Import the 'calendar' module.
2. Prompt the user to enter the year and convert it to an integer.
3. Prompt the user to enter the month and convert it to an integer.
4. Use 'calendar.month(year, month)' to get the string representation of the month's calendar.
5. Print the generated calendar.

Time Complexity:
- O(1) (calendar generation is direct without iterations based on input size)

Space Complexity:
- O(1) (fixed memory usage for calendar display)

Sample Execution:

Case 1: Display July 2025
Input:
Enter year: 
2025
Enter month: 
7
Output:
      July 2025
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

Case 2: Display February 2024 (leap year)
Input:
Enter year:
2024
Enter month:
2
Output:
   February 2024
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29

"""

import calendar

year = int(input('Enter year: '))
mon = int(input('Enter month: '))

print(calendar.month(year, mon))
