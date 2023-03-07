fhand=open('song.txt')
rjecnik={}
for line in fhand:
    line=line.rstrip()
    line=line.lower()
    words=line.split()
    for word in words:
        if word in rjecnik:
            rjecnik[word]+=1
        else:
            rjecnik[word]=1
#print(rjecnik)
count=0
for word in rjecnik:
    if rjecnik[word]==1:
        count+=1
        print(word)
print(count)
fhand.close()