from tkinter import *
import ii2 as ii


w = Tk()
w.title("ii")
w.resizable(True, True)
w.geometry('800x400')
txt = Entry(w)
txt.place(x=10, y=10, relwidth=0.75, bordermode='inside')
txt.focus()
symma = 0

def vv():
	ii.vvod()

def con():
	global symma
	ii.run('configinternet.ini')
	symma=0

def pt():
	global symma
	tekst.insert(1.0, ii.telo(txt.get(),chehvar.get()))
	w.update()
	a = txt.get()
	symma+= int(a)
	v = ' '*20+'Результат спустя ' +str(symma) +' шагов\n '
	tekst.insert(1.0,v)

def d():
	ii.var(chhh.get())

tekst = Text(font='arial 14', wrap=WORD)
tekst.place(x=10, y=40, relwidth=0.75, relheight=0.8)

chhh = IntVar()
chhh.set(1)
r =Radiobutton(text='прамая', variable=chhh, value=0, command=d, font='arial 12')
r.place(relx=0.83, y=10)
r2 = Radiobutton(text='относительная', variable=chhh, value=1, command=d, font='arial 12')
r2.place(relx=0.83, y=40)

but3 = Button(w, text='Обновить\nвходные', font='arial 14', bg='green', command=vv)
but3.place(relx=0.83, y=100)

but2 = Button(w, text='Обновить\nконфигурацию', width=12, height=2, font='arial 14', bg='green', command=con)
but2.place(relx=0.82, y=180)

but = Button(w, text='запуск', bg='green', font='arial 18',command=pt)
but.place(relx=0.83, y=260)

scrol = Scrollbar(w, command=tekst.yview)
tekst['yscrollcommand'] = scrol.set
scrol.place(relx=0.76, y=40, relheight=0.8)

chehvar = IntVar()
chehvar.set(0)
cheh= Checkbutton(w,text='Вкл графы', variable=chehvar, onvalue=1, offvalue=0)
cheh.place(relx=0.83, y=70)

w.mainloop()