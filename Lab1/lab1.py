#1- Write a Python program which accepts the user's first and last name and print them inreverse order with a space between them.
# first_name=input("Enter Your First Name:")
# last_name=input("Enter Your Last Name:")
# full_name = last_name[::-1] + " " + first_name[::-1]
# print(full_name)

#2- Write a Python program that accepts an integer (n) and computes the value ofn+nn+nnn.
# n=int(input("Enter number: "))
# nn = int(str(n) + str(n))
# nnn = int(str(n) + str(n) + str(n))
# result = n + nn + nnn
# print(f"Expected Result {result}")

#3- Write a Python program to print the following here document.
# doc="""Sample string ​:
# a string that you "don't" have to escape
# Thisis a ....... multi-line
# heredoc string --------> example"""
# print(doc)

#4- Write a Python program to get the volume of a sphere with radius 6.
# import math
# r=6
# V = (4/3) * math.pi * math.pow(r,3)
# print(f"The volume of a sphere with radius {r} is {V}")

#5- Write a Python program that will accept the base and height of a triangle and computethe area.
# height=float(input("Enter Height of a Triangle: "))
# base=float(input("Enter a Base of a Triangle: "))
# area=0.5*height*base
# print(f"The area of the triangle is: {area}")

#6- Write a Python program to construct the following pattern, using a nested for loop.
# for i in range(5):
#     for j in range(i+1):
#         print("*", end="") #end="". This ensures that the asterisks are printed on the same line without any whitespace between them.
#     print()
    
# for i in range(4, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()

#7- Write a Python program that accepts a word from the user and reverse it.
# word=input("Enter word: ")
# print(word[::-1])

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
# for i in range(7):
#     if i==3 or i==6:
#         continue
#     print(i)

#9- Write a Python program to get the Fibonacci series between 0 to 50
# a, b = 0, 1
# while b <= 50:
#     print(b,end=" ")
#     a, b = b, a + b

#10- Write a Python program that accepts a string and calculate the number of digits andletters. 
# def count_digits(s):
#     count_digit=count_letter = 0
#     for char in s:
#         if char.isdigit():
#             count_digit += 1
#         elif char.isalpha():
#             count_letter +=1
#     print(f"Number of digits in string is {count_digit} and Number of Letters is {count_letter}")

# s = input("Enter Your String: ")
# count_digits(s)   # prints 9