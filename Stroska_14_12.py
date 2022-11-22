veta = input('Zadaj vetu: ')

pocet_s = 0
pocet_pis = 0
miesto = 0
naj = ''

veta = veta.split(' ')
pocet_s = len(veta)
for i in range(len(veta)):
    if len(naj) < len(veta[i]):
        naj = veta[i]
        miesto = i+1
        
pocet_pis = len(naj)
print('Pocet slov je: '+str(pocet_s))
print('Najdlhsie slova: '+naj)
print('Pocet pismen najdlhsieho slova je: '+str(pocet_pis))
print('Miesto najdlhsieho slova je: '+str(miesto))
