#1 DICE ROLLING GAME 
import random
while True:
    roll=(input("ROLL THE  DICE?? (y/n):"))
    if roll=='y':
       die1=random.randint(1,6)
      print("You rolled:",die1)
   elif roll=='n':
      print("Thanks for playing")
      break
   else:
      print("Incorrect choice")
   
      
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




