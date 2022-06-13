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

mobiles=[
    [1000,"samsungA52","5G","AMOLED",27000,"samsung",12],
    [1001,"samsungA52S","4G","AMoLED",32000,"samsung",20],
    [1002,"redminote10","5G","LED",17000,"redmi",70],
    [1003,"redminote11pro","4G","superAMOLED",20000,"redmi",70],
    [1004,"samsungA72","4G","AMOLED",27000,"samsung",1],
    [1005,"samsungA53","4G","AMOLED",27000,"samsung",34],
    [1006,"samsungm52","4G","AMOLED",27000,"samsung",7],
    [1007,"samsungm53","4G","AMOLED",27000,"samsung",89],
    [1008,"samsungA22","4G","AMOLED",27000,"samsung",0],
    [1009,"iphone13","4G","AMOLED",97000,"apple",0],
    [1010,"oneplusnordce2","4G","AMOLED",23000,"oneplus",67]
]

#q1 total no of out_of_stock mobiles

#q2 total stock

#q3 print mobiles avl within price range 20k-30k

#q4 print all 5g phones

#q5 print samsung mobiles

#q6 print low cost mobiles

#q7 count of mobiles having display amoled

#q8 print all mobiles having stock >10

#9 print costly mobile

#10 print count of mobiles in desc price order

#q11 sort mobiles based on avl stock of desc order

#q12 is there any mobiles available at 10000

#q13 list all mobiles having same price