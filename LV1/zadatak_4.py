fhand=open('song.txt')
dictionary={}

for line in fhand:
    line=line.rstrip()
    words=line.split()
    for word in words:
        if word in dictionary:
            dictionary[word]+=1
        else:
            dictionary[word]=1
count=0
for key, value in dictionary.items():
    if value==1:
        print(key)
        count+=1
print(count)