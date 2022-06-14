
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

out_of_stock=[oos for oos in mobiles if oos[6]==0]
print(out_of_stock)
print(len(out_of_stock))


#q2 total stock

# tot_stock = [mob[-1] for mob in mobiles]
# print(tot_stock)
# print(sum(tot_stock))

#q3 print mobiles avl within price range 20k-30k

# avl_range=[mob for mob in mobiles if mob[4]>=20000 and mob[4]<=30000]
# print(avl_range)
# #OR
# avl_range=[mob for mob in mobiles if mob[4] in range(20000,30000)]
# print(avl_range)

#q4 print all 5g phones

# four_g_phones=[mob for mob in mobiles if mob[2]=="5G"]
# print(four_g_phones)

#q5 print samsung mobiles

# samsung=[mob for mob in mobiles if mob[-2]=="samsung"]
# print(samsung)

#q6 print low cost mobiles

# lowest_price=min([mob[4] for mob in mobiles])
# min_pro=[mob for mob in mobiles if mob[4]==lowest_price]
# print(min_pro)
# #OR
low_cost=min(mobiles,key=lambda mob:mob[4])
print(low_cost)


#q7 count of mobiles having display amoled
amoled_count=[mob for mob in mobiles if mob[3]=="AMOLED"]
print(len(amoled_count))

#q8 print all mobiles having stock >10

high_stock=[mob for mob in mobiles if mob[-1]>50]
print(high_stock)

#9 print costly mobile
# mobiles.sort(reverse=True,key=lambda mob:mob[4])
# print(mobiles[0])

costly_pro=max(mobiles,key=lambda mob:mob[4])
print(costly_pro)

#10 print count of mobiles in desc price order

#q11 sort mobiles based on avl stock of desc order

#q12 is there any mobiles available at 10000

#q13 list all mobiles having same price

