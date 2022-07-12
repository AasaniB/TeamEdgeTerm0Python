#********************************************************************
                                                                  
 #  Team Edge list Challenges!                                     
  
 #  Use this program to learn about Python lists:
    
 #  1. Declare and store data in lists
 #  2. Access list data by index
 #  3. Modify list data by index
 #  4. Multi-dimensional lists (lists inside lists!)
 #  5. List methods: append() and pop()
 #  6. The length of the list - introduce conditionals
 #  7. Strings as sequences - join() split() 
 #  
 #  Follow the -->To Dos ! run the program to test often and debug
 # ***************************************************************





print("------------------- CHALLENGE 1 -------------------")
#This is an empty Python list:
empty_list = []

#this list has 5 Strings. We can print it:
names = ["Julian", "Wolf", "Alex", "Steph", "Alessandro"]
print("names: " + str(names))  

friends = ["Aasani", "Brandon", "Bob", "Obama", "Joe"]

#-->TODO: Declare another list called friends with at least 5 strings inside (if you don't have 5 friends make them up!)


#this list holds numbers
numbers2 = [12.9, 23.4 , 100, 3.1415 , 500, 1.20]
print("numbers: " + str(numbers2)) 

numbers = [1, 2, 3, 4, 5]
#-->TODO: Declare another list and add in at least 5 numbers. Why five? I don't know. It just feels right.



#this list has mixed data types. It's allowed in Python!
random_stuff = ["Aardvark", True, False, 1.23, "Grandpa"]
print("random: " + str(random_stuff))

#-->TODO: Declare and log a list filled with the first 5 things that come into your head, booleans, Strings, numbers are all cool,
random_data=[1, True, "Wow", False, 10]

#-->TODO: Declare and log two more lists with whatever you want. 

random_things = ["Apples", 5, False, True, "F", 8]

random_things2 = ["5", 6, True, False, False, True, "Drake", 7]


print("------------------- CHALLENGE 2 -------------------")
 
#This code logs the first element of the names list:
print("The first name is " + names[0])

#-->TODO: Print the name of your best friend from your friends list
print(friends[1])

#-->TODO: Print the first AND last elements of any list you made, or make a brand new one.
print(friends[0] + friends[-1])

print("------------------- CHALLENGE 3 -------------------")
#this code changes the value of the second element of the names list, then we print the list:
names[1] = "Alyssa"
print(names)

#-->TODO: Replace your friends! Modify the list to replace any or all of your friends with new ones.
friends.pop()
friends.append("Frank")
friends.pop(3)
friends.append("Jim")
print(friends)

#The code below uses the times_ten() function to multiply the first element in our list by 10:
def times_ten(number):
    number = number * 10
    return number

numbers[0] = times_ten(numbers[0])
print(numbers)

#-->TODO: Write another function that multiplies a number by 1000 and print the list, as above 
def times_one_thousands(number2):
  number2 = number2 * 1000
  return number2

numbers2[3] = times_one_thousands(numbers2[3])  
print(numbers2)



#-->TODO: Replace your random list elements with anything you want, using the index. 

random_things2[0] = "Sus"
print(random_things2)

print("------------------- CHALLENGE 4 -------------------")

#As it turns out, you can also store lists within lists! Declare them and store them as variables.
child_list_1 = ["This", "is" , "a", "meaningless", "list"]
child_list_2 = ["This" ,"list" , "is", "also" , "meaningless"]
parent_list = [child_list_1, child_list_2]
print("This list has babies: " + str(parent_list))

#-->TODO: Store and print all the lists we have worked on thus far in a new parent list
parent_list = [friends, numbers, numbers2, random_things, random_data, random_things2,random_stuff,names]
print(parent_list)
print("------------------- CHALLENGE 5 -------------------")

#We can add elements into a list wihtout replacing anything. Using append() adds an element to the END of the list:
movies = ["Toy Story 4", "The Dark Knight", "Parasite"]
print("Movies: " + str(movies))
movies.append("Joker")
movies.append("Black Panther")
print("Movies now has: " + str(movies))

#-->TODO: Declare a list with 5 favorite songs
song = ["Song1", "Song2","song3","song4","song5"]
#-->TODO: Add 2-3 more songs using .append() and print both before and after.
song.append("song6")
song.append("song7")
#We can also remove elements using .pop(), which removes the last element or the element at the given index. You can store it after it comes out:
cities = ["New York", "Oakland", "Las Vegas", "Topeka"]
print("cities: " + str(cities))
unwanted_city = cities.pop()
print("unwanted city: " + str(unwanted_city))

#-->TODO: remove your last song using .pop() and print the removed element as above
print(song)
nosong = song.pop()
print(song)
#Note: there are more methods to remove and modify list elements. We will cover those later

print("------------------- CHALLENGE 6 -------------------")

#Lists have properties. one of the most important is the size, or length. Here are two examples:
print(f"I have {len(names)} friends")

how_many_cities = len(cities)
print(f"There are {how_many_cities} ciites in my list")

#-->TODO: Print out the number of friends, or other items from other lists using string literals as above
print(f"I have {len(friends)} friends")
print(f"There are {len(random_things)} random things in this list")


#The len() function is key, especially in conditionals or to simply count how many times to do something.

if len(numbers) > 3:
    print("There are more than 3 numbers in my list")
else:
    print("I need more numbers in my list!!!")

#-->TODO: Write another if/else statement to check the size of your songs list. If you have 5 or less, add two more songs!
if len(song) < 5:
  print("You need to add more songs")
  song_input1 = input("Enter a song name")
  song.append(song_input1)
  song_input2 = input("Enter another song name")
  song.append(song_input2)
else:
  print("You've got enough songs")

print("------------------- CHALLENGE 7 -------------------")

#Strings can also be thought of lists:
sentence = "I am a boring sentence."
boring_list = sentence.split(" ") #split the sentence by each space to get a list of words
print("boring sentence as a list: " + str(boring_list))

word = "Abracadabra"
word_split_list = word.split() #split by nothing, and you get each character in the string as its own element.
print("letter by letter: " + str(word_split_list))

#using this you can split strings up by any character!

#-->TODO: Change the name of the person who is late in this sentence and print it.
split_me = "I heard Alex was late to class today."

split_list = split_me.split(" ")
split_list[2] = "Chris"
print(split_list)

#-->TODO: Add an exclamation mark to this sentence using split() and append(), then print. (yes, there are other ways, but...)
make_me_exciting = "What a wonderful day"

exciting_split = make_me_exciting.split(" ")
exciting_split.append("!")

print(exciting_split)

#We can also join our list elements into a string using.....join()!
rejoined = " ".join(boring_list)  #joins it using spaces
print('back in one piece: ' + rejoined)

#-->TODO:  Finally, put the split_me sentence today and the make_me_exciting strings back together and print. You should see a string

unsplit = "".join(split_me)
unsplit2 = " ".join(exciting_split)

print(unsplit)
print(unsplit2)
