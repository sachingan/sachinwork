# num=8
# temp=""
# if(num%3==0):
#     temp+="fizz"
#
# if(num%5==0):
#     temp+="buzz"
#
# if(num%5!=0 or num%3!=0):
#     print("indivisible by 3,5 and 15")
#
# print(temp)


# num=8
# if num%15==0:
#     print("fizzbuzz")
# else:
#     if num%5==0:
#         print("fizz")
#     else:
#         print("buzz")


num = 8
temp = ""
if(num%3==0):
    temp=temp+"fizz"
if(num%5==0):
    temp=temp+"buzz"
else:
    print("not correct dude")
print(temp)