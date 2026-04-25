#1 DICE ROLLING GAME 
# import random
# while True:
#    roll=(input("ROLL THE  DICE?? (y/n):"))
#    if roll=='y':
#       die1=random.randint(1,6)
#       print("You rolled:",die1)
#    elif roll=='n':
#       print("Thanks for playing")
#       break
#    else:
#       print("Incorrect choice")
#    
#       
# 1. MODIFICATION IN DICE ROLLING GAME
import random
def no_dice(n):
   return [random.randint(1,6) for i in range(n)]
def main():
   count=0
   while True:
      count+=1
      roll=(input("ROLL THE  DICE?? (y/n):"))
      if roll=='y':
         n=int(input("How many dice do you want to roll?"))
         result=no_dice(n)
         print("You rolled:",result)
      elif roll=='n':
        print("Thanks for playing!")
        print(f"You rolled the dice {count} times")
        break
      else:
         print("Incorrect choice")
if __name__=='__main__':
 main()
# ANOTHER MODIFICATION ON ROLLING GAME--count the times the user have play and display it 
#show the score




  #RESTRAUNT MANAGEMENT SYSTEM PROGRAM 
# import time
# menu={"pizza":4.2,
#    "coffee":2,
#    "italian pasta":5,
#    "volcano choclate cupcake":2.9,
#    "sandwich":2,
#    "salad":3,
#    "boba":4
#     }
# time.sleep(2)
# print("Welcome to catcakes restraunt")
# print("-----MENU-----")
# print("PIZZA🍕 ---- $4.2")
# print("COFFEE☕️---- $2")
# print("ITALIAN PASTA🍝 ------$5.0")
# print("VOLCANO CHOCLATE CUPCAKE 🧁-------$2.9")
# print("SANDWICH🥪------$2")
# print("SALAD🥗------$3")
# print("BOBA🧋-------$4")
#  # ordering of menu
# order_total=0
# first_order=input("Sir,What do you like to order first??---")
# time.sleep(2)
# if first_order in menu:
#      order_total+=menu[first_order] 
#      print(f"Order of {first_order} has been added")
# else:
#      print("The order is UNAVAILABLE!!")
#      while True:
#       unlimited_order=input("Do you want to add another item? (y/n):")
# time.sleep(1)
# if unlimited_order=='y':
#      order=input("Enter item:")
#      order_total+=menu[order]
#      print(f"Order of {order} has been added")
# elif unlimited_order=='n':
#      time.sleep(2)
#      print("Here is 🍕\n🥪\n☕️\n🧋\n🥗\n🍔")
#      time.sleep(3)
#      print("Enjoy the happy meal!! ")
#      time.sleep(3)
#      print(f"Here is PAYMENT:--${order_total}cents")
#      time.sleep(3)
#      print("Have a good day,Sir!!")
#      break
#    else:
#      print("The order is UNAVAILABLE!!")
#  # switch case add or remove the order, lower case or upper case item entered should not throw error, add afeature which shows the order they add in list ussing emoji
# #add a feed back for food store it in variable or dictionary using customer  













    #NUMBER GUESSING GAME
#---------------------------------
# import random
# number_guess=random.randint(1,100)
# while True:
#  try:
#    guess=int(input("Guess any number between (1-100)--:"))
#    if guess>number_guess:
#     print("Too High!,Guess again")
#    elif guess<number_guess:
#     print("Too low...,Try again")
#    elif number_guess==guess:
#     print("There You Go!!..you GOT IT IN  TRIES")
#     break
#  except ValueError:
#    print("please enter the valid number!!")
    

#ENHANCEMENT IF USER INPUT IS INVALID THEN ADDING STATEMENT SO THAT IT WILL NOT THROW ANY ERROR
# import random
# import time
# time.sleep(1)
# print("--------------------------NUMBER GUESSING GAME--------------------")
# time.sleep(1)
# while True:
#      range1=(input("Enter the minimum value you want to guess:"))
#      range2=(input("Enter the maximum value you want to guess:"))
#      if range1.isdigit() and range2.isdigit():
#        range1=int(range1)
#        range2=int(range2)
#        if range1<range2:
#           break
#        else:
#          print("The minimum value should be less the maximum")
#      else:
#        print("please Enter the valid numbers")
# computer=random.randint(range1,range2)
# count=0
# while True:
#     guess=(input(f"Guess any number between {range1}-{range2}:"))
#     if guess.isdigit():
#          guess=int(guess)  
#          count+=1
#          if guess>computer:
#              print("Too High!,Guess again")
#          elif guess<computer:
#             print("Too low...,Try again")

  

#ENHANCEMENT- Implement a feature that limits the number of guesses a player can make. If
#the player runs out of attempts, the game should end, and the correct number
#should be revealed.
# import random
# import time
# time.sleep(0)
# print("--------------------------NUMBER GUESSING GAME--------------------")
# print(".....................Limit to guess any number IS--6................... ")
# time.sleep(0)
# while True:
#     range1=(input("Enter the minimum value you want to guess:"))
#     range2=(input("Enter the maximum value you want to guess:"))
#     if range1.isdigit() and range2.isdigit():
#       range1=int(range1)
#       range2=int(range2)
#       if range1<range2:
#          break
#       else:
#         print("The minimum value should be less the maximum")
#     else:
#       print("please Enter the valid numbers")
# computer=random.randint(range1,range2)
# count=0
# while True:
#   guess=(input(f"Guess any number between {range1}-{range2}:"))
#   if guess.isdigit():
#         guess=int(guess)  
#         count+=1
#         if count==6:
#            print(f"Sorry...You lose,Try Again!")
#         else:
#            print(f"")
#            break
#         if guess>computer:
#             print("Too High!,Guess again")
#         elif guess<computer:
#            print("Too low...,Try again")
#         elif computer==guess:
#            print(f"There You Go!!..you GOT IT IN {count} TRIES")
#            break
#         else:
#            print("please enter the valid number!!")
  

#ENHANCEMENT ADDING SCORE HIGH SCORE
  
# import random
# import time
# time.sleep(1)
# print("--------------------------NUMBER GUESSING GAME--------------------")
# time.sleep(1)
# while True:
#     range1=(input("Enter the minimum value you want to guess:"))
#     range2=(input("Enter the maximum value you want to guess:"))
#     if range1.isdigit() and range2.isdigit():
#       range1=int(range1)
#       range2=int(range2)
#       if range1<range2:
#          break
#       else:
#         print("The minimum value should be less the maximum")
#     else:
#       print("please Enter the valid numbers")
# computer=random.randint(range1,range2)
# count=0
# while True:
#    guess=(input(f"Guess any number between {range1}-{range2}:"))
#    if guess.isdigit():
#         guess=int(guess)  
#         count+=1
#         if guess>computer:
#             print("Too High!,Guess again")
#         elif guess<computer:
#            print("Too low...,Try again")
#         elif computer==guess:
#            print(f"There You Go!!..you GOT IT IN {count} TRIES")
#            break
#         else:
#            print("please enter the valid number!!")
  
#ROCK PAPER AND SCISSOR GAME-----
# import random
# print("---------ROCK PAPER AND SCISSOR GAME--------")
# won=0
# lose=0
# Tie=0
# while True:
#  emojis={'r':'🪨','p':'📄','s': '✂️'}
#  choices=('r','p','s')
#  user_choice=input("ROCK🪨 PAPER📑 SCISSORS (r/p/s): ").lower()
#  if user_choice not in choices:
#    print("please choose any one from above choices")
#    continue
#  computer_guess=random.choice(choices)
#  print(f"you chose {emojis[user_choice]}")
#  print(f"computer chose {emojis[computer_guess]}")
#  won+=1
#  if (
#    user_choice=='r'and computer_guess=='s' or
#    user_choice=='p'and computer_guess=='r' or
#    user_choice=='s'and computer_guess):
#    print("YOU WON..")
#    Tie+=1
#  elif user_choice==computer_guess:
#    print("Tie..!,Try Again")
#    lose+=1
#  else:
#    print("SORRY.. YOU LOSE ")
   
#  should_continue=input("Continue..? (y/n):")
#  if should_continue=='y':
#    print("")
#  else:
#    print("THANK YOU FOR PLAYING")
#    print(f"You Won=={won}")
#    print(f"You Lose=={lose}")
#    print(f"Total Tie=={Tie} ")
#    break


   



