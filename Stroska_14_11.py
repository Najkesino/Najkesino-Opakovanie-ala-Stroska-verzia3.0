import tkinter, random
canvas = tkinter.Canvas(width = 300, height = 100, bg='white')
canvas.pack()

x = 30
minus = 270

def Bengoro():
    canvas.delete('all')
    global x, minus
    slovo = entry1.get()
    for i in range(len(slovo)):
        for neviem in range(10):
            canvas.delete('pismeno'+str(i))
            canvas.create_text(x+minus, 50, text=slovo[i], fill='blue', font='Arial 20 bold', tags='pismeno'+str(i))
            minus -= 27
            canvas.update()
            canvas.after(10)
        x += 20
        minus = 270
        canvas.update()
        canvas.after(1000)
    x = 30
    minus = 270
    canvas.after(1000, Bengoro)

entry1 = tkinter.Entry()
entry1.pack()
button1 = tkinter.Button(text='OK', command=Bengoro)
button1.pack()
