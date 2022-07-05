
mobiles=[
    [1000,"samsungA52","5G","AMOLED",27000,"samsung",12],
    [1001,"samsungA52S","4G","AMoLED",32000,"samsung",20],
    [1002,"redminote10","5G","LED",17000,"redmi",70],
    [1003,"redminote11pro","4G","superAMOLED",20000,"redmi",70],
    [1004,"samsungA72","4G","AMOLED",27000,"samsung",1],
    [1005,"samsungA53","4G","AMOLED",27000,"samsung",34],
    [1006,"samsungm52","4G","AMOLED",27000,"samsung",7],
    [1007,"samsungm53","4G","AMOLAD",27000,"samsung",89],
    [1008,"samsungA22","4G","AMOLED",27000,"samsung",0],
    [1009,"iphone13","4G","AMOLED",97000,"apple",0],
    [1010,"oneplusnordce2","4G","AMOLED",23000,"oneplus",67]
]

#q1 total no of out_of_stock mobiles

out_of_stock=[mob for mob in mobiles if mob[-1]==0]
# print(out_of_stock)


#q2 total stock
total_stock=[mob[-1] for mob in mobiles]
# print(sum(total_stock))

#q3 print mobiles avl within price range 20k-30k
mob_range=[mob for mob in mobiles if mob[4]>=20000 and mob[4]<=30000]
# print(mob_range)

mob_range=[mob for mob in mobiles if mob[4] in range(20000,30001)]
# print(mob_range)


#q4 print all 5g phones
fiveg_phones=[mob for mob in mobiles if mob[2]=="5G"]
# print(fiveg_phones)

#q5 print samsung mobiles

samsung=[mob[1] for mob in mobiles if mob[-2]=="samsung"]
# print(samsung)

#q6 print low cost mobiles
low_cost=min([mob[4] for mob in mobiles])
lc=[mob for mob in mobiles if mob[4]==low_cost]
# print(lc)
#q7 count of mobiles having display amoled
amoled_count=[mob for mob in mobiles if mob[3]=="AMOLED"]
# print(len(amoled_count))



#q8 print all mobiles having stock >10
stock_gt_ten=[mob for mob in mobiles if mob[-1]>50]
# print(stock_gt_ten)


#9 print costly mobile
costly_mob=[mob[4] for mob in mobiles]
costly_mob.sort()
cost_mob=[mob for mob in mobiles if mob[4]==costly_mob[-1]]
# print(cost_mob)



#10 print count of mobiles in desc price order
desc_price=[mob[4] for mob in mobiles]
# print(sorted(desc_price,reverse=True))

#q11 sort mobiles based on avl stock of desc order
# print(sorted([mob[-1] for mob in mobiles],reverse=True))

#q12 is there any mobiles available at 10000
flag=0
for mob in mobiles:
    if mob[4]==32000:
        flag=1
        break
if flag==0:
    print("NOT available")
else:
    print(" available")


#q13 list all mobiles having same price

