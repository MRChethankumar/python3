#try:
dec = int(input("Enter a number: "))
bi = 0
num = list()
while(dec>0):
	rem = dec % 2
	num.append(str(rem))
	dec = dec // 2
print("".join(num[::-1]))

#except:
#   print("Enter a proppr decmal value")
