vstup = input('Zadaj text:')
sifra = ''

#cezarova sifra s psunom 2

for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)+5)
    if znak == 'y':
        novyznak = 'a'
    if znak == 'z':
        novyznak = 'b'
    sifra = sifra+novyznak
print(sifra)

#cezarova sifra s posunom 3
'''
for znak in vstup:
    novyznak = znak
    if 'a' <= znak <= 'y':
        novyznak = chr(ord(znak)+3)
    if znak == 'x':
        novyznak = 'a'
    if znak == 'y':
        novyznak = 'b'
    if znak == 'z':
        novyznak = 'c'
    sifra = sifra+novyznak
print(sifra)
'''
