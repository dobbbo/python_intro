# This program greets the user by name and shows which year they were born in.
print('Hello world!')
print('What is your name?')
name = input()
print('Nice to meet you, ' + name + '.')
print('What is your age?')
age = input()
year_of_birth = 2022 - int(age)
print('You were born in ', year_of_birth) # Assumes users birthday this year has already passed.