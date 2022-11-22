import random

heslo = ''

for i in range(3):
    heslo = heslo+chr(random.randint(66, 81))
for i in range(2):
    heslo = heslo+chr(random.randint(48, 57))
for i in range(3):
    heslo = heslo+chr(random.randint(97, 123))
print(heslo)
