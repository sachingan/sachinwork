master_word="aabbccaadtdteegg"
chk_word="egg"
mw_dic={}

for word in master_word:
    if word in mw_dic:
        pass
    else:
        mw_dic[word]+=1