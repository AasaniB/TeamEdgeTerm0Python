
# -------------------------------------------- 
# Day 2 Challenges
# -------------------------------------------- 

message = "Welcome to Day 2.\nToday we are learning about conditionals.\nLet's practice writing some conditionals of our own!"
print(message)
# -------------------------------------------- 

print("------------------- Challenge 1 -------------------")
# Can you drive?
   # Prompt the user to enter their age.
   # Write conditional statements that print out whether you can drive in your city. 

print("Challenge 1:")

city = input("Enter your city: ")
age = input("Enter your age: ")

if int(age) >= 16:
  print("You are allowed to drive in ", city)











# -------------------------------------------- 

print("------------------- Challenge 2 -------------------") 

# Who placed first?
   # Write conditional statements that checks which is the highest and prints the highest score. 
   # Hint: Create three variables and assign them random scores. 



num1 = random.randint(0,99)
num2 = random.randint(0,99)
num3 = random.randint(0,99)

print (num1)
print (num2)
print (num3)

if (num1 > num2) and (num1 > num3):
  print ("The highest number was", num1)
elif (num2 > num1) and (num2 > num3):
  print ("The highest number was", num2)
elif (num3 > num1) and (num3 > num2):
  print ("The highest number was", num3)







# -------------------------------------------- 

print("------------------- Challenge 3 -------------------")

# One of the most common parts of our daily routine is checking the weather. 
# Our outfit and accessories are dependent on the temperature and conditions outside. 
# ie. We're probably not going to wear shorts out when it's snowing...


# **** Challenge 3: Part 1 ****
# Write a conditional statement that checks the value of the weather variable 
# and prints out a weather report based on the current weather:
# Rainy: Bring an umbrella
# Sunny: Wear a hat and sunglasses
# Snowing: Wear gloves and a scarf 

# Here's a variable to get you started:
weather = "rainy"


Rainy = 1
Sunny = 2
Snowing = 3

randomWeather = random.randint(1,3)

if randomWeather == 1:

  randomTemp = random.randint(40,55)

  print("It's", randomTemp, "degrees outside")
  print("It's gonna be rainy today")
  print("Bring an umbrella")
elif randomWeather == 2:

  randomTemp = random.randint(70,100)

  print("It's", randomTemp, "degrees outside")
  print("It's gonna be sunny today")
  print ("Wear your best hawaiian shirt ")
elif randomWeather == 3:

  randomTemp = random.randint(5,30)

  print("It's", randomTemp, "degrees outside")
  print("It's gonna be snowing today")
  print("Wear your warmest coat")
else:
  print("detecting weather")










# Tip: Try changing the value of the weather variable to test your other conditions.

# **** Challenge 3: Part 2 ****
# Now that you've written conditions for specific weather forecasts, let's also add in temperature! 
# You can't dress accordingly if you only know that it's raining outside but not how cold it is!
# For example:
    # If it's raining and 60 degrees, you might want to bring your umbrella and wear a light jacket.
    # However, if it's raining and 30 degrees, you might want to break out a warmer jacket with your umbrella instead. 
    
   # Add to your conditional statements above and modify your weather reports to also take into account the temperature. 
   # Make sure to account for at least three different temperatures!
   # Hint: You will need another variable to keep track of the temperature.












# -------------------------------------------- 

print("------------------- Challenge 4 -------------------")

# Prompt the user to enter the day of the week (1-7 representing Monday - Sunday)
# Write a set of conditionals that will take a number from 1 to 7 
# and print out the corresponding day of the week. 
# Make sure to add a statement that accounts for any numbers out of range! 


day = input("Enter a day of the week 1-7: ")

if day == str(1):
  print("It's Monday!")
elif day == str(2):
  print("It's Tuesday!")
elif day == str(3):
  print("It's Wednesday!")
elif day == str(4):
  print("It's Thursday!")
elif day == str(5):
  print("It's Friday!")
elif day == str(6):
  print("It's Saturday!")
elif day == str(7):
  print("It's Sunday!")
else:
  print("That's not a day of the week")








# -------------------------------------------- 

print("------------------- Challenge 5 -------------------")

# A leap year is a calendar year that contains an additional day added 
# to keep the calendar year synchronized with the astronomical year or seasonal year.
# To calculate if a specific year is/was a leap year, you can follow the following steps:
     # 1. If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
     # 2. If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
     # 3. If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
     # 4. The year is a leap year (it has 366 days).
     # 5. The year is not a leap year (it has 365 days).

# Those are a lot of conditions...
# Your challenge is to translate the steps above into conditionals which will evaluate if the 
# year stored in a variable is/was a leap year.






