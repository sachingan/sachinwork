

# students=open("students.txt")
# all_students=[stud.rstrip("\n") for stud in students]
# # print(all_students)
#
# f_students=open("failed.txt")
# failed_Students=[stud.rstrip("\n") for stud in f_students]
# # print(failed_Students)
#
# passed_studs=open("passed_students.txt","w")
# passed_students=set(all_students)-set(failed_Students)
# print(passed_students)
#
# for stud in passed_students:
#     passed_studs.write(stud)

fp=open("passed_students.txt","a")
name="suraj"
fp.write(name)


