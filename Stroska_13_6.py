spojenie = input('Zadaj spojenie dvoch slov: ')
slovo1 = ''
slovo2 = ''
for i in range(len(spojenie)):
    if (i%2) == 0:
        slovo1 = slovo1+spojenie[i]
    elif (i%2) == 1:
        slovo2 = slovo2+spojenie[i]
print(slovo1)
print(slovo2)
