#try-->blovk doubtful code
#except-->block handling code
#raise-->key word and custom error throw
#finally-->block clean up processing

# num1=int(input("Enter number 1:"))
# num2=int(input("Enter number 2:"))
#
# try:
#     res=num1/num2
#     print(f"Result is {res}")
# except Exception as e:
#     num2=int(input("Invalid number Entered! Enter another value"))
#     print(num1/num2)
#     # try:
#     #     res=num1/num2
#     # except Exception as e:
#     #     num2 = int(input("Invalid number Entered! Enter another value"))
#
# finally:                #any mandatory block that should work should be included in the finally block
#     print("db transaction")
#     print("file operation")


#raise-->used for creating custom error
# age=int(input("Enter age:"))
#
# if(age<18):
#     raise Exception("Not eligible for taking booster dose")
# else:
#     print("eligible")

phone_no=input("Enter phone number:")


if(len(phone_no)!=10):
    raise Exception("Invalid phone no.")
else:
    print("valid phone no")

