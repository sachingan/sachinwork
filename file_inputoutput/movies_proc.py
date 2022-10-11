#no of movies ireleased in 2022
#no of malayalam movies
#theatre released movies
#list of movies whose rating greater than 5

movies=open("movies.txt")
movie_details=[movie.rstrip("\n").split(",") for movie in movies]
print(movie_details)

movie_rel_2022=[m[0] for m in movie_details if m[1]=="2022"]
print(len(movie_rel_2022))

mallu_movies=[movie[0] for movie in movie_details if movie[-2]=="malayalam"]
print(mallu_movies)

theatre_movies=[movie[0] for movie in movie_details if movie[-1]=="theatre"]
print(theatre_movies)

rating_gt_5=[m[0] for m in movie_details if m[2]=="5"]
print(rating_gt_5)

movie_by_year={}        #{2022:a,2021:b,2020:c}
for movie in movie_details:
    if movie[1] in movie_by_year:
        movie_by_year[movie[1]]+=1
    else:
        movie_by_year[movie[1]]=1

print(movie_by_year)
print(max(movie_by_year.items(),key=lambda i:i[1]))
