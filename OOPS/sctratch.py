# num=[9,39,8,78]
#
# master_word="abbcceddffggt"
# chk_word="egg"
#
# emt=[]
# for w in chk_word:
#     for m in master_word:
#         if w==m:
#             emt.append(w)
#
# if emt
#     print(emt)

from blog.models import users,posts
# print(users)
session={}

def signin_required(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("SIGN IN REQUIRED")
    return wrapper


def authenticate(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user=[details for details in users if details["username"]==username and details["password"]==password]
    return user

# print(authenticate(username="akhil",password="Password@123"))

#GET--to update
#POST--to create
#PUT/PATCH--to update
#DELETE--to delete


class loginview:

    def put(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]

        # print(session)

class postlistview:         #to view posts one must be signed in
    @signin_required
    def get(*args,**kwargs):
        return posts                                # if "user" in session: ------>Convert this into a decorator function
    def post(self,*args,**kwargs):                  #  return posts
        post_data=(kwargs.get("data"))                   # else:
        userId=session["user"]["id"]                     #  #print("Signin required")
        post_data["userId"]=userId
        posts.append(post_data)
        print("posted successfully")
        print(posts[-1])


class mypostlistview:
    @signin_required
    def get(self,*args,**kwargs):
        userid=session["user"]["id"]
        my_posts=[post for post in posts if post["userId"]==userid]
        return my_posts

class addlike:
    @signin_required
    def post(self,*args,**kwargs):
        postid=kwargs.get("postId")
        post=[post for post in posts if post["postId"]==postid]
        if post:
            post=post[0]
            userId=session["user"]["id"]
            post["liked_by"].append(userId)
            print(post["liked_by"])





login_check=loginview()
login_check.put(username="anu",password="Password@123")
my_post_det=postlistview()

my_post={"postId":9,"title":"MY POST","content":"I AM SACHIN GANESH H","liked by":"[]"}
my_post_det.post(data=my_post)

likes=addlike()
likes.post(postId=1)



my_posts=mypostlistview()
# print(my_posts.get())












