s=int(input("Enter number of states "))
m = [[int(input()) for x in range (s)] for y in range(s)]

terms=[]
termlen=1
t=[([0]*s) for i in range(s)]

# for i in range(s):
# 	print(m[i])
for i in range(s):
	if m[i].count(0)==len(m[i]):
		terms.append(i)
		termlen+=1
	else:
		m[i]=[j/sum(m[i]) for j in m[i]]

for i in range(s):
	print(m[i])
print("\n")

for i in range(s):
	for j in range(s):
		for k in range(s):
			if k not in terms:
				t[i][j]+=m[i][k]*m[k][j]

for i in range(s):
	print(t[i])
#print(terms,"\n",termlen)