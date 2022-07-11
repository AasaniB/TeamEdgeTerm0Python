# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!
a
# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------




# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------
import os
milk_tea = 5.00
strawberry_cream = 5.95
peach_spritzer = 4.35
mango_spritzer = 4.35
oreo_cream = 5.95
blended_vaporeon = 6.00

def display_menu():
	print("1. Milk Tea",milk_tea)
	print("2. Strawberry Cream",strawberry_cream)
	print("3. Peach Spritzer",peach_spritzer)
	print("4. Mango Spritzer",mango_spritzer)
	print("5. Oreo Cream", oreo_cream)
	print("6. Blended Vaporeon", blended_vaporeon)

def ordering_process():
	display_menu()
	numOfUsers = int(input("How many people are in your group?"))
	number_items_ordered = (int(input("How many items will you be ordering?")))
	while number_items_ordered > 0:
		display_menu()
		item_sum = 0
		individual_items = (input("What item are you ordering?"))
		if individual_items == "1":
			item_sum = item_sum + milk_tea
			number_items_ordered = number_items_ordered - 1
		elif individual_items == "2":
			item_sum = item_sum + strawberry_cream
			number_items_ordered = number_items_ordered - 1
		elif individual_items == "3":
			item_sum = item_sum + peach_spritzer
			number_items_ordered = number_items_ordered - 1
		elif individual_items == "4":
			item_sum = item_sum + mango_spritzer
			number_items_ordered = number_items_ordered - 1
		elif individual_items == "5":
			item_sum = item_sum + oreo_cream
			number_items_ordered = number_items_ordered - 1
		elif individual_items == "6":
			item_sum = item_sum + blended_vaporeon
			number_items_ordered = number_items_ordered - 1 
		else:
			print("Please use the number associated with the item on the menu.")
	
	totalpt1 = item_sum * 1.10
	print("The total sum is",totalpt1)
	total = totalpt1 / numOfUsers
	print("The cost of the order to each person is",total)

ordering_process()

# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------

# part 3









# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 





#part 3






# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 




# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------







# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
