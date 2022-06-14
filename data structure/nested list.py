lst=[
    [10,11],
    [13,45],
    [50,15],
    [60,16]
]

fltn_lst=[num for s_list in lst for num in s_list]
print(fltn_lst)

gr_th_sixt= [ num for num in fltn_lst if num>16]
print(gr_th_sixt)

odd_num=[num for num in fltn_lst if  num%2!=0]
print(odd_num)

even_num=[num for num in fltn_lst if num%2==0]
print(even_num)
print(sum(even_num))

arr_list=[ num+1 if num>25 else num-1 for num in fltn_lst ]
print(arr_list)
arr_list.sort()
print(arr_list)

#print all numbers greater than 16

# for arr in lst:             #arr=[10,11],[13,45],[50,15][60,16]
#     for num in arr:         #num=10,11,13,45,50,15,60,16
#         if num>16:
#             print(num)
# print(max(lst)[1])


# flatten_list=[]
# for arr in lst:
#     for num in arr:
#         flatten_list.append(num)
# print(flatten_list)
# print(max(flatten_list))
