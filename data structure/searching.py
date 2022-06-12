arr=[1,2,3,14,15,16,65,78,89]
element=10
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

flag=0
for n in range(0,len(arr)):
    if arr[n]==element:
        flag=1
        break
if flag==0:
    print("Element not found")
else:
    print("element found")
