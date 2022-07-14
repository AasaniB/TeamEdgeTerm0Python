#############################################################################
 #                                                                  
 #  Team Edge dictionaries: Dictionaries CHALLENGES 
 # 
 #  For this activity, you will be building a dictionary and with properties
 #  and methods. You will access the properties, set new values, and use
 #  the methods to change your dictionary state. What dictionary? Ask your coach.
 # 
 #  1. DEFINE: Make a dictionary and set its properties, printing changes in between.
 #  2. MODIFY: Add 2 new properties and assing values. Change existing values,
 #     including adding or updating values inside lists
 #  3. METHODS: Now its time to make some methods tha can make a change
 #     to your values, like a boolean, or they can print something about
 #     the dictionary. Nothing fancy, unless you fancy it.
 #  4. LITERALLY: Use string literals to put it all together in one statement.
 # 
 # #########################################################################/

print("------------------- CHALLENGE 1 : DEFINE    -------------------")

#Below is a simple example of a dictionary implementaion. 
#-->TODO: Add at least 3 comments to the dictionary below to demonstrate you understand its usage

dictionary = {
    "name": "box",
    "is_empty": True
}
#working with the dictionary:
dictionary["length"] = 12
dictionary["width"] = 8
dictionary["contents"] = ["thing 1", "thing 2", "thing 3"]
print(f"{dictionary['name']} is {dictionary['length']} {dictionary['width']}")
dictionary["contents"].append("thing 4")
print(f"{dictionary['name']} has {dictionary['contents']}")
print(dictionary)

 

#-->TODO: Declare a new dictionary and set at least 4 properties to it including: string, boolean, number, list

##################################  MY dictionary ########################### #/

new_dict = {
    "name": "food shop",
    "is open_bool": True,
    "Number of items on menu": 10,
    "Items on menu": ["Cake", "Apple Sauce", "Chips", "Carrots", "Turkey"],
    "Is open": ["Open", "Closed"]
    
  
}






########################################################################## #/



print("------------------- CHALLENGE 2 : MODIFY   -------------------")

#-->TODO: Print your dictionary you created above
print(new_dict)


#-->TODO: Update the dictionary you just created  by adding new properties and values, including list elements, in this section.

new_dict["Items on menu"].append("Pizza")
new_dict['Number of items on menu'] += 1
new_dict["is open_bool"] = False


#-->TODO: Print your dictionary again and observe changes
print(new_dict)


print("------------------- CHALLENGE 3 : MEHTODS   -------------------")


#-->TODO: Make a method that will update your dictionary value. It should take in a dictionary and return it modified.

def change_dict():
  keep_asking = input("Would you like to modify the food shop's menu? Yes or no? ")
  while keep_asking != "no":
    if "yes" in keep_asking:
      ask_user = input("Would you like to open/close the shop or an item to the menu ")
      if "open shop" in ask_user:
        print("the shop is now open")
        new_dict["is open_bool"] = True
        print(f"is open = {new_dict['is open_bool']}")
      if "close shop" in ask_user:
        print("The shop is now closed")
        new_dict['is open_bool'] = False
        print(f"is open = {new_dict['is open_bool']}")
      if "add item" in ask_user:
        user_item = input("What item would you like to add to the list? ")
        if user_item not in new_dict:
          print("adding item to the food shop")
          new_dict["Items on menu"].append(user_item)
          new_dict["Number of items on menu"] += 1
          print(f"Here's the updated menu: New food options: {new_dict['Items on menu']} Number of items on list: {new_dict['Number of items on menu']}")
        else:
          print("The item you requested is already on the menu, you should order it!")
    keep_adding = input("Would you like to change anything else? Yes or no? ")
    if "No" in keep_adding:
      print("Ok")
      break
      
        
change_dict()


#-->TODO: Call the method.



print("------------------- CHALLENGE 4 : LITERALLY   -------------------")

#-->TODO: Put it all together using a string literal to tell the story of your dictionary!
