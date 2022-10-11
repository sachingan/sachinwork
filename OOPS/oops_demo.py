# class person:
#     name=str
#     age=int
#     gender=str
#     def set_person(this,name,age,gender):
#         this.name=name
#         this.age=age
#         this.gender=gender
#     def print_person(this):
#         print(this.name,this.age,this.gender)
#
# p1=person()
# p2=person()
# p1.set_person("sachin",25,"male")
# p1.print_person()
#
# class student_details:
#     name=str
#     age=int
#     gender=str
#     education = str
#     def __init__(this,name,age,gender,edu):
#         this.name=name
#         this.age=age
#         this.gender=gender
#         this.xyz=edu
#     def print_stud_details(this):
#         print(this.name,this.age,this.gender,this.xyz)
#
# sachin_details=student_details("sachin",25,"male","BTECH")
#
# sachin_details.print_stud_details()
#
# class course:
#
#     def __init__(self,**kwargs):
#         self.course_nm=kwargs.get("course_nm")
#         self.course_idee=kwargs.get("course_id")
#         self.course_fee=kwargs.get("course_feae")
#     def print_stud_det(self):
#         print(f"course name {self.course_nm},course id {self.course_idee},course fee {self.course_fee}")
#
# stud=course(course_nm="btech",course_id="nss15me098",course_feae="8996")
# stud.print_stud_det()
#

class car:
    def __init__(self,**kwargs):
        self.mileage=kwargs.get("mileage")
        self.top_speed=kwargs.get("top_speed")
        self.rpm=kwargs.get("rpm")
        self.airbags=kwargs.get("airbags")
        self.varant=kwargs.get("variant")
    def print_car_details(self):
        print(self.top_speed,self.rpm,self.airbags,self.mileage,self.varant)

ob=car(mileage="18 kmph",top_speed="180 kmph",rpm= "220  rpm",airbags="2 airbags",variant="petrol variant")
ob.print_car_details()


