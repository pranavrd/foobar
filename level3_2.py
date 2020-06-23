from itertools import combinations

inp = input()
l = list(map(int,inp.split()))
l.sort()

L = list(combinations(l,3))

count=0

# for i in L:
# 	if i[2]%i[1]==0 and i[1]%i[0]==0:
# 		count+=1
# 		print(i[0],i[1],i[2])
l2 = []
#numbers divisible by any other number
print("First Tuple")
for i in range(len(l)):
	for j in range(i+1,len(l)):
		if l[j]%l[i]==0:
			print(l[j],l[i])
			l2.append(l[j])

print(l2)
#numbers divisible by any number in previous list
print("Second Tuple")
for i in l:
	for j in l2:
		if i!=j and i%j==0:
			print(i,j)
			count+=1
print(count)

#problem : if list is all the same numbers then count is null which is nt the case