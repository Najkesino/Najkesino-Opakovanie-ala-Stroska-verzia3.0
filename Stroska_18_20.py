import random
heslo = ''
for i in range(8):
    heslo = heslo+chr(random.randint(97, 123))
print(heslo)

