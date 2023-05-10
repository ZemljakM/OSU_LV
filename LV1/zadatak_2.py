try:
    number=float(input("Unesite broj: "))
    if number<0.0 or number>1.0:
        print("Nije broj iz intervala")
    elif number<0.6:
        print("F")
    elif number<0.7:
        print("D")
    elif number<0.8:
        print("C")
    elif number<0.9:
        print("B")
    else:
        print("A")
except:
    print("Nije unesen broj")

