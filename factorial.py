#num =  int(input("Enter a number: "))
#fact = 1
#for x in range(1,num+1):
#    fact = fact*x

#print("Factorial of the {} is {}".format(num, fact))



def factorial(n):
    if n==1:
       return n
    return n*factorial(n-1)

num =  int(input("Enter a number: "))
fact = factorial(num)
print("Factorial of the {} is {}".format(num, fact))

