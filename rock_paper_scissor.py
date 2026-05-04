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
