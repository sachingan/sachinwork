# bands={"name":"pink floyd","genre":"psycadelic rock","year":"1980","members":4}
#
# print(bands["name"])
# print(bands["genre"])
#
# studet_details={"name":"sachin","date_of_birth":"06/11/1996","classs":"10","div":"A"}
#
# print(studet_details["name"])
#
# print("blood_group" in studet_details)
#
# studet_details["blood_group"]="O+ve"
# print(studet_details)
#
# #to update
#
# studet_details["classs"]="engineering"
# print(studet_details)

acount={"name":"sachin","acount_type":"sb","netbanking":"no","age":"25","balance":10000000,"disabled":"no"}
print("Acount holder name:",(acount["name"]))
print("Net balance:",(acount.get("balance")))
acount["balance"]+=10000000
print("new balance",(acount["balance"]))

if "disabled" in acount:
    acount["disabled"] ="yes"
else:
    acount["disabled"]="no"

print(acount)

if acount["balance"]>100000:
    acount["balance"]=acount["balance"]-(0.25*acount["balance"])
else:
    acount["balance"]=acount["balance"]-(0.1*acount["balance"])
print(acount)
