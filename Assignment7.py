# 1. WAP TO PRINT REVERSED LIST [USE REVERSED() FUNCTION AND FOR
# LOOP OR USE LEN() FUNCTION AND FOR LOOP]
# [var=reversed(name of list)]
# WAP to display elements present at odd index in a list

# [USE REVERSED() FUNCTION AND FOR LOOP
input_list = input("Enter the elements ").split()
input_list = [int(element) for element in input_list]
print("Reversed list using reversed() function:")
for item in reversed(input_list):
    print(item, end=" ")
print()  
# USE LEN() FUNCTION AND FOR LOOP]
input_list = input("Enter the elements").split()
input_list = [int(element) for element in input_list]
print("Reversed list using len() function:")
for i in range(len(input_list) - 1, -1, -1):
    print(input_list[i], end=" ")
print() 

# WAP to display elements present at odd index in a list
input_list = input("Enter the elements of the list separated by spaces: ").split()
input_list = [int(element) for element in input_list]
print("Elements at odd indices are:")
for index in range(len(input_list)):
    if index % 2 != 0: 
        print(input_list[index])


# WAP to input a digit and print it in words.
digit_to_word = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
digit = input("Enter a digit: ")
if digit.isdigit() and 0 <= int(digit) <= 9:
    print("The digit", digit, "in words is:", digit_to_word[int(digit)])
else:
    print("Invalid input!")

# WAP to print first n odd numbers in descending order.

n = int(input("Enter the value of n: "))
odd = 2 * n - 1
for i in range(n):
    print(odd - 2 * i, end=", " if i < n - 1 else "\n")


# 5. WAP to print the following series:
# a. 1,4,7,10............40

num = 1
while num <= 40:
    print(num, end=", " if num < 40 else "\n")
    num = num+3

# b. 1,-4,7,-10.............-40

num = 1
sign = 1
while (num) <= 40:
    print(sign * num, end=", " if (num) < 40 else "\n")
    num = num+3
    sign = sign*-1

# WAP to print every integer between 1 and n divisible by m. Also report
# whether the number is divisible by m is even or odd.

n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

for i in range(1, n + 1):
    if i % m == 0:
        if i % 2 == 0:
            print(i,"is divisible by ",m,"and  is even")
        else:
            print(i,"is not divisible by ",m,"and  is odd")

