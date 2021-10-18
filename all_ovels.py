ovels = ['a','i','e','o','u']
data = list(input("Give an input: ").lower())
count = 0
checked = set()

for v in ovels:
    for c in data:
      if v==c and v not in checked:
	      checked.add(v)
	      # count += 1

if len(checked) == 5:
   print("Accepted")
else:
   print("Invalid input")

# abc = dict()
# for c in data:
#     abc[c] = abc.get(c,0)+1

# print(abc)
# bla = list()
# for k,v in abc.items():
#     bla.append((v,k))
# print(sorted(bla, reverse=True))
