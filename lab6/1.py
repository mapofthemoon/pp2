#Python builtin functions exercises

#Write a Python program with builtin function to multiply 
#all the numbers in a list Write a Python program with builtin function that accepts a string and calculate the 
#of upper case letters and lower case letters Write a Python program with builtin function that checks whether 
#a passed string is palindrome or not. Write a Python program that invoke square root function after specific 
#milliseconds. Sample Input: 25100 2123 Sample Output: Square root of 25100 after 2123 miliseconds is
#158.42979517754858 Write a Python program with builtin function that returns True if all elements of the tuple are 
#true. 

import math
n = int(input("Input the size of the list:"))
print("Input the elements of the list")
data = input().split()
list = []
for i in range(n):
    a = int(data[i])
    list.append(a)
result = math.prod(list)
print("The product of list elements:", result)
