s=int(input("Enter number of states "))
m = [[int(input()) for x in range (s)] for y in range(s)]

terms=[]
termlen=1
t=[([0]*s) for i in range(s)]

# for i in range(s):
# 	print(m[i])
for i in range(s):
	if m[i].count(0)==len(m[i]):
		m[i][i]=1
		terms.append(i)
		termlen+=1
	else:
		m[i]=[j/sum(m[i]) for j in m[i]]

for i in range(s):
	print(m[i])
print("\n")

k=0

for i in range(s):
	if m[i][i]==1:
		t[k][k]=1
		k+=1
	
for i in range(s):
	for j in range(s):
		if m[i][i]!=1:
			t[i+termlen-1][j]=m[i][j]

for i in range(s):
	print(t[i])
print("\n")

print(terms,"\n",termlen)