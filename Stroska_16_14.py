spojenie = input('Zadaj spojenie slov: ')
slovo1 = spojenie[::2]
slovo2 = spojenie[::-2]
print(slovo1+' '+slovo2[::-1])

