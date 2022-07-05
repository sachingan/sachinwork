result=[
    {"district":"tvm","win":98,"A+":45000},
    {"district":"ktm","win":95,"A+":44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90, "A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"ksd","win": 99, "A+": 58000},
    {"district":"pkd","win": 95, "A+": 50000},
    {"district":"mpm","win":90,"A+":4500}
]

#dist with max win
print(max(result,key=lambda item:item["A+"]))

#sort in order of win %

print(sorted(result,key=lambda item:item["win"],reverse=True))

#dist with min A+

print(min(result,key=lambda item:item["A+"]))

#total no. of A+ winners

aplus=[ distwise["A+"] for distwise in result ]
print(sum(aplus))