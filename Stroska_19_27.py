#desifrovanie s 2 posunmi
vstup = input('Zadaj text:')
sifra = ''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)-2)
    if znak == 'a':
        novyznak = 'y'
    if znak == 'b':
        novyznak = 'z'
    sifra = sifra+novyznak
print(sifra)

#desifrovanie s 3 posunmi
'''
vstup = input('Zadaj text:')
sifra = ''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)-3)
    if znak == 'a':
        novyznak = 'x'
    if znak == 'b':
        novyznak = 'y'
    if znak == 'c':
        novyznak = 'z'
    sifra = sifra+novyznak
print(sifra)
'''
