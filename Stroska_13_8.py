veta = input('Zadaj vetu: ')
if veta[-1] == '.':
    print('Je to oznamovacia veta.')
elif veta[-1] == '!':
    print('Je to rozkazovacia veta.')
elif veta[-1] == '?':
    print('Je to opytovacia veta.')
