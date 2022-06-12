
lst=[10,11,12,14,15,16,17,12,12,12,12,100]

#
oddlst=[]
# for i in lst:                 #.append - To add an element in the last position
#     if i%2!=0:
#         oddlst.append(i)
#
# print(oddlst)

for i in lst:
    if i%2==0:
        oddlst.append(i)
print(oddlst)
oddlst.sort()       #.sort() - To sort in ascendiing order
print(oddlst)
oddlst.sort(reverse=True)
print(oddlst)       #.sort(reverse=True) - To sort in descenfding order
