import random

heslo = ''

for i in range(8):
    heslo = heslo+chr(random.randint(97, 123))
for i in range(random.randint(1, 8)):
    cislo = random.randint(1, 7)
    if ord(heslo[cislo])<66 or ord(heslo[cislo])>81:
        heslo = heslo[0:cislo]+heslo[cislo].upper()+heslo[cislo+1:]
print(heslo)
