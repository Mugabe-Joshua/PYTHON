# my_name = input("Enter your name: ")
# print(type(my_name))
# my_age = input(int('Enter your age: '))
# print(type(my_age))
# my_weight = input(float("Enter your weight: "))
# print(type(my_weight))
# my_height = input(float("Enter your height: "))
# print(type(my_height))

my_name = "Joshua"
my_age = 25
my_weight = 68.2
my_height = 172.5
is_male = True
print(type(my_name))
print(type(my_age))
print(type(my_weight))
print(type(my_height))
print(type(is_male))
#ASSIGNMENT COMPLETE! :)

my_first_friend, my_second_friend, my_third_friend = "Hakim", "Aaron", "Eliot"
print(my_first_friend)
print(my_second_friend)
print(my_third_friend)

# my_first_friend, my_second_friend, my_third_friend = "Hakim", "Aaron", #"Eliot" I have removed the value of my_third_friend thus resulting in an error.
# print(my_first_friend)
# print(my_second_friend)
# print(my_third_friend)

#ASSIGNING A VALUE TO A VARIETY OF VARIABLES
my_name = "Joshua"
my_sister = "Joshua"
my_brother = "Joshua"
print(my_name)
print(my_brother)
print(my_sister)

my_sis = my_sibling = my_sister = "Jude"    #Assigning the same value to multiple variables
print(my_sis)
print(my_sibling)
print(my_sister)

#Escape Characters
statement = "Joshua's mother is a good woman.:)"
print(statement)

statement = "Joshua\'s mother is a good woman.:)"
print(statement)

#Research complex numbers and how to represent them in python
#Complex numbers are represented in python using the letter 'j' to represent the imaginary part of the complex number.
complex_number = 3 + 4j
print(complex_number)
print(type(complex_number))

#OPERATORS:

#Arithmetic operators
#Addition
num1 = 10
num2 = 5
result = num1 + num2
print(result)

#Subtraction
result = num1 - num2
print(result)

#Multiplication
result = num1 * num2
print(result)

#Division
result = num1 / num2
print(result)

#Modulus
result = num1 % num2
print(result)

#Exponentiation
result = num1 ** num2
print(result)

#Floor Division
result = num1 // num2
print(result)

#Comparison Operators
#Equal to
result = num1 == num2
print(result)

#Not equal to
result = num1 != num2
print(result)

#Greater than
result = num1 > num2
print(result)

#Less than
result = num1 < num2
print(result)

#Greater than or equal to
result = num1 >= num2
print(result)

#Less than or equal to
result = num1 <= num2
print(result)

#Logical Operators
#AND
num3 = 15
result = num1 > num2 and num1 < num3
print(result)

#OR
result = num1 > num2 or num1 < num3
print(result)

#NOT
result = not(num1 > num2 and num1 < num3)
print(result)

#Identity Operators
#IS
result = num1 is num2
print(result)

#IS NOT
result = num1 is not num2
print(result)

#Membership Operators
#IN
my_list = [1, 2, 3, 4, 5]
result = 3 in my_list
print(result)

#NOT IN
result = 3 not in my_list
print(result)

#Bitwise Operators
#AND
result = num1 & num2
print(result)

#OR
result = num1 | num2
print(result)

#XOR
result = num1 ^ num2
print(result)

#NOT  
result = ~num1
print(result)

#LEFT SHIFT
result = num1 << num2
print(result)