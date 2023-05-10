def total_euro(sati, zarada_po_satu):
    return sati*zarada_po_satu


x=float(input("Broj radnih sati: "))
y=float(input("Zarada po satu: "))
print("Ukupna zarada: ", total_euro(x,y))