# yt practice program 
# 1 if-elseif-else(syntax)
#  if (condition)
# statement 1
# elif (condition)
# statement 2
# else:
# statement3
#example program to know your eligible for vote or not
# age=int(input("enter your age"))
# if(age>=18):
#     print("your eligible for vote")
#     print("you can have your llicence")
# else:
#     print("you cannot vote")
#     print("you cannot drive or have licence")
# program to demonstrate the if elif traffic light
# light="pink"
# if(light=="red"):
#     print('stop')
# elif(light=="green"):
#     print("go")
# elif(light=="yellow"):
#     print("look")
# else:
#    print('the light is broken')
#program to give gardes of students according to given marks
# m=int(input("Enter your marks:"))
# if(m>=90 and m<=100):
#     print("your grade is A")
# elif(m>=80 and m<=70):
#     print("your grade is B")
# elif(m>=70 and m<=60):
#     print("your grade is shit not studied properly huh?..'C")
# else:
#     print("Sorry your suspended from school you FAILED!!")
# program to check if the number entered by the user is even or odd 
# a=int(input("Enter a number"))
# if(a>=0):
#      print("the number is positive")
#      if(a%2==0):
#          print("the number is even")
#      else:
#          print("the number is odd")
#      if(a%7==0):
#          print("the number is divisible by 7")
#      else:
#          print("the number is not divisible by 7")
# else:
#      print("the number is negative")
# program to greatest among three number
# a=int(input("enter your first number:"))
# b=int(input("enter your second number:"))
# c=int(input("enter your third number:"))
# if(a>b and a>c):
#     print("the first number is greater")
# elif(b>a and b>c):
#     print("the second number is greater")
# elif(c>a and c>b):
#     print("the third number is greater")
# elif(a==b==c):
#     print("all numbers are same")
# else:
#     print("the given input is not num")
#list comprehension
#1 program to add number to each element in list
# marks=[10,20,30,40]
# new_list=[]
# for x in marks:
#     new_list.append(x+2)
#     print (new_list)
####### reduced way
#     markes=[10,20,30,40]
#     new_marks=[x+2 for x in marks]
#     print(new_marks)
# #2 program to find the cube of each elemnt in list
# makes=[]
# for x in range(10):
#          makes.append(x*3)
#          print(makes)
###########reduced way
#list2=[10,20,30,40,50]
# makes=[x**3 for x in range(10)]
# print("the list comprehention way ",makes)
#program to ask three favorite movie to user and store it into list
# movie=[]
# movie.append(input("Any comedy movie you like:"))
# movie.append(input("Any horror movie you like when your pants get wet everytime you watch:"))
# movie.append(input("Any action movie you like when you want thrill in movie"))
# print(movie)
###program to know whether the given list is palindrome or not if it is in numeric
# palin=[]
# palin.append(int(input("enter 1st num:")))
# palin.append(int(input("enter 2nd num:")))
# palin.append(int(input("enter 3rd num:")))
# palin.append(int(input("enter 4rth num:")))
# palin.append(int(input("enter 5th num:")))
# palindrom=palin.copy()
# palidrome=palindrom.reverse()
# if(palin==palidrome):
#     print("the list contain palidrome")
# else:
#     print("the list does not  contain palidrome")
#counting the number of grades student have
# grade=('A','B','C','A','A','C','B')
# grades=grade.count('A')
# print(grade)
# print(grades)
#calculator 
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# print("For addition chose 1")
# print("For subtraction chose 2")
# print("For division chose 3")
# print("For modules chose 4")
# print("For multiplication chose 5")
# number=int(input("chose number between 1 to 5:"))
# if(number==1):
#     print('The addition is:',a+b)
# elif(number==2):
#     print('The subtraction  is:',a-b)
# elif(number==3):
#     print('The division is:',a/b)
# elif(number==4):
#     print('The modulo is:',a%b)
# elif(number==5):
#     print('The multiplication  is:',a*b)
#kaun banega crore pati
# print("Round 1.......")
# Money=[1000,2000,3000,4000,5000]
# Option=[1.,2.,3.,4.]
# q1=input("Question 1: Which state in india have traditional dance like garba?")
# print("1.Gujarat")
# print("2.Maharatra")
# print("3.Odisha")
# print("4.Andra pradesh")
# q12=(input("select any number from 1 to 4:"))
# if(q12==1.):
#     print("Your answer is correct")
# else:
#     print("Your answer is incorrect")
#     print("You lost 1000...👎🏼")















   








