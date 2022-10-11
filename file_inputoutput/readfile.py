
f=open("abc.txt")
# lines=[line for line in f]
# print(lines)

#here we get output as ['hello hai hello\n', 'hello hai hello\n', 'hello hello']
#here we have to use remove \n from the right side because we dont need it.
#so we use a method in the dir(str) called rstrip which is used to remove anything on the right side

# print(dir(str))
# output=[line.rstrip("\n") for line in f]
# print(output)

#To write
# f=open("abc.txt","w")   #w to write on abc.txt file
#
# lst=["javascript","python","c++","hai",]

# for lang in lst:
#     lang+="\n"
#     f.write(lang)


\









