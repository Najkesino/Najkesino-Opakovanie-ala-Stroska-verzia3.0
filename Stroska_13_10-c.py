import tkinter, random
canvas = tkinter.Canvas(width = 300, height = 100, bg='white')
canvas.pack()

x = 50

def rytmus():
    global x
    slovo = entry1.get()
    for i in range(len(slovo)):
        if i%2 == 1:
            canvas.create_text(x, 30, text=slovo[i], fill='blue', font='Arial 15 bold')
            x += 20
        elif i%2 == 0:
            canvas.create_text(x, 30, text=slovo[i], fill='red', font='Arial 15 bold')
            x += 20

entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='OK', command=rytmus)
button1.pack()
