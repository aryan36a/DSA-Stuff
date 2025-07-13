#Linear Search
#Starts from the left and one by one compares each elemnent of the array
#Time Complexity:-O(n)
#Auxiliary Space:- O(1)[iterative] & O(n)[Recursive]

#Iterative Linear Search

array=[1,2,3,4,5,6,7,8,9,10]
target=10
for i in range(0, len(array)):
    if array[i]==target:
            print("Target found at position:",i)

#Recursive Linear Search
def linear_search(array,target,locator):
    if array[locator]==target:
         print("Target found at position:",locator)
    else:
         return linear_search(array,target,locator+1) 

#Driver
linear_search(array,target,locator=0)

#Binary Search
#Divide and conquer
#Time complexity:- O(log N)

#Iterative Binary Search Algorithm
def iterative_binary_search(array,target,low,high):
    while low<=high:
        mid=low+(high-low)//2
    
        if array[mid]==target:
             return mid
        if array[mid]<target:
             low=mid+1
        elif array[mid]>target:
             high=mid-1
    return -1

#Driver
res=iterative_binary_search(array,target,0,len(array)-1)
if res!=-1:
     print("Target found at:",res)
else:
     print("Element not present in array")

#Recursive Binary Search Algorithm
def recursive_binary_search(array, target, low, high):
    if low <= high:
        mid = low + (high - low) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            return recursive_binary_search(array, target, low, mid - 1)
        else:
            return recursive_binary_search(array, target, mid + 1, high)
    else:
        return -1

#Driver
res_rec = recursive_binary_search(array, target, 0, len(array) - 1)
if res_rec != -1:
    print("Target found at:", res_rec)
else:
    print("Element not present in array")