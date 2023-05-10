end=False
lista=[]

while end!=True:
    try:
        unos=input("Unesi broj: ")
        if unos=="Done":
            break
        else:
            broj=float(unos)
            lista.append(broj)
    except:
        print("Nije unesen broj")

print(len(lista))
print(sum(lista)/float(len(lista)))
print(min(lista))
print(max(lista))
lista.sort()
print(lista)