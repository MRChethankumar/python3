a=[[1,2],[3,4]]
b=[[5,6],[7,8]]

addi = []
multi = []

for i in range(0,len(a)):
	temp = list()
	for j in range(0,len(a[i])):
		temp.append(a[i][j]+b[i][j])
	addi.append(temp)

print(addi)


for i in range(0,len(a)):
	for j in range(0,len(b[0])):
		m_temp = list()
		summ = 0
		for k in range(0,len(b)):
			summ+=a[i][k]*b[k][j]
		m_temp.append(summ)
		multi.append(m_temp)
print(multi)





def trans():
	a = [[1,2,3],[4,5,6]]
	transpose =list()
	for i in range(0,len(a[0])):
		temp = list()
		for j in range(0,len(a)):
			temp.append(a[j][i])
		transpose.append(temp)
	print(transpose)

trans()