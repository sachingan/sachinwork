class p1:
    def m1(self):
        print("this is p1")


class p2(p1):
    def m2(self):
        print("this is p2")

class p3(p2):
    def m3(self):
        print("this is p3")

p3=p3()
p3.m3()
p3.m2()
p3.m1()
