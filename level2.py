n=input("ID ")
b=int(input("base "))
flag=0
k=len(n)
l=[]
upid=0
count=0
while True:
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
		flag=1
		break
    
	n=z[:]
    
	if z in l:
	    upid=l.index(z)
	    break
	l.append(z)

if flag==1:
    print(1)
else:
    print(len(l)-upid)