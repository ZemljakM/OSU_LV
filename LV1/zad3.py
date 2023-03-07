lista = []
string = True

while string:
    unos = input()
    if unos == "Done":
        break
    try:
        broj = float(unos)
        lista.append(broj)
    except:
        print("nije unesen broj")

print("kolicina brojeva: ", len(lista))
print("Srednja: ", sum(lista)/len(lista))
print("Min: ", min(lista))
print("Max: ", max(lista))
lista.sort()
print(lista)
