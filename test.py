import random
for x in range(random.randint(2,2000)):
  print(random.randint(1,99)," ", end="", flush=True)

# inp = input()
# l = list(map(int,inp.split()))
# l.sort()

# cnt = 0
# memo = [0] * len(l)
# print(memo,type(memo)) 
# for i in range(len(l) - 1):
#   for j in range(i + 1, len(l)):
#     if l[j] % l[i] == 0:  
#       print(memo)  
#       memo[j] += 1
#       cnt += memo[i]

# print(cnt)