data=[1,4,7,0,2,3,10,9,8,5]
for i in range(len(data)):
    for j in range(len(data)):
        if data[i]<data[j]:
            data[i],data[j]=data[j],data[i]
print(data)