from blog.models import  users,posts
# print(users)

session={}

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("Invalid!  Sign in required")
    return wrapper



def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user

# print(authenticate(username="akhil",password="Password@123"))

class loginview:

    def post(self,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]  #0th position because here we get a list of dictionary
                                     #of the single user details.so we take the
        print(session)                      #0th element of list,thereby removing the list.



class postlistview:
    @signin_required
    def get(self,*args,**kwargs):
        return posts



login=loginview()
login.post(username="akhil",password="Password@123")

postview=postlistview()
print(postview.get())
