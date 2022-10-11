dic={"k1":20,"k2":"hello","k3":True}

# print(dic.items())
for k,v in dic.items():
    print(k,v)

for v in dic.values():
    print(v)


# dic.pop("k3")
# print(dic)

print(dic.get("k2"))




