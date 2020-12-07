'''
-------------------------------------------------------------------------------
Name:		problem1.py
Purpose:	It converts the tempurature in celsius to be read in fahrenheit.

Author:	Soon Fah.M

Created:	date in 12/07/2020
------------------------------------------------------------------------------
'''


# input for celsius
c_Temp = float(input("Please input the tempurature in celsius: "))

# converts celsius to fahrenheit
f_Temp = float(c_Temp) * 9 / 5 + 32

# prints the outcome telling the tempurature
print("Your current tempurature is " + str(f_Temp) + " degrees fahrenheit.")