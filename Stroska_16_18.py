rc = input('Rodné číslo: ')
if int(rc[0:2])<=22:
    if int(rc[2:4])>12:
        p = 'Žena'
        dat = rc[4:6]+'.'+str(int(rc[2:3])-5)+rc[3:4]+'.'+'20'+rc[0:2]
    elif int(rc[2:4])<=12:
        p = 'Muž'
        dat = rc[4:6]+'.'+rc[2:4]+'.'+'20'+rc[0:2]
elif int(rc[0:2])>22:
    if int(rc[2:4])>12:
        p = 'Žena'
        dat = rc[4:6]+'.'+str(int(rc[2:3])-5)+rc[3:4]+'.'+'19'+rc[0:2]
    elif int(rc[2:4])<=12:
        p = 'Muž'
        dat = rc[4:6]+'.'+rc[2:4]+'.'+'19'+rc[0:2]
print('Dátum narodenia: '+dat)
print('Pohlavie: '+p)
