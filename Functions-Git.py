#4.13.3: Greetings
#Matthew Beaver
#2/5/19



name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "! ")
    print("Nice to meet you")

greeting()



#4.13.4: Functions and Variables
#Matthew Beaver
#2.11.19

x =  10

def print_something():
    x = 3
    print('\n', x)

print('\n', x)
print_something()

#4.13.6: Functions and Variables, Part 3
#Matthew Beaver
#2.18.19


def print_number(x):
    print(x)

print_number(13)
print_number(23)


# 4.14.4: Name & Age
# Matthew Beaver
# 2.18.19

def name_and_age(name, age):
    print('\n','Hi, my name is', name, 'and I am', age, "years old!")

name_and_age('Mike', 33)
name_and_age('Zane', 18)

# 4.14.5: Default Parameter Values
# Matthew Beaver
# 2.19.19

def print_two_number(x, y = 20):
    print('First Number: ', x)
    print('Second Number: ' + str(y))

print_two_number(34, 45)
print_two_number(78)

# 4.14.6: Print Sum
# Matthew Beaver
# 2.19.19


def print_sum(x, y):
    print(x + y)

print_sum(46, 62)


# 4.16.3: Enter a Number using Try and Except
# Matthew Beaver
# 2.20.19

try:
    my_num = int(input('Enter an integer: '))
    print('Your number:', my_num)

except ValueError:
    print('\n''That was not an integer.')


# 4.16.4: Enter Name & Age using the Try & Except Rule
# Matthew Beaver
# 2.20.19


name = input('Enter your name: ')

age = -1

try:
    age = int(input('Enter your age: '))
except ValueError:
    print('\n''That was not an integer for your age')

print('\n''Name:', name)
print('Age:', age)

#Matthew Beaver
#1.14.19

my_number = 7

print ("Guess a number between 1 and 10")
print ("")

guess = int(input("Enter a guess: "))

while guess != my_number:
    print ("")
    print ("Your number was wrong. Guess again!")
    guess = int(input("Guess again: "))

print("")
print ("Great! That must have taken you awhile.")

#Program Tracing
# Matthew Beaver
x = 20

while x > 5:
    print(x)
    x = x - 2
