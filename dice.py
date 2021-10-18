import random 
while True:     
     print(''' 1. roll the dice             2. exit     ''')    
     user = input("what you want to do\n")
     try:
       user=int(user)
     except:
       print("Invalid Choice")
       continue     
     if user==1:         
        number = random.randint(1,6)         
        print(number)     
     elif user==2:
       break
     else:
       print("Invalid Choice")
       continue