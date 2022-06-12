# lst=[2,3,4,6,5]
#
# sum=50
# count=1
#
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum == sum:
#             print(f"{lst[i]} & {lst[j]} are pairs")
#
#
#         count+=1
# print("total iterations is ",count)     #Here the processs is inefficient sice the programme runs a lot of iterations


lst=[2,3,4,6,5]
element=7
low=0
upp=len(lst)-1
count=1

while(low<upp):
    cur_sum = lst[low] + lst[upp]
    if cur_sum==element:
        print(f"{lst[low]} & {lst[upp]} are pairs")
        break

    elif(cur_sum<element):
        low+=1
    elif cur_sum>element:
        upp-=1
    count+=1
print(f"iterations are {count}")