data = input("Enter list")
n= input("Enter no. of shifts")
sol = []
for x in data:
	if data.count(x)<=n :
		sol.append(x)

print(sol)