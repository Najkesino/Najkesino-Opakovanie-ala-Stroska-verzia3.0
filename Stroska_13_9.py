import tkinter, random
canvas = tkinter.Canvas(width = 300, height = 100, bg='white')
canvas.pack()

x = 20
def funkcia():
    global x
    slovo = entry1.get()
    for i in range(len(slovo)):
        farba = random.choice(('red', 'blue', 'green', 'black', 'pink', 'lime'))
        canvas.create_text(x, 50, text=slovo[i], fill=farba, font='Arial 10 bold')
        x += 20

entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='OK', command=funkcia)
button1.pack()
