count = 0
summ=0
avg=0
while True:
     num = input("Enter number: ")
     if num == "exit":
        print(count, summ, avg)
        break
     else:
        try:
          num = float(num)
          count = count + 1
          summ = summ+num
          avg = summ/count
        except:
          print("Invalid data")

