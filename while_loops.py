import random
#********************************************************************
 #                                                                  
 #  Team Edge Mini-project: WHILE LOOP CHALLENGES
 # 
 #   Complete the following loop challenges below. Follow the ToDos
 #   1. IN YOUR PRIME: Declare a while loop that prints all the prime 
 #      numbers between 0 and 100 (use the helper function provided)
 #   2. FOUND: use a while loop to search the contents of a list for
 #     the key!
 #   3. BUGGIN: Find out why these while loops don't do what they say 
 #     they do.
 #   4. MATH QUIZ: Prompt a user to solve a random math problem, if 
 #      they get it right, say congrats, if not, keep prompting.
 #   5. WHAT AM I: Write a game loop that prompts that never stops
 #      asking, "Iknow you are a _____, but what am I?"
 # 
 # ***************************************************************/

print("------------------- CHALLENGE 1 : IN YOUR PRIME -------------------")

#Here is a humble while loop in action. We need a variable to hold the counter value.

# while num <= 10:
#     print("example counter--> " + str(num))
#     num += 1


#------------ Helper function, do not mess with this part below ---------------??
num = 100

def test_prime(n):
  if n==1:
    return False

  elif n == 2:
    return True

  else:
    for x in range(2, n-1):
      if n % x == 0:
        return False
    return True
test_prime(100)
# #-->TODO: Declare a while loop that prints all the prime numbers between 0 and 100, use test_prime() helper function
# while True:
#   test_prime(100)
    
    
     



print("------------------- CHALLENGE 2 : FOUND   -------------------")

#here is a list full of items
items = ["pencil" , "eraser" , "mirror" , "comb" , "spoon" , "key" , "earrings" ,"cat food" , "magazine"]

#-->TODO: Use a while loop to search the contents of a list for the key! If it exists, print "found the key!"
y = 0
key_found = False
while key_found == False:
  y += 1
  if items[y] == "key":
    key_found = True
    print("found the key")
  if items[y] != "key":
    print("The key was not found")
  
  
  
  
    



print("------------------- CHALLENGE 3 : BUGGIN   -------------------")

#Oh no! these functions have loops that don't do what they say they should do. Can you fix that?
#One more thing...to stop an infite loop you hit Control + C in the terminal  

#-->TODO: Make me count  2, 4, 6,..., 50

def even_numbers_to_fifty():
    num = 0
    while num < 51:
      num +=2
      print(num)
      if num == 50:
        break
    
        

even_numbers_to_fifty()

#-->TODO: Make this design  below
#
#          [ 0 ]
#          [ 0, 1 ]
#          [ 0, 1, 2 ]
#          [ 0, 1, 2, 3 ]
#          [ 0, 1, 2, 3, 4 ]
#          [ 0, 1, 2, 3, 4, 5 ]
#          [ 0, 1, 2, 3, 4 ]
#          [ 0, 1, 2, 3 ]
#          [ 0, 1, 2 ]
#          [ 0, 1 ]
#          [ 0 ]



def pattern():

  index = 0 
  my_list =[]
    
  while index <= 5:
    my_list.append(index)
    print(my_list)
    index += 1
  while index > 1:
    my_list.pop()
    print(my_list)
    index = index -1

      

pattern()


print("------------------- CHALLENGE 4 : MATH QUIZ   -------------------")



#-->TODO: Make a Math Quiz that adds two random numbers (between 0 and 100 to make it easy).
#         The user enters the answer. If wrong, keep prompting. If correct, say congrats!!
#         Use this handy boolean to get you started! You will need input()!

is_correct = False


while is_correct == False:
  random_int = random.randint(0,1)
  random_int2 = random.randint(0,1)
  get_num = input("Guess the first number: ")
  get_num2 = input("Guess the first number: ")

  if int(get_num) == random_int or int(get_num2) == random_int2:
    print("congrats", str(random_int), "and", str(random_int2), "were the right numbers")
    is_correct = True
  else:
    print("That wasn't the correct guess")
  



print("------------------- CHALLENGE 5 : WHAT AM I?   -------------------")

#-->TODO: Write a game loop that prompts that never stops asking, "I know you are a _____, but what am I?"
#         You are given two starter functions and a loop to get started! 
#         Notice how one function calls the other and uses the returned value as the input. This is called Recursion! 

keep_asking = True

def prompt_user():
  print("What do you think I am?")
  response = input("")
  return response
  pass

def response(response):
  print(f"I know you're {response}, but what am I")
  pass

while keep_asking:
  response(prompt_user())
  pass

#-->TODO: Challenge! write a secret word to break out of the loop!




