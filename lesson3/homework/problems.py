# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
user_input = int(input("Type in a number."))
if user_input % 2 == 0:
    print("Even")
else:
    print("Odd")

# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".

day = input("what day is it?")
if day == "saturday":
    print("weekend")
elif day == "sunday":
    print("weekend")
else:
    print("weekday")
# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".
num = 2
while True:
    guess = int(input("choose a number from 1 and 10 "))
    if guess == num:
        print("Correct!")
        break
    else:
        print("Try again!")

# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".

positive_int = 134
while True:
    user_int = int(input("choose a positive big even number."))
    if user_int == positive_int:
        print("wow! you are correct!")
        break
    else:
        print("womp womp, try again!")

# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".

print(6 < 7)
