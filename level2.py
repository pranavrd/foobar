n = input("ID ")
b = int(input("Base "))

k=len(n)

for i in range(0,10):
	x=''.join(sorted(n,reverse=True))
	y=''.join(sorted(n))

	if b==10:
		z=int(x)-int(y)
	else:
		z=int(x,b)-int(y,b)

	zcap=[]

	while z>0 :
		t=int(z%b)
		zcap.append(t)
		z=z//b

	z=''.join(str(i) for i in zcap[::-1])

	con=""
	if len(z)<k:
		for i in range(0,k-len(z)) :
			con+="0"
		z=con+z

	if z[:]==n[:] :
		print(1)
		break

	print(z)

	n=z[:]
#got the end of first cycle of n
#add condition to check if z is same length as n


