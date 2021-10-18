fhandler = open("file.txt","r")

data = fhandler.read()

data_list = list()

data_list = data.split()

count = dict()

for word in data_list:
    count[word] = count.get(word,0)+1

words = list()

for (k,v) in count.items():
    words.append((v,k))

print(words)

sorted_lis = sorted(words, reverse=True)

out_put = "" 

for x,y in sorted_lis:
    out_put += y+' '+str(x)+' '



#for key, value in count.items():
#    out_put += key+' '+str(value)+' '

#Keymax = ""

#Keymax = max(count, key=count.get) 

#out_put += "Done "+Keymax+" "+str(count[Keymax])

print(out_put)


