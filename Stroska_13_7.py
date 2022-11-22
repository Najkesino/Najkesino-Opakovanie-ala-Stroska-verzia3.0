slovo1 = input('Zadaj slovo: ')
slovo2 = input('Zadaj druhé slovo: ')
spojenie = ''
if len(slovo1) >= len(slovo2):
    for i in range(len(slovo2)):
        spojenie = spojenie+slovo1[i]+slovo2[i]
    spojenie = spojenie+slovo1[len(slovo1)-len(slovo2)::]
elif len(slovo1) < len(slovo2):
    for i in range(len(slovo1)):
        spojenie = spojenie+slovo1[i]+slovo2[i]
    spojenie = spojenie+slovo2[len(slovo2)-len(slovo1)::]
print(spojenie)
