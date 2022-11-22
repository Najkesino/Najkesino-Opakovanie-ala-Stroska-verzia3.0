vstup = input('Zadaj email: ')
tdl = vstup.split('.')
domena3 = tdl[-3]
domena3 = domena3.split('@')
server = vstup.split('@')
print('TDL: '+'.'+tdl[-1])
print('Server: '+server[-1])
print('User: '+server[0])
print('Domémy:')
print('Domána 1. úrovne je: '+tdl[-1])
print('Domána 2. úrovne je: '+tdl[-2])
print('Domána 3. úrovne je: '+domena3[-1])

#michal.velky@mail.pythonsoftware.net

