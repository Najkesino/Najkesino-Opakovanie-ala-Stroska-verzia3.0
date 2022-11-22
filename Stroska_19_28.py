vstup = input('Zadaj text:')
posun = input('Zadaj posun: ')
sifra = ''
for znak in vstup:
    novyznak = znak
    if (ord(znak)+int(posun)) > 122:
        novyznak = chr(97+(ord(znak)+int(posun)-123))
    if (ord(znak)+int(posun)) <= 122:
        novyznak = chr(ord(znak)+int(posun))
    sifra = sifra+novyznak
print(sifra)
