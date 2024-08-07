#1. WAP to find sum of all odd numbers within the given range.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
sum = 0
for number in range(start, end + 1):
    if number % 2 != 0:
        sum = sum+number
print("The sum of all odd numbers between", start, "and", end, "is:", sum)

#2. WAP to find sum of all even numbers within the given range.
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
sum = 0
for number in range(start, end + 1):
    if number % 2 == 0:
        sum = sum+number
print("The sum of all even numbers between", start, "and", end, "is:", sum)

#3.WAP to calculate cube of all the numbers from 1 to a given number.
number = int(input("Enter the number: "))
for num in range(1, number + 1):
    cube = num ** 3
    print(cube)

#4. WAP to find multiples of 5 in a list
list = [10, 23, 45, 50, 62, 75, 89, 100]
multiples_of_5 = []
for number in list:
    if number % 5 == 0:
        multiples_of_5.append(number) 
print("Multiples of 5 in the list are:", multiples_of_5)

# 5. WAP to find the maximum number in a list.
list = [10, 23, 45, 67, 89, 12, 34]
number = max(list)
print("The maximum number in the list is:", number)

# or 
list = [10, 23, 45, 67, 89, 12, 34]
number = list[0]
for i in list:
    if i > number:
        number = i
print("The maximum number in the list is:", number)

# 6. WAP to find the minimum number in a list.
list = [10, 23, 45, 67, 89, 12, 34]
number = min(list)
print("The minimum number in the list is:",number)

# or
list = [10, 23, 45, 67, 89, 12, 34]
number = list[0]
for i in list:
    if i < number:
        number = i
print("The minimum number in the list is:", number)

# 7. WAP to print multiples of 3 using range() function.
start = 3
end = 100  
for num in range(start, end + 1, 3):
    print(num)
