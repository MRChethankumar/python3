import math

num = int(input("Enter a number: "))
temp = num
summ = 0
while (temp>0):
 rem = temp % 10
 temp = temp // 10
 summ = summ+math.pow(rem, 3)

if (num == summ):
   print("Armstrong")
else:
   print("Not an Armstrong number")
