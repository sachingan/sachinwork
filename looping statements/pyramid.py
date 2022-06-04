num=7
for row in range(0,num):
    for col in range(0,num-row+1):
         print("",end=" ")
    for col in range(0,row+1):
         print("*",end=" ")
    print()

# num = 4
# for i in range(0,num):
#     for col1 in range(0, num - i-1):
#         print(end=" ")
#     for col2 in range(num - i-1, num - i ):
#         print("*", end=" ")
#     for col3 in range(0, i-1):
#         print("*",end=" ")
#     for col4 in range(num,num+1):
#         if (i!=0):
#             print("*", end=" ")
 # print()

                #
              #   #
            #   #   #
          #   #   #   #

for row in range(1,5):
  for col in range(1,5-row):
     print(" ",end=" ")
  for col in range (1,row+1):
      print("# ",end="  ")
  print()