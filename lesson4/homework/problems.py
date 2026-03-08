# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
test_scores1 = int(input("put in your first test score, "))
test_scores2 = int(input("put in your second test score, "))
if test_scores1 >= 50 and test_scores2 >= 50:
    print("yay! you passed both!!")
else:
    print("you failed at least one test...")


# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
question1 = input("did you bring lunch? (yes/no) ")
question2 = input("did you bring water? (yes/no) ")

if question1 == "yes" and question2 == "yes":
    print("you're fully ready!!")
elif question1 == "yes" or question2 == "yes":
    print("you're somewhat ready..?")
else:
    print("You're not ready...")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
number = int(input("put in a number, "))
if not (number >= 1 and number <= 10):
    print("out of range...")
else: 
    print("in range!!")


# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random
num = random.randint(1, 10)
guess = int(input("guess a number between 1 and 10, "))
if guess == num and num % 2 == 0:
    print("even match!!")
elif guess == num or num == 5:
    print("nice try..!")
else:
    print("nope...")


# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
num1 = int(input("put in a number, "))
num2 = int(input("put in another number, "))
if num1 % 5 == 0 and num2 % 2 != 0:
    print("Interesting pair!!")
else:
    print("Plain pair...")