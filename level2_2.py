st=int(input("Start "))
en=int(input("End "))

x=st//8+1
y=st%8+1
ex=en//8+1
ey=en%8+1

hop=[[+2,+1],[+2,-1],[-2,+1],[-2,-1],[+1,+2],[+1,-2],[-1,+2],[-1,-2]]
  
hopx=[]
hopy=[]
hopdist=[] 

hopx.append(x)
hopy.append(y)
hopdist.append(0) 

visited = [[0 for i in range(9)]  
                  for j in range(9)] 
 
visited[x][y] = 1

while(len(hopx) > 0): 
	tx = hopx[0]
	ty = hopy[0]
	tdist=hopdist[0] 

	hopx.pop(0)
	hopy.pop(0)
	hopdist.pop(0)
    
    
	if(tx==ex and ty==ey):
		print(tdist)
	break      

	for i in range(8): 
          
		x = tx + hop[i][0] 
		y = ty + hop[i][1] 
          
		if(x >= 1 and x <= 8 and y >= 1 and y <= 8 and visited[x][y]==0): 
			visited[x][y] = 1
			hopx.append(x)
			hopy.append(y)
			hopdist.append(tdist+1) 