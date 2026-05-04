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
  



