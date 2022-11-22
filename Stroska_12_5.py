slovo1 = input('Zadaj slovo: ')
slovo2 = input('Zadaj druhé rovnako dlhé slovo: ')
spojenie = ''
if len(slovo1)==len(slovo2):
    for i in range(len(slovo1)):
        spojenie = spojenie+slovo1[i]+slovo2[i]
else:
    print('Nezadal si rovnako dlhé slová.')
print(spojenie)
