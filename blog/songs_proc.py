#highest rating song
#sad songs with random sample of 2
#which album contains most songs
#total no of albums
import json
import random
from functools import reduce
with open("songs.json",encoding="utf-8") as e:
    songs=json.load(e)
    print(e)

#total no of songs in album 1
tot_no_in_album=[song for song in songs if song["album"]=="album1"]
# print(len(tot_no_in_album))


#sad songs in sample of 2
sad_songs=[song["name"] for song in songs if song["mode"]=="sad"]
rand_sad=random.sample(sad_songs,2)
# print(rand_sad)

#highest rating song
highest=max(songs,key=lambda song:song["rating"])
# print((highest)["rating"])
rating_song=[song["name"] for song in songs if song["rating"]==highest["rating"]]
# print(rating_song)

top_song=reduce(lambda s1,s2:s1 if s1["rating"]>s2["rating"] else s2,songs)
# print(top_song["name"])


#total no of albums
total_albums=set([s["album"] for s in songs])
# print(len(total_albums))



#which album contains most songs
song_det=[song["album"] for song in songs]
print(song_det)
album={}
for alb in song_det:
    if alb in album:
        album[alb]+=1
    else:
        album[alb]=1

print(max(album.items(),key=lambda i:i[1]))



