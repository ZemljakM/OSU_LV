def total_euro(sati, placeno):
    ukupno=sati*placeno
    return ukupno

sati=float(input("Unesite broj radnih sati: "))
placeno=float(input("Unesite iznos po radnom satu: "))

print("Ukupan iznos: ", total_euro(sati,placeno))
