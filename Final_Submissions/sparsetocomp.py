sparse = [[0,2,0,0,5],
          [0,0,0,8,0],
          [9,3,0,0,0],
          [0,4,0,0,0]]
temp=[][]
for i in range(4):
    for j in range(5):
        if sparse[i][j]!=0:
            temp[i].append(i,j,sparse[i][j])
print(temp)