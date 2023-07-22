
# Welcome the user to the program
print("Hello, welcome to the Python Questionnaire!")
print("*******************************************")

# ask the user for their name
name = input("What is your name? ")

# ask the user for their age
age = input("What is your age? ")

# ask the user for their city
city = input("What city do you live in? ")

# ask the user what they enjoy
enjoy = input("What do you enjoy doing? ")

# create output text
output = "Your name is {} and you are {} years old. You live in {} and you enjoy {}."

# print output to screen
print(output.format(name, age, city, enjoy))


