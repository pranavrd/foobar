from fractions import Fraction

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors

s=int(input("Enter number of states "))
m = [[int(input()) for x in range (s)] for y in range(s)]

terms=[]
termlen=0
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
			t[i+termlen][j]=m[i][j]

r=[[0 for i in range(termlen)] for j in range(s-termlen)]
q=[[0 for i in range(s-termlen)] for j in range(s-termlen)]

for i in range(s-termlen):
	for j in range(termlen):
		r[i][j]=t[i+termlen][j]

for i in range(s-termlen):
	for j in range(s-termlen):
		q[i][j]=-1*t[i+termlen][j+termlen]
	q[i][i]=1+q[i][i]

f=getMatrixInverse(q)

fr=[[0 for i in range(termlen)] for j in range(s-termlen)]

for i in range(s-termlen):
	for j in range(termlen):
		for k in range(s-termlen):
			fr[i][j]+=f[i][k]*r[k][j]

for i in range(s):
	print(t[i])
print("\n")

for i in range(s-termlen):
	print(r[i])
print("\n")

for i in range(s-termlen):
	print(q[i])
print("\n")

for i in range(s-termlen):
	print(f[i])
print("\n")

for i in range(s-termlen):
	print(fr[i])
print("\n")


for i in fr[0]:
	print(Fraction(i).limit_denominator())

#print(np.dot(f,q))
print(terms,"\n",termlen)