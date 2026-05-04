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
#time.sleep(2)
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
