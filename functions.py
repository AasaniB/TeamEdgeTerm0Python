# -------------------------------------------- 

	# You've just learned about functions.
	# Functions are reusable pieces of code that make your code more modular.
	
	# If you are writing the same bit of code over and over, you are doing more work that you have to.
	# Use functions to simplify your code and decrease the amount of work you're doing. 

	# Any time you start thinking 'this is tedious', you can probably write a function for that task.

# -------------------------------------------- 


# -------------------------------------------- 
  # Challenge 1: Let's try to write some basic functions.
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")

# **** Challenge 1: Problem 1 ****
# Write a function called print_message() that prints any message you want.
messages=["hello world", "Halloween", "Sauce", "Donut", "Bird Person"]
def print_message(message = random.choice(messages)):
	print(message)

print_message()

# **** Challenge 1: Problem 2 ****
# Write a function called print_five_messages() that calls print_message() five times.
def print_5_messages(message = random.choice(messages)):
  for x in messages:
    y = 1

    if y == 1:
      x = random.choice(messages)
      y += 1
      print(x)
    elif y == 2:
      x = random.choice(messages)
      y += 1
      print(x)
    elif y == 3:
      x = random.choice(messages)
      y += 1
      print(x)
    elif y == 4:
      x = random.choice(messages)
      y += 1
      print(x)
    elif y == 5:
      x = random.choice(messages)
      y += 1
      print(x)
      break
    else:
      print("No")

print_5_messages()


# **** Challenge 1: Problem 3 ****
# Write a function called get_user_input() that asks the user if they'd like to print your message
# once or five times. Then call one of the two functions above based on what the user decides.

def get_user_input(message = random.choice(messages)):
  userIn = input("Would you like to print a message once or 5 times? ")

  if userIn == str(1):
    print_message()
  elif userIn == str(5):
    print_5_messages()
  else:
    print("You can only print the message once or 5 times")

get_user_input()


# **** Challenge 1: Problem 4 ****
# Write a function called print_greeting() that prints a greeting message to the user.

greetings = ["Howdy", "Hello there", "Wassup", "Hi"]
def print_greeting(greet = random.choice(greetings)):
  user = input("Would you like to be greeted? ")

  if user == "yes":
    print(greet)

  elif user == "no":
    print("Well I didn't want to greet you anyway")

print_greeting()


# **** Challenge 1: Problem 5 ****
# Write a function called print_closing() that prints a goodbye message to the user.
goodbye = ["See ya", "Later aligator", "See ya wouldn't want to be ya", "Peace out", "Smell you later"]

def print_closing(bye = random.choice(goodbye)):
  print("Well its been fun but I'm going to sleep")

  print(bye)

print_closing()


# **** Challenge 1: Problem 6 ****
# Write a function called run() that greets the user, asks them for input, and sends a goodbye message.
# Remember! Use the functions that you've already made. Don't hardcode anything!

def run(bye = random.choice(goodbye), greet = random.choice(greetings), message = random.choice(messages)):
  print_greeting()
  get_user_input()
  print_closing()

run()



# -------------------------------------------- 

# Challenge 2: Functions are also able to take input and return output. 
				# The value(s) you pass to it are called parameters.

# -------------------------------------------- 

print("------------------- Challenge 2 -------------------")

# **** Challenge 2: Problem 1 ****

# Write a function called sum_double that takes two number paramters and returns their sum.
# However, if the two values are the same, the funciton will return double their sum.

	# Examples:
		# sum_double(1, 2) → 3
		# sum_double(3, 2) → 5
		# sum_double(2, 2) → 8

# -------------------------------------------- 




num1 = 1
num2 = 2

double = num1 * num2

def sum_double():
  user_input = input("Enter a number: ")
  input2 = input("Enter another number: ")
  num1 = int(user_input)
  num2 = int(input2)
  sum = num1 + num2 
  
  if num1 != num2:
    print(sum)
  else:
    print(sum * 2)

sum_double()



# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 2 ****

# Write a function called makes_10 that takes two numbers, a and b, and returns true if one of them is 10 or if their sum is 10.

	# Examples:
		# makes_10(9, 10) → True
		# makes_10(9, 9) → False
		# makes_10(1, 9) → True

# -------------------------------------------- 



def make_10():
  is_10 = True
  user_in = input("Enter a number: ")
  user_in2 = input("Enter another number: ")

  n1 = int(user_in)
  n2 = int(user_in2)

  sum = n1 + n2

  if sum == 10 or n1 == 10 or num2 == 10:
    print(is_10)
  else:
    is_10 = False
    print(is_10)
make_10()


# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 3 ****

# Write a function that will return the time our alarm is set to go off.

# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean
# indicating if we are on vacation, return a string in the form "7:00" indicating
# when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on
# the weekend it should be "10:00". However, if we are on vacation -- then on weekdays
# it should be "10:00" and weekends it should be "off".
	# Examples:
		# alarm_clock(1, False) → "7:00"
		# alarm_clock(6, True) → "off"
		# alarm_clock(0, False) → "10:00"

# -------------------------------------------- 







# Make sure to test your code! Write a few function calls to make sure your code works!

# -------------------------------------------- 

# **** Challenge 2: Problem 4 ****

# Write a function that will tell you if you received a speeding ticket.
# You are driving a little too fast, and a police officer stops you. 

# To compute the result, encoded as a number value: 
	# 0=no ticket
	# 1=small ticket
	# 2=big ticket
# If speed is 60 or less, the result is 0. 
# If speed is between 61 and 80 inclusive, the result is 1. 
# If speed is 81 or more, the result is 2.

# -------------------------------------------- 








# Make sure to test your code! Write a few function calls to make sure your code works!
