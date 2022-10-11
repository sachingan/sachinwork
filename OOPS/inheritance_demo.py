class parent:
    def car(self):
        print("MG gloster")
    def work(self):
        print("successful")

class child(parent):                    # here within the bracket parent is given which means that child
    pass                                # also inherits all the properties of the parent class

ob=child()
ob.car()