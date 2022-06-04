# num1=10
# num2=20
# if(num1>num2):
#     print(f"{num1} is largest")
# elif(num2>num1):
#      print(f"{num2} is largest")
# else:
#     print("same no.")
 # print({num1} if num1>num2 else {num2})
num1=23
num2=23
num3=456
if ((num1>num2) & (num1<num3)) or ((num1<num2) & (num1>num3)):
    print("num1 m")
elif ((num2>num1) & (num2<num3)) or ((num2<num1) & (num2>num3)):
    print("num2 m")
elif ((num3>num1) & (num3<num2)) or((num3<num1) & (num3>num2)):
    print("num3 m")
elif ((num1==num2)&((num1<num3)or(num1>num3))):
    print("num1and num2 are s")
elif (num1==num2==num3):
    print(same)