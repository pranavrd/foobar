import math
from fractions import Fraction

def transposeMatrix(m):
    return map(list,zip(*m))

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
    
def getMatrixDeternminant(m):
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
        return determinant
        
def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],[-1*m[1][0]/determinant, m[0][0]/determinant]]
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

def convertDecToFrac(x):
	tol=1.0E-10
	h1=1
	h2=0
	k1=0
	k2=1
	b=x
	a=math.floor(b)
	aux=h1
	h1=a*h1+h2
	h2=aux
	aux=k1
	k1=a*k1+k2
	k2=aux
	try:
		b=1/(b-a)
	except:
		b=1
	while (abs(x-h1/k1) > x*tol):
		a=math.floor(b)
		aux=h1
		h1=a*h1+h2
		h2=aux
		aux=k1
		k1=a*k1+k2
		k2=aux
		try:
			b=1/(b-a)
		except:
			b=1

	ans=[]
	ans.append(h1)
	ans.append(k1)
	return ans
    
def solution(m):
    terms=[]
    termlen=0
    t=[([0]*s) for i in range(s)]
    
    for i in range(s):
        if m[i].count(0)==len(m[i]):
            m[i][i]=1
            termlen+=1
        else:
            m[i]=[j/sum(m[i]) for j in m[i]]
    for i in range(s):
        for j in range(s):
            t[(i+termlen)%s][(j+termlen)%s]=m[i][j]
    
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
                
    num=[]
    den=[]
    for i in fr[0]:
    	if fr[0]!=0:
	    	den.append(convertDecToFrac(i)[1])
	    	num.append(convertDecToFrac(i)[0])

    maxden=max(den)

    for i in range(len(num)):
    	terms.append(int(num[i]*(maxden/den[i])))

    terms.append(maxden)
    # for i in fr[0]:
    #     stringo=str(Fraction(i).limit_denominator())
    #     try:
    #         num.append(int(stringo.split("/")[0]))
    #     except:
    #         num.append(0)
    #     try:
    #         den.append(int(stringo.split("/")[1]))
    #     except:
    #         den.append(0)
    # maxden=max(den)

    # for i in range(len(num)):
    #     if num[i]==0:
    #         terms.append(0)
    #         continue
    #     if den[i]<maxden:
    #         terms.append(int(num[i]*maxden/den[i]))
    #     else:
    #         terms.append(num[i])
    
    # terms.append(maxden)
    return terms

s=int(input("Enter number of states : "))
m=[[int(input())for x in range(s)]for y in range(s)]

terms=solution(m)

print(terms)