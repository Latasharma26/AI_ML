# WAP to take input from user and evaluate the number of seconds. (Hint:
# Take today’s day and time as input. No need to take whole date as
# input.)
hours = int(input("Enter hour : "))
minutes = int(input("Enter minute : "))
seconds = int(input("Enter second : "))
total_seconds = hours * 3600 + minutes * 60 + seconds
print("Total seconds from the start of the day:", total_seconds)

# WAP to take your height (in cm) as input and convert your height into
# feet and inches. (Hint: 1 foot=12 inches,1 inch=2.54 cm)
height_cm = float(input("Enter your height in cm: "))
height_inches = height_cm / 2.54
feet = int(height_inches // 12)
inches = round(height_inches % 12)
print("feet ",feet, "inches ",inches)

# WAP to read a number n and print n 2 ,n 3 ,n 4
n = int(input("Enter a number: "))
print(n**2, n**3, n**4)

# WAP to obtain x, y, z from user and calculate the expression
# 4x 4 +3y 3 9z+6π
x = float(input("Enter value for x: "))
y = float(input("Enter value for y: "))
z = float(input("Enter value for z: "))
pi = 3.14
result = 4 * (x ** 4) + 3 * (y ** 3) - 9 * z + 6 * pi
print(" result is:", result)


# WAP to take a 2 digit number and then print the reversed number.

num = int(input("Enter a two-digit number: "))
tens = num // 10
ones = num % 10
reversed_num = ones * 10 + tens
print("Reversed number:", reversed_num)


# WAP to take a 3 digit number and then print the reversed number.
num = int(input("Enter a three-digit number: "))
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
reversed_num = ones * 100 + tens * 10 + hundreds
print("Reversed number:", reversed_num)

# WAP that reads a number of seconds and prints it in the form of minutes
# and seconds (HINT: 200 seconds are printed as 3 minutes and 20
# seconds).
total_seconds = int(input("Enter the number of seconds: "))
minutes = total_seconds // 60
seconds = total_seconds % 60
print("The time is:", minutes, "minutes and", seconds, "seconds.")

# WAP to take two numbers and print if the first number is fully divisible
# by second number or not.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num2 != 0:
    if num1 % num2 == 0:
        print(num1, "is fully divisible by", num2)
    else:
        print(num1, "is not fully divisible by", num2)
else:
    print("Division by zero is not allowed.")
