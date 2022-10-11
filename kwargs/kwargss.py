# def add_num(n1,n2):
#     return(n1+n2)
#
#
# print(add_num(10,20))
#
# def sub_num(*args):
#     print(args)



#
# dic={'n1': 10, 'n2': 20, 'n3': 30}
# print(dic.items())
# print(sum([v for k,v in dic.items()]))


def add_the(**kwargs):  #turns them into dictionary
    print(sum([v for k,v in kwargs.items()]))
    print(sum([v for v in kwargs.values()]))
    print(kwargs)

print(add_the(n1=10,n2=20,n3=30))



