word="hello hai hello hai"
text=word.split(" ")
print(text)
w_count={}
for w in text:
    if w in w_count:
       w_count[w]+=1

    else:
        w_count[w]=1
print(w_count)


