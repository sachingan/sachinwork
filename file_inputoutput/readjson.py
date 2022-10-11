import json             #json is a module

with open("blogs.json",encoding="utf-8") as f:
    data=json.load(f)
print(data)

print(len(data))

#no.of posts by user 1
no_of_post=[post for post in data if post["userId"]==1]
print(len(no_of_post))

#total likes for postid 6
likes_for_post=[len(post["liked_by"]) for post in data if post["postId"]==6]
print(likes_for_post[0])

#no. of post liked by user 2
posts_liked_by_user=[post for post in data if 2 in post["liked_by"]]
print(len((posts_liked_by_user)))