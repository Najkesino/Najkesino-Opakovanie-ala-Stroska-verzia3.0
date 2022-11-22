vstup = input('Zadaj slovo: ')
for i in range(len(vstup)):
    print((len(vstup)-i)*'.'+vstup[:i+1])
