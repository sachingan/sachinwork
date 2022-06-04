


def prime_number(n):
    flag=0
    for i in range(2, n):
     if(n%i==0):
        flag=1
        break
    return  flag==0


def is_prime(low,upp):
    for num in range(low,(upp+1)):
        print((num) if prime_number(num) else):



