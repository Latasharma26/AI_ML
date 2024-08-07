# WAP to accept a number from 1 to 7 and display the name of day like 1
# for Sunday, 2 for Monday and so on.
day_number = int(input("Enter a number from 1 to 7: "))
if day_number == 1:
    print("Sunday")
elif day_number == 2:
    print("Monday")
elif day_number == 3:
    print("Tuesday")
elif day_number == 4:
    print("Wednesday")
elif day_number == 5:
    print("Thursday")
elif day_number == 6:
    print("Friday")
elif day_number == 7:
    print("Saturday")
else:
    print("Invalid input ")

# WAP to accept a number from 1 to 12 and display the month and days
# in that month
month_number = int(input("Enter a number from 1 to 12: "))

if month_number == 1:
    print("January has 31 days.")
elif month_number == 2:
    print("February has 28 or 29 days depending on whether it's a leap year.")
elif month_number == 3:
    print("March has 31 days.")
elif month_number == 4:
    print("April has 30 days.")
elif month_number == 5:
    print("May has 31 days.")
elif month_number == 6:
    print("June has 30 days.")
elif month_number == 7:
    print("July has 31 days.")
elif month_number == 8:
    print("August has 31 days.")
elif month_number == 9:
    print("September has 30 days.")
elif month_number == 10:
    print("October has 31 days.")
elif month_number == 11:
    print("November has 30 days.")
elif month_number == 12:
    print("December has 31 days.")
else:
    print("Invalid input")

# WAP to check whether the number entered is 3 digit number or
# not.(len())
num = input("Enter a number: ")
if num.isdigit() and len(num) == 3:
    print("The number is a three-digit number.")
else:
    print("The number is not a three-digit number.")

# WAP to check whether a person is senior citizen or not.
age = int(input("Enter the age of the person: "))
if age >= 65:
    print("The person is a senior citizen.")
else:
    print("The person is not a senior citizen.")

# WAP to check whether the number entered by user is positive or
# negative.
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# WAP to check whether a number is divisible by both 2 and 3.

num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("The number is divisible by both 2 and 3.")
else:
    print("The number is not divisible by both 2 and 3.")


# WAP to find largest out of 3 numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print("The largest number is:", largest)


# WAP to check whether a number is prime number or not.
num = int(input("Enter a number: "))
if num > 1:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
else:
    print(num, "is not a prime number.")


# WAP to check a character is vowel or not.
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(char, "is a vowel.")
else:
    print(char, "is not a vowel.")


# Accept the following from user and calculate the percentage of class
# attended :
# a. Total number of working days.
# b. Total number of days for absent.
# After calculating the attendance shows that, if the percentage is
# less than 75%, then student will not be able to sit in the exam.
total_days = int(input("Enter the total number of working days: "))
absent_days = int(input("Enter the total number of days absent: "))
if total_days <= 0:
    print("Total number of working days must be greater than 0.")
else:
    attended_days = total_days - absent_days
    attendance_percentage = (attended_days / total_days) * 100

    
print("Attendance Percentage:", round(attendance_percentage, 2), "%")
if attendance_percentage < 75:
        print("The student will not be able to sit in the exam.")
else:
        print("The student is eligible to sit in the exam.")


# Accept 3 sides of triangle and check whether the triangle is equilateral,
# isosceles or scalene triangle.
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

if (side1 + side2 > side3) and (side2 + side3 > side1) and (side1 + side3 > side2):
    if side1 == side2 == side3:
        print("The triangle is equilateral.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print("The triangle is isosceles.")
    else:
        print("The triangle is scalene.")
else:
    print("The given sides do not form a valid triangle.")


# WAP that inputs 3 numbers and calculates two sums as per the
# following conditions :
# a. Sum1 as the sum of all input numbers.
# b. Sum2 as the sum of non-duplicate numbers; ignore duplicate
# numbers
# (HINT: I/P of numbers 2, 3, 3 will give sum1=8 and sum2=2)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
sum1 = num1 + num2 + num3

nums = [num1, num2, num3]
sum2 = 0
for num in nums:
    if nums.count(num) == 1:
        sum2 = sum2+num
print("Sum1 as the sum of all input numbers",sum1)
print("Sum2 as the sum of non-duplicate numbers",sum2)

# WAP that reads two numbers and arithmetic operator and displays the
# computed result.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an arithmetic operator ")
if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operator."

# WAP to print whether a given character is an uppercase or a lowercase
# character or a digit or any other character.
char = input("Enter a single character: ")
if char.isupper():
    print("The character " ,char , " is an uppercase letter.")
elif char.islower():
    print("The character " , char ," is a lowercase letter.")
elif char.isdigit():
    print("The character " ,char , " is a digit.")
else:
    print("The character " , char , " is a special character.")

# A store charges Rs 120 per item, if you buy less than 10 items. If you buy
# between 10 and 99 items, the cost is Rs. 100 per item. If you buy 100 or
# more items, the cost is Rs. 70 per item. WAP that asks the user how
# many items they have purchased and calculates the total cost.
num_items = int(input("Enter the number of items purchased: "))
if num_items < 10:
    cost_per_item = 120
elif 10 <= num_items < 100:
    cost_per_item = 100
else:
    cost_per_item = 70
total_cost = num_items * cost_per_item
print("The total cost for", num_items, "items is Rs.", total_cost)
