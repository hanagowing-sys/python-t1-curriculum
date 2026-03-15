# Problem 1
# Create a list of 3 operating systems.
# Print the last one using len().
# Then reverse the list and print it.
system = ["microsoft", "android", "linux"]
print(system[len(system)-1])
system.reverse()
print(system)

# Problem 2
# Create a list of 4 school subjects.
# Print the second subject.
# Then sort them alphabetically and print the result.
subjects = ["science", "math", "history", "language arts"]
print(subjects[1])
subjects.sort()
print(subjects)

# Problem 3 
# Create a list of 5 error codes.
# Print how many there are.
# Then find the index of "403" and print it.
error_codes = ["404", "500", "403", "401", "502"]
print(len(error_codes))
print(error_codes.index("403"))

# Problem 4 
# Create a list of 2 programming languages.
# Print a random one.
# Then append another language and print the list.
import random
languages = ["Python", "Java"]
print(random.choice(languages))
languages.append("C++")
print(languages)

# Problem 5
# Create a list of 6 passwords.
# Print the one in the middle using len().
# Then remove the first password in the list and print it.
passwords = ["password123", "qwerty", "lemmeinpls", "abc123", "wherethehuzzat", "67676767"]
print(passwords[len(passwords)//2])
print(passwords.pop(0))
print(passwords) 
