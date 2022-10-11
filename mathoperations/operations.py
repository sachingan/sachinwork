# def add(n1,n2):
#     return n1+n2
#
# def sub(n1,n2):
#         return n1-n2
#
# def cube(n):
#     return n**3
#
#
# def prime_number(n):
#     flag=0
#     for i in range(2, n):
#      if(n%i==0):
#         flag=1
#         break
#     return (f"{n} is not a prime no") if flag==1 else (f"{n} is a prime no")
#
n1=0
n2=1
sum=0
n=int(input("Enter a number:"))
for i in range(0,n):
    print(sum,end=" ")
    n1=n2
    n2=sum
    sum=n1+n2




