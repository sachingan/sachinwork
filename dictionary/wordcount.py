# text="hai hello hai hello"

# words=text.split(" ")
# print(words)
#
# word_count={}
# for w in words:
#     if w in word_count:
#         word_count[w]+=1
#     else:
#         word_count[w]=1
# print(word_count)

#print first recurvise in ABACCD

# text="ABACCD"

# wc={}
# for w in text:
#     if w in wc:
#         print("The first recursive charecter is",w)
#         break
#
#     else:
#         wc[w]=1


#second recursive charecter

# text="ABACCD"
# word_count={}
# rec_elements=[]
#
# for word in text:
#     if word in word_count:
#         rec_elements.append(word)
#     else:
#         word_count[word]=1
# print(f"second recursive charecter:{rec_elements[1]}")

#MOST RECURSIVE CHARECTER

text="ABACCDC"
word_count={}
emt=[]
for word in text:
    if word in word_count:

        emt.append(word)
    else:
        word_count[word]=1
print(word_count)
print(emt)



#sorting dictionary based on value

# word_count={"a":2, "b":5,"c":2,"d":4,"e":2 }
# wc_list=word_count.items()
# print(f"wc list is:{wc_list}")
# print(sorted(wc_list,key=lambda item:item[1],reverse=True))
#
# print(max(wc_list,key=lambda p:p[1]))
#
# print(min(wc_list,key=lambda i:i[1]))

