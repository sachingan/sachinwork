mobile_det=open("mobiles.txt")
all_mobiles=[]
for mob in mobile_det:
    mob_det=mob.rstrip("\n").split(",")
    all_mobiles.append(mob_det)

print(all_mobiles)

max_price=max(all_mobiles,key=lambda mob:int(mob[-1]))
print(max_price)


