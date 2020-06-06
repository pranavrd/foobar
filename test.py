def zeroes(z):
	zero=0
	zcap=[]

	while z>0 :
		t=int(z%2)
		zcap.append(t)
		z=z//2

	z=''.join(str(i) for i in zcap[:])
	for i in range(len(z)):
		if z[i]=='0':
			zero+=1
		else:
			break
	return zero

i=int(input("Pellet size : "))

j=0
while i!=1:
	if i&1==0:
		i=i>>1
	elif ((i==3) or (zeroes(i-1)) > zeroes(i+1)):
		i-=1
	else:
		i+=1
	j+=1
print(j)
# if(i&1==1):
# 	print(dectobin(i-1))
# 	print(dectobin(i+1))

