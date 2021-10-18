try:
   fhandler = open("file.txt","r")

except:
  print ("Can not open fiel")

output = ""

for line in fhandler:
    day = list()
    line = line.strip()
    day = line.split()
    output += day[2]

print(output)
    

