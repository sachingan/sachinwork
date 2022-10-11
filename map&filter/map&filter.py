lst=[11,2,30,4]
squares=list(map(lambda n:n**2,lst))
print(squares)

#add-1 if num>10,add+1 if num<10

random=list(map(lambda n:n+1 if n<10 else n-1,lst))
print(random)

divis_by_2=list(filter(lambda n:n%2==0,lst))
print(divis_by_2)

from functools import reduce

sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)

product=reduce(lambda  n1,n2:n1*n2,lst)
print(product)

max_num=print(reduce(lambda n1,n2:n1 if n1>n2 else n2,lst))
min_num=print(reduce(lambda n1,n2:n1 if n1<n2 else n2,lst))
