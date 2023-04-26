# 1- Given a list of numbers, create a function that returns a list where all similar adjacent elements have been reduced to a single element.
# my_list = [1, 2, 3, 3, 4, 5, 5]

# def remove_duplicate(list):
#     my_new_list = []
#     for ele in list:
#         if (ele not in my_new_list):
#             my_new_list.append(ele)
#     return my_new_list

# print(remove_duplicate(my_list))

# 2- Consider dividing a string into two halves
# import math
# def divide_str(str):
#     if len(str) % 2 == 0:
#         half_length = len(str) // 2            
#     else:
#         half_length = math.ceil(len(str) / 2)
#     first_half = str[:half_length]
#     second_half = str[half_length:]
#     result={
#         "first_half":first_half,
#         "second_half":second_half
#     }
#     return first_half,second_half

# first_str=input("Enter First String : ")
# second_str=input("Enter Second String : ")

# first_front,first_back=divide_str(first_str)
# second_front,second_back=divide_str(second_str)

# print(f"({first_front} + {second_front}) + ({first_back} + {second_back})")


#3- Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

# def check_duplication(list):
#     for i in range(len(list)):
#         for j in range(i+1, len(list)):
#             if list[i] == list[j]:#compare each element in the sequence with every other element that comes after it
#                 return False
#     return True
# print(check_duplication([1, 5, 7, 9]))
# print(check_duplication([1, 5, 7, 1, 9]))

#4- Bubble Sort

# def bubble_sort(list):
#     list_length=len(list)
#     for i in range(list_length):
#         for j in range(list_length-i-1):
#             if list[j] > list[j+1]:
#                 list[j], list[j+1] = list[j+1], list[j]  
#     return list

# print(bubble_sort([64, 34,10,8, 25, 12, 22, 11, 90]))