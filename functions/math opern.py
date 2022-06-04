# def add_numbers(n1,n2):
#     return(n1+n2)
# print(add_numbers(10,5))
# n1=3
# def cube(n1):
#     return(n1**3)
# print(cube(n1))
#
# def smart_sub(n1,n2):
#    return n1-n2 if(n1>n2) else n2-n1
# print(smart_sub(10,20))

# def validate_gmail(email):
#    return(email.endswith("@gmail.com"))
# print(validate_gmail("das@gmail.om"))


# def factorial(n1):
#    fact=1
#    for i in range(1,n1+1):
#       fact=fact*i
#    return fact
# print(factorial(4))

add=lambda n1,n2:n1+n2
print(add(10,5))

cube=lambda n:n**3
print(cube(2))

smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(1,6))