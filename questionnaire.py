# ask the user for their name
# ask the user for their age
# ask the user for their city
# ask the user what they enjoy
# create output text
# print output to screen


print("Hello, welcome to the Python Questionnaire!")
name = input("What is your name? ")
age = input("What is your age? ")
city = input("What city do you live in? ")
enjoy = input("What do you enjoy doing? ")
output = "Your name is {} and you are {} years old. You live in {} and you enjoy {}."
print(output.format(name, age, city, enjoy))


