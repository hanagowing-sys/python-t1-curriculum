# Homework Problem 1
# Ask the user for two numbers.
# Print their quotient and remainder on separate lines.
num1 = int(input("choose a number "))
num2 = int(input("choose another number "))
quotient = num1 // num2
remainder = num1 % num2
print(f"Quotient: {quotient}")
print(f"Remainder: {remainder}")

# Homework Problem 2
# Ask the user for their favorite animal and favorite color.
# Print a sentence combining them like: "A blue tiger would be awesome!"
favorite_animal = input("What is your favorite animal? ")
favorite_color = input("What is your favorite color? ")
print(f"A {favorite_color} {favorite_animal} would be awesome!")


# Homework Problem 3
# Use a for loop to print all the even numbers from 0 to 10 (including 10).
for i in range(0, 11, 2):
    print(i)


# Homework Problem 4
# Ask the user how many push-ups they can do.
# Multiply it by 7 and print how many they could do in a week.
pushups = int(input("How many pushups can you do? "))
pushups1 = pushups * 7
print(f"If you did {pushups} pushups a day, you would've done {pushups1} in a week!")


# Homework Problem 5
# Use a for loop to print the square of each number from 1 to 6.
# (Example: 1*1=1, 2*2=4, etc.)
for i in range(1, 7):
    square = i * i
    print(f"{i}*{i}={square}")