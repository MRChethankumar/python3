#def isPalandrome(s):
#   return s==s[::-1]

#def isPalandrome(s):
#    for i in range(0,len(s)//2):
#         return s[i] == s[len(s)-1-i]

def isPalandrome(s):
    return s == "".join(reversed(s))
     


s = input("Enter string: ")
res = isPalandrome(s)

if res:
   print("Pal")
else:
   print("Not Pal")
