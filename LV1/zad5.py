fhand=open('SMSSpamCollection.txt')
ham_words=0
ham_lines=0
spam_words=0
spam_lines=0
count=0
for line in fhand:
    line = line.rstrip()
    words = line.split()
    if words[0]=="ham":
        ham_lines+=1
        ham_words+=len(words)-1
        
    else:
        spam_lines+=1
        spam_words+=len(words)-1
        if words[len(words)-1].endswith("!"):
            count+=1 

print(ham_words/ham_lines)
print(spam_words/spam_lines)
print(count)
fhand.close()