# arr=[1,2,3,14,15,16,65,78,89]
# element=10
#programe to find an element from array

#
# fak=0
# for n in arr:
#     if(n==element):
#         fak=1
#         break
# if fak==0:
#     print("Element not found")
# else:
#     print("Element found")
#
# flag=0
# for n in range(0,len(arr)):
#     if arr[n]==element:
#         flag=1
#         break
# if flag==0:
#     print("Element not found")
# else:
#     print("element found")

#EFFICIENT WAY

arr=[1,2,3,5,6,7,8]
element=6
arr.sort()                      #we need to sort before doing this method
low=0
upp=len(arr)-1
flag=0
while (low<upp):
    mid=(low+upp)//2            #mid=3                  mid=4
    if arr[mid] == element:       # 5 (arr[4]) != 6     6=6
        flag=1
        break
    elif element > arr[mid]:      #6>5 true
        low=mid+1               #low=4
    elif element < arr[mid]:      #
        upp=mid-1               #
print("Element found" if flag==1 else "not found")






