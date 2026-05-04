import random
print("---------ROCK PAPER AND SCISSOR GAME--------")

won=0; lose=0; tie=0
emojis={'r':'🪨','p':'📄','s':'✂️'}
choices=('r','p','s')

while True:
 user_choice=input("ROCK 🪨 PAPER 📄 SCISSORS (r/p/s): ").lower()
 if user_choice not in choices:
  print("please choose r, p or s"); continue

 computer_guess=random.choice(choices)
 print(f"you chose {emojis[user_choice]}")
 print(f"computer chose {emojis[computer_guess]}")

 if user_choice==computer_guess:
  print("Tie..!"); tie+=1
 elif (user_choice=='r' and computer_guess=='s') or (user_choice=='p' and computer_guess=='r') or (user_choice=='s' and computer_guess=='p'):
  print("YOU WON"); won+=1
 else:
  print("SORRY.. YOU LOSE"); lose+=1

 if input("Continue..? (y/n): ").lower()!='y':
  print("THANK YOU FOR PLAYING")
  print(f"You Won=={won}")
  print(f"You Lose=={lose}")
  print(f"Total Tie=={tie}")
  break
