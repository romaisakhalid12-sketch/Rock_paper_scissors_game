import random
# random_integer = random.randint(1,2)
# print(random_integer)
# random_float = random.random()
# print(random_float)
# random_float *5
# random_side = random.randint(0,1)
# if random_side == 1:
#     print("Heads")
# else:
# #     print("Tails")
# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut",
# "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia",
# "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky",
# "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi",
#   "Illinois", "Alabama", "Maine", "Missouri", "Arkansas",
#   "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
#   "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
#   "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
#   "Montana", "Washington", "Idaho", "Wyoming", "Utah",
#   "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
# num_of_states = len(states_of_america)
# print(states_of_america[num_of_states-1])

# name_string = input("give me everybodys name,seperated by a comma. ")
# names = name_string.split(",")
# num_items = len(names)
# random_choice = random.randint(0,num_items-1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + " is going to buy a meal today")
# fruits=["grapes","mangoes","peaches","cherries","potatoes"]
# vegetables =["spinach","kales","tomatos","celery","potatoes"]
# dirty_dozen = [fruits,vegetables]
# print(dirty_dozen)
game_images =["rock","paper","scissors"]
user_choice = int(input("What do you choose? Type 0 for Rock,1 for paper or 2 for scissors"))
if user_choice >= 3 or user_choice <0 :
 print("you typed an invalid number,YOU LOSE!")
else:
 print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose :")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
 print("You win!")
elif computer_choice == 0 and user_choice ==2:
 print("You lose!")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("it's a draw")


