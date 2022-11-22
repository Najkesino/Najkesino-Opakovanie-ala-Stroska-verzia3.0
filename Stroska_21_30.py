from random import *

pocet_retazcov = input('Zadaj pocet slov ktore zadas: ')

for i in range(int(pocet_retazcov)):
    s = input('Zadaj nejaké slovo: ')
    novy = ''
    for i in range(len(s)):
        ktory = randrange(len(s))
        print('Odstraňujem znak', s[ktory])
        novy = novy+s[ktory]
        print('Zatiaľ som vytvoril:', novy)
        s = s[:ktory]+s[ktory+1:]
        print('Ešte zostali tieto znaky:', s)
print('Zamiešané slovo:', novy)
