data=[1,4,7,0,2,3,10,9,8,5]
for i in range(len(data)):
    for j in range(len(data)-1):
        if data[j]>data[j+1]:
            data[j],data[j+1]=data[j+1],data[j]
print(data)