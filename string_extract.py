str = 'Perfect-Plan-B:0.7541'
strlen = len(str)
poscol = str.find(':')
num = str[poscol+1:]
num = float(num)
print(num)
