# 1. WAP TO PRINT A TABLE OF A NUMBER
num=8
for i in range(1, 11):
    print(num , " * " , i , " = " , num * i)
# 2. WAP TO TAKE INPUT FROM USER AND PRINT THE TABLE OF A NUMBER.
num = int(input("Enter a number to print its table: "))
for i in range(1, 11):
    print(num , " * " , i , " = " , num * i)

# 3. WAP TO PRINT FIBONACCI SERIES FROM 1 TO 50.
a, b = 0, 1
print("Fibonacci series from 1 to 50:")
while a <= 50:
    if a >= 1:
        print(a, end=" ")
    a, b = b, a + b

# 5. FIND THE SUM OF FIRST 10 EVEN NUMBERS.
n = 10
sum = n * (n + 1)
print("The sum of the first 10 even numbers is:", sum)

# 6. FIND THE SUM OF FIRST 10 ODD NUMBERS
n = 10
sum = n * n
print("The sum of the first 10 odd numbers is:", sum)

# 7. FIND THE SUM OF ALL ELEMENTS OF A LIST.
numbers = [10, 20, 30, 40, 50]  
sum=0
for num in numbers:
    sum = sum+num
print("The sum of all elements in the list is:", sum)

# 8.PROGRAM TO COUTN TOTAL NUMBER OF DIGITS IN A NUMBER
number = int(input("Enter a number: "))
count = 0
if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10
        count += 1
print("The total number of digits in the number is:", count)

# 9.PROGRAM TO SHOW ALL THE ELEMENTS OF A LIST.
list = [1, 2, 3, 4, 5]
print("The elements of the list are:")
for element in list:
    print(element)

# 10.Python program to count the number of even and odd numbers from a
# list.
list = [10, 20, 30, 53, 22, 72, 99]
even = 0
odd = 0
for number in list:
    if number % 2 == 0:
        even = even+1  
    else:
        odd = odd+ 1  
print("Total number of even numbers:", even)
print("Total number of odd numbers:", odd)
