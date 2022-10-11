def samrt_funct(fn):
    def inner_funct(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner_funct




@samrt_funct
def sub(n1,n2):
    return n1-n2
@samrt_funct
def div(n1,n2):
    return n1/n2

print(sub(20,45))
print(div(10, 20))
