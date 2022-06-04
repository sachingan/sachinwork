num=123
sum=0
while(num>0):
    l_d=num%10
    cube=l_d**3
    sum=sum+cube
    num//=10
print(sum)