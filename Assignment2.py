# # Print output as 5@10@9
# print("5@10@9")

# #  Write a program to compute simple and compound interest.
# # principal = float(input("Enter the principal amount: "))
# # rate = float(input("Enter the rate of interest: "))
# # time = float(input("Enter the time: "))
# # simple_interest = (principal * rate * time) / 100
# # n = int(input("Enter the number of times interest is compounded per year: "))
# # compound_interest = principal * (1 + rate / (100 * n))**(n * time) - principal
# # print("Simple Interest",simple_interest)
# # print("Compound Interest",compound_interest)

# # Write a program to read three numbers in three variables and swap
# # first two variables with the sums of first and second, second and
# # third numbers respectively.

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# a, b = a + b, b + c
# print(a,b,c)

# # WAP to show escape sequences.
# #new line \n
# print("new \n line ")
# #tab \t
# print("Tab\ttab")
# #Backslash \\
# print("hello\\backslash is here")
# #SIngle quotation
# print("Hello \' world")
# #Double quote
# print("\"Hello, world!\"")
# #backspace
# print("hello\b")

# Write a program to read today’s date from user. Then display how
# many days are left in the current month.
# from calendar import monthrange

# # Input today's date
# year = int(input("Enter the current year: "))
# month = int(input("Enter the current month (1-12): "))
# day = int(input("Enter today's day (1-31): "))

# days_in_month = monthrange(year, month)[1]  # Get the second element of the tuple
# days_left = days_in_month - day

# print(days_left)

# WAP to show all the keywords available in python.
import keyword
keywords = keyword.kwlist
print(keywords)

# Print the imaginary part out of 2+3j and obtain conjugate of 4+2j
complex_num1 = 2 + 3j
complex_num2 = 4 + 2j
print("The imaginary part of", complex_num1, "is", complex_num1.imag)
print("The conjugate of", complex_num2, "is", complex_num2.conjugate())

