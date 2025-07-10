"""
Title: Calculate Area of a Circle
Author: Rushikesh Padaki
Date: 10 July 2025

Description:
Calculates the area of a circle based on the radius provided by the user.
- Prompts the user to enter the radius of the circle in centimeters.
- Calculates the area using the formula: area = π * r^2
- Displays the area of the circle with six decimal places in sq.cm.

Algorithm:
1. Prompt the user to enter the radius of the circle.
2. Convert the radius input to a floating-point number.
3. Calculate the area using the formula area = π * radius^2.
4. Display the calculated area formatted to six decimal places.

Time Complexity:
- O(1) (Constant time for computation)

Space Complexity:
- O(1) (Constant space usage)

Sample Execution:

Case 1: User enters radius = 5
Output:
Enter the radius of the circle (in cm): 5
Area of the circle = 78.539816 sq.cm

Case 2: User enters radius = 3.2
Output:
Enter the radius of the circle (in cm): 3.2
Area of the circle = 32.169909 sq.cm
"""

import math

radius = input('Enter the radius of the circle (in cm): ')

area = math.pi * pow(float(radius), 2)

print('Area of the circle = %.6f sq.cm' % area)
