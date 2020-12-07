'''
-------------------------------------------------------------------------------
Name:		problem2.py
Purpose:	Calculating chicken pieces to be distributed evenly among students in Mr.Fabroa's class and giving the remainder to Mr.Fabroa.

Author: Soon Fah.M

Created:	date in 12/07/2020
------------------------------------------------------------------------------
'''

# input for the amount of chicken and the amount of students to calculate for 
num_classmates = int(input("How many people are there in the class? (not including Mr.Fabroa): "))

num_chicken = int(input("What is the number of chicken pieces: "))

# calculating the amount of chicken everyone gets
c_student_og = num_chicken / num_classmates
c_teach = num_chicken % num_classmates
c_student = c_student_og - c_teach

# the result number of pieces for everyone
print("There will be " + str(c_student) + " chicken pieces per student.")
print("There will be " + str(c_teach) + " pieces of chicken for Mr.Fabroa.")