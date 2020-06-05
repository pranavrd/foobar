i=int(input("Pellet size : "))

j=0
while i!=1:
	if i&1==0:
		i=i>>1
	elif ((i==3) or ((i+1)&i) > ((i-1)&(i-2))):
		i-=1
	else:
		i+=1
	j+=1
print(j)
