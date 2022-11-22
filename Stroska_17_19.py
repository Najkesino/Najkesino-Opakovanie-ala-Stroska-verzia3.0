url = input('Zadaj URL adresu: ')
protokol = url.split(':')
najdom = url.split('.')
najdom = najdom[2]
das = url.split('/')
print('Protokol: '+protokol[0])
print('Doména najvyššej úrovne: '+najdom[0:3])
print('Doménová adresa servera: '+das[2])

#https://shop.pythonsoftware.com/download/examples
