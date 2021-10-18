import random
import datetime

def linearSearch(arr, key):
   for i in range(0,len(arr)):
       if arr[i]==key:
          return i
   return -1


if __name__ == "__main__":
   array = list()
   n = int(input("Enter number of elements: "))
   for _ in range(0,n):
       array.append(random.randint(0,n+1))
   
   print(array)

   key = int(input("Enter key: "))
   start = datetime.datetime.now()
   index = linearSearch(array, key)
   end = datetime.datetime.now()
   
   if(index>0):
      print("Found at {}".format(index))
   else:
      print("Not found")

   print("Time taken is {}".format(end-start))

   
    
       
   
