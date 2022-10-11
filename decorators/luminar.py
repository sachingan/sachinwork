class employee:
    def __init__(self,**kwargs):
        self.Employe_Id=kwargs.get("Employe_Id")
        self.Name=kwargs.get("Name")
        self.Role=kwargs.get("Role")
    def __str__(self):
       return self.Name

class department:
    def __init__(self,**kwargs):
        uuser=kwargs.get("user")
        if uuser.Role=="Admin":
            self.dept_name=kwargs.get("dept_name")
            self.user=kwargs.get("user")
        else:
            print("ACCESS DENIED")

    def __str__(self):
        return self.dept_name

emp=employee(Employe_Id=666,Name="sachin",Role="not admin")
dept=department(dept_name="Mechanical",user=emp)
print(emp)
print(dept)
print(dept.user)

