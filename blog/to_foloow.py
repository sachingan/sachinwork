import json
import random

try:
    with open("../blog/users.json",encoding="utf-8") as e:
        data=json.load(e)
        print(data)

        all_users=[user["id"] for user in data]
        my_followings=[user["followers"] for user in data if user["username"]=="akhil"][0]
        my_id=[user["id"] for user in data if user["username"]=="akhil"].pop()
        to_follow=set(all_users)-set(my_followings)
        to_follow.remove(my_id)
        print(to_follow)
        suggestions=random.sample(to_follow,2)
        print(suggestions)

except Exception as e:
    print(e.__class__)

st={2,3,4,5,9,1}
lst=[*st]       #star is added for "destructuring" or convvert from set to list
print(lst)
sett={*lst}
print(sett)