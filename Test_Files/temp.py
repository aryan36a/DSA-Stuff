salaries=[1234,3421,3215,4124,123,6345,3214,2485]
def bubble_sort(salaries):
    global bubble_sort_list
    bubble_sort_list=salaries.copy()
    for i in range(len(bubble_sort_list)):
        for j in range(len(bubble_sort_list)-1):
            if bubble_sort_list[j]>bubble_sort_list[j+1]:
                bubble_sort_list[j],bubble_sort_list[j+1]=bubble_sort_list[j+1],bubble_sort_list[j]
    print(bubble_sort_list)

temp=[]


if len(salaries)>=5:
    bubble_sort(salaries)
    for i in range(1,6):
        index=len(salaries)-i
        temp.append(bubble_sort_list[index])
    print(temp)
else:
    print("Not Enough Data")
