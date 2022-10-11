class courses:
    course_name:str
    active_status:bool
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")
        self.user=kwargs.get("user")

    def __str__(self):
        return self.course_name

class batches:
    course:courses
    batch_code:str
    batch_name:str

    def add_batch(self,**kwargs):
         self.batch_name=kwargs.get("batch_name")
         self.batch_code=kwargs.get("batch_code")
         self.course_name=kwargs.get("course_name")

    def __str__(self):
        return self.batch_name

class students:
    student_name:str
    student_id:str
    phone_number:int
    batch:batches
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.student_id = kwargs.get("student_id")
        self.phone_number = kwargs.get("phone_number")
        self.batch_name = kwargs.get("batch_name")


    def __str__(self):
        return self.student_name

# course=courses()
# course.post(course_name="python",user="Admin")
# print(course)
# batch=batches()
# batch.post(batch_name="pythonmay22",batch_code="A52",course_name=course)
# print(batch)
# student_det=students.txt()
# student_det.post(student_name="sachin",student_id="s57",phone_number=9895970874,batch_name=batch)
# print(student_det)

django=courses()
django.add_course(course_name="django",active_status=True,user="student")

bigdata=courses()
bigdata.add_course(course_name="bigdata",active_status=True,user="student")

dj_b1=batches()
dj_b1.add_batch(batch_name="pythonmay22",batch_code="djmay2k22",course_name=django)
print(dj_b1)

bd1=batches()
bd1.add_batch(batch_name="bigdatamay22",batch_code="bdmay2k22",course_name=bigdata)

akshay=students()
akshay.add_student(student_name="akshay",student_id="A45",phone_number=96446118466,batch_name=bd1)
print(akshay)

amith=students()
amith.add_student(student_name="amith",student_id="A56",phone_number=9644659466,batch_name=bd1)
print(amith)

suresh=students()
suresh.add_student(student_name="suresh",student_id="S15",phone_number=9644611786,batch_name=dj_b1)
print(suresh)

ashwathi=students()
ashwathi.add_student(student_name="ashwathi",student_id="A20",phone_number=9644479536,batch_name=dj_b1)
print(ashwathi)

#to get ashwathis course name
print(ashwathi.batch.course.course_name)

