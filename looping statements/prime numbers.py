# num=8
# flag=1
# for i in range(2,num):        #2,3,4,5,6,7
#     if (num%i==0) :           #8%2==0,8%3!=0,8%==0,8%5!=0,8%6!=0,8%7!=0
#         flag=0                #flag=0
#         break
#
# if(flag==0):
#     print(f"{num} is not a prime number")
# else:
#     print(f"{num} is a prime number")


num1=2
num2=13
flag=1
for i in range(num1,num2): #2,3,4,5,6,7,8,9
    if(num2%i==0):          #3,
       flag=0
       break
if(flag==0):
    print(f"{num2} is not a prime number")
else:
    print(f"{num2 } is a prime number")
