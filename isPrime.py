#num = int(input("Enter a number: "))
#if num > 1:
#      for x in range(2,num):
#        if num % x == 0:
#            print("Not Prime")
#             print("{} times {} is {}".format(x,num//x, num))
#            break
#      else:
 #         print("Prime")*/


def prime_numbers(low,high):
    primes = []
    while(low < high):
         flag = 1
         for x in range(2,low):
             if low % x == 0:
                flag = 0
                break;
         if flag == 1:
           primes.append(low)
         low += 1
    print(primes)

low = int(input("enter low: "))
high = int(input("enter high: "))

prime_numbers(low,high)
 
             

         

         
