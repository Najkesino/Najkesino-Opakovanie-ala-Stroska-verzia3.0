vstup = input('Zadaj text:')
sifra = ''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)-1)
    if znak == 'a':
        novyznak = 'z'
    sifra = sifra+novyznak
print(sifra)
