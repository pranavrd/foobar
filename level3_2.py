inp = input("Enter list : ")
l = list(map(int,inp.split()))
l.sort()

count=0

l2 = [0] * len(l)

for i in range(len(l)):
	for j in range(i):
		if l[i]%l[j]==0:
			l2[i]+=1
print(l2)
for i in range(len(l)):
	for j in range(1,i):
		if l[i]%l[j]==0:
			count+=l2[j]

print(count)
