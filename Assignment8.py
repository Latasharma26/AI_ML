# WAP to accept the age of n employees and count the number of persons
# in the following age group
# a. 26-35
# b. 36-45
# c. 46-55
n = int(input("Enter the number of employees: "))
age_26_35 = 0
age_36_45 = 0
age_46_55 = 0

for i in range(n):
    age = int(input("Enter the age of employee: "))
    if 26 <= age <= 35:
        age_26_35 =  age_26_35 + 1
    elif 36 <= age <= 45:
        age_36_45 = age_36_45+1
    elif 46 <= age <= 55:
        age_46_55 = age_46_55+1

print("Number of employees in age group 26-35:", age_26_35)
print("Number of employees in age group 36-45:", age_36_45)
print("Number of employees in age group 46-55:", age_46_55)
# 2. (You can use while loop in this program)Teacher wants to upload the
# photo of a student on admission portal. The portal has some restrictions
# over the dimensions of the picture that we can upload. Minimum

# dimensions of the picture can be L x L, where L is the length of the side
# of square. The teacher have n photos of various dimensions. Dimension
# of a photo is denoted as W x H, where W is width of the photo and H is
# height of the photo. When any photo is uploaded the following events
# may occur:
# a. If any of the width or height is less than L, User is prompted to
# upload another one. Prints UPLOAD ANOTHER in that case.
# b. If width and height are both large enough
# i. And if photo is already square then print “PHOTO
# ACCEPTED”
# ii. Else user is prompted to crop it and print “CROP IT ”
# (Take L,N,W,H as input)

# Taking the inputs
L = int(input("Enter the minimum dimension L: "))
n = int(input("Enter the number of photos: "))

i = 0

while i < n:
    W = int(input("Enter the width of the photo: "))
    H = int(input("Enter the height of the photo: "))
    
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    else:
        if W == H:
            print("PHOTO ACCEPTED")
        else:
            print("CROP IT")
    
    i += 1


# 3. Write a program to print the following pattern: * * * * * *.
n = 6
for i in range(n):
    print('*', end=' ')
print()

# 4.Write a program to print the following pattern :
# * * *
# * * *
# * * *

n = 3
m = 3
for i in range(n):
    for j in range(m):
        print('*', end=' ')
    print()

# 5 WAP to take a number as input from user and check whether the given
# number is Armstrong number or not.
# (ARMSTRONG NUMBER: Armstrong number is a number that is equal to
# the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407
# are the Armstrong numbers. 317=3**3+1**3+7**3=317)
# (HINT: use str() and len()).

num = int(input("Enter a number: "))
num_str = str(num)
num_len = len(num_str)
sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_len
if sum_of_powers == num:
    print(num," is an Armstrong number.")
else:
    print(num," is not an Armstrong number.")


# 6 WAP to demonstrate for-else and while-else loop.

# for else
numbers = [10, 20, 30, 40]
for num in numbers:
    print(num)
    if num == 3:
        print("Number 3 found, breaking the loop.")
        break
else:
    print("Loop completed without break.")


# while-else
count = 0
while count < 3:
    print(count)
    count += 1
else:
    print("While loop completed normally.")