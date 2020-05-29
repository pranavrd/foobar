n = input("ID ")
b = int(input("Base "))

k=len(n)

x=''.join(sorted(n,reverse=True))
y=''.join(sorted(n))

z=int(x,b)-int(y,b)

zcap=[]

while z>0 :
	t=int(z%b)
	zcap.append(t)
	z=z//b

z=''.join(str(i) for i in zcap[::-1])

zdash=int(t,3)

if zdash==n:
	return 1

n=z[:]
#got the end of first cycle of n
#add condition to check if z is same length as n


