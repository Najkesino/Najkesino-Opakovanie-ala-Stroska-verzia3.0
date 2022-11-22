import tkinter, random
canvas = tkinter.Canvas(width = 300, height = 100, bg='white')
canvas.pack()

x = 50
uhol = 0

def rytmus():
    global x, uhol
    slovo = entry1.get()
    for i in range(len(slovo)):
        canvas.create_text(x, 30, text=slovo[i], fill='blue', font='Arial 15 bold', angle = uhol)
        x += 20
        uhol -= 360//(len(slovo)-1)

entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='OK', command=rytmus)
button1.pack()
