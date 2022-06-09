# expenses = [1,10,1.6, True ,"hello"]
# # print(expenses)
#
#
# # print(expenses[0])
# # print(expenses[2])
# # print(expenses[-1])
#
#
# # for amount in expenses:
# #     print(amount)       #1,10,1.6,True,hello
#
# for i in range(0,5):
#     print(expenses[i])
#
# print(len(expenses))    #len() is used to return the length of an object
#
# for i in range(0,len(expenses)):
#     print(expenses[i])


# numbers=[1,2,3,4,5,6,7,8,9,10]
#print even numbers

# for num in numbers:
#     if (num%2==0):
#         print(num)

# for num in numbers:
#     if num<5:
#         print(num-1)        #0,1,2,3
#     elif(num==5):
#         print(num)          #5
#     else:
#         print(num+1)        #7,8,9,10,11



#count of numbers between 4 to 9
# numbers=[1,2,3,4,5,6,7,8,9,10]
# count=0
# for num in numbers:
#     if num>=4 and num<10:
#         count+=1
#
# print(count)
#
# count=0
# for num in numbers:
#     if num in range(4,10):
#         count+=1
# print(count)

# numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
#neg count
#pos count
#zero count
# neg=0
# ze
# p_sum=0
for num in numbers:
    if num<0:
        n_sum+=num

    else:
        p_sum+=sum
print(neg)
print(zero)
print(pos)

# #OR
#
# print(len([n for n in numbers if n>0]))
#


numbers = [-1, 2, 0, 3, 4, 5, -2, 0, 3, 4, -5, 0, 7, 0]

sum=0
for n in numbers:
    sum+=n
print(sum)