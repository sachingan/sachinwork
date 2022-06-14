lst=[1,2,3,3,4,5,6,7,6,6,5,5,1]
#to remove the duplicatees convert the above list into set

st=set(lst)
# print(st)           #output={1,2,3,4,5,6,7}

st1={1,2,4,5,6,8}
st2={6,7,8,9}

st1.add(3)
# print(st1)
st1.update(st2)
print(st1)

union_set=st1.union(st2)
print(union_set)
intersection_set=st1.intersection(st2)
print(intersection_set)
diff_Set=st1.difference(st2)
print(diff_Set)

students={"ram","askay","arjun","ashik","allu","anson"}
pass_students={"ram","anson","ashik"}

fail_students=students.difference(pass_students)
print(fail_students)