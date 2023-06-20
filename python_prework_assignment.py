#Python Prework Assignment

#Question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
def hello_name(user_name):
    """Display a customized greeting message to user"""
    print(f"Hello {user_name}!")

#Calling the function
hello_name("USERNAME")
hello_name('Javier')


#Question 2
#Write a function, first_odds that prints the odd numbers from 1-100 and returns nothing.
def first_odds():
    """Print odds numbers from 1-100"""
    number = 1
    while number <= 100:
        if number % 2 == 0:
            number += 1
        else:
            print(number)
            number += 1

#Calling function
first_odds()

#Another example
def first_odds():
    """Print odds numbers from 1-100"""
    for number in range (1, 101, 2):
        print(number)

#Calling function
first_odds()


#Question 3 
#write a function, max_num_in_list to return the max number of a given list.
def max_num_in_list(a_list):
    """Return the max number of a given list"""
    max_number = a_list[0]
    for number in a_list:
        if number > max_number:
            max_number = number
    return max_number

#Calling function
my_list = [9, 4, 7, 1]
print(max_num_in_list(my_list))
print(max_num_in_list([23, 34, 56, 42]))


#Question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, 
#but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).
def leap_year(year):
    """Return if the given year is a leap year or not."""
    if (year % 400 == 0) and (year % 100 == 0):
        leap = True
    elif (year % 4 == 0) and (year % 100 != 0):
        leap = True   
    else:
        leap = False
    print(leap) 

#Calling function
leap_year(4200)
leap_year(2024)
leap_year(2023)


#Questiom 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
#The return should be boolean Type.
def is_consecutive (a_list):
    """Check if the numbers on a list are consecutive or not."""
    next_num = a_list[1] 
    for number in a_list:
        if number +1 == next_num:
            next_num += 1
            return True
        else:
            return False
    # print(return)

#Calling Fuction
print(is_consecutive([7, 8, 9]))
print(is_consecutive([101, 102, 103]))
print(is_consecutive([27, 29, 31]))
