fhand=open('SMSSpamCollection.txt', encoding="utf8")
sum_ham=0
count_ham=0
sum_spam=0
count_spam=0
count=0
for line in fhand:
    line=line.rstrip()
    words=line.split()
    if words[0]=="ham":
        sum_ham+=len(words)-1
        count_ham+=1
    else:
        sum_spam+=len(words)-1
        count_spam+=1
        if words[len(words)-1].endswith('!'):
            count+=1

print("Ham: ", sum_ham/count_ham)
print("Spam: ", sum_spam/count_spam)
print(count)