age = int(input("how old are you?"))
has_ticket = input("do you have a ticket? (yes/no) ")

if age >= 13 and has_ticket == "yes": # AND: both conditions must be true for our code unside the if statement to run
    print("You can enter the pg-1 movie.")
else:
    print("You cannot enter the pg-13 movie.")
print("movie check complete.")

has_pass = input("do you have a pass? (yes/no) ")
has_coins = input("do you have coins to pay? (yes/no) ")

if has_pass == "yes" or has_coins == "yes": # OR: at least one condition must be true for our code inside the if statement to run
    print("You can ride the bus.")
else:
    print("You cannot ride the bus.")

homework_done = input("did you do your homework? (yes/no) ")
if not homework_done == "yes": # NOT: flips true to false and false to true.
    print("Go finish your homework.")
else:
    print("Good job! You're all done")
print("homework check complete.")

# you can combine logical operators
is_raining = input("is it raining? (yes/no) ")
has_umbrella = input("do you have an umbrella? (yes/no) ")

if is_raining == "yes" and not has_umbrella == "yes": # Order of operations: first NOT, then AND, then OR
    print("Stay inside. You might get wet!")
elif is_raining == "yes" and has_umbrella == "yes":
    print("You're ready to go outside!")
else:
    print("no rain, you can go outside!!")