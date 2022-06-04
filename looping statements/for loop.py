# res=" "
# for i in range(0,99,11):
#     res+=str(i)
#     print(res)

# numbers=range(0,50,5)
# for i in numbers:
#     print(i)

num=50
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break
    if(flag==0):
        print("number is prime")
    else :
        print("number is not prime")



