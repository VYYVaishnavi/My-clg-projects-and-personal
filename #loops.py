#loops in python
#loops are used to repeat the instruction
# i stands for iterator 
#for example 
# for x in reversed(range(1,11)):
#     print(x)
#print("HAPPY NEW YEAR")
#for i in range(10+1):
 #    print (i)
# for x in range(1,11,3):#STEP PARAMETER ADDED
#     print(x)
# pookie="cookies"# FOR STRING 
# for i in pookie:
#     print(i)

# credit_card="1234-567-8910"
# for x in credit_card:
#     print(x)
    
    # continue keyword
# for x in range(1, 21):
#  if x== 13: 
#     break # BREAK THE EXECUTION CODE ON PURPOSE
# else:
#      print (x)
# for x in range(1, 21):
#  if x== 13: 
#     continue # SKIPS THE VALUE GIVEN IN IF CONDITION
# else:
#      print (x)
# PROGRAM TO BUILD THE COUNTDOWN TIMER 
# import time
# my_time=int(input("Enter the number of seconds for countdown:"))
# for x in range(my_time,0,-1): # can also be reversed by reversed function
#     print(x)
#     time.sleep(1)
# print("happy new year!")
# ACTUAL TIMER PROGRAM WHICH SHOWCASE TIME DIGITALLY
# import time
# my_time=int(input("Enter the number of seconds for countdown:"))
# for x in range(my_time,0,-1): 
#      seconds= int(x % 60)
#      minutes=int(x/60)%60
#      hours=int(x/3600)
#      print(f"{hours:02}:{minutes:02}:{seconds:02}")
#      time.sleep(0)
 

    
    


