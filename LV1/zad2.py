try:
    broj=float(input("Unesite broj: "))
    if broj<0.0 or broj>1.0:
        print("nije unesen broj iz intervala")
    elif broj<0.6:
        print("F")
    elif broj<0.7:
        print("D")
    elif broj<0.8:
        print("C")
    elif broj<0.9:
        print("B")
    else:
        print("A")
except:
    print("Nije unesen broj")    