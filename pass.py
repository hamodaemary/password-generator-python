from tkinter import *
import random
def ran():
	n = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	m = random.choice(n)*10
	z = [1,2,3,4,5,6,7,8,9,10]
	c = random.choice(z)*10
	e = ent.get()
	lbl.config(text='#pass'+str(m)+str(c)+str(e))
x = Tk()
lbl = Label(text='',bg='green',fg='white')
lbl.pack()
ent= Entry(bd=2,font=(12))
ent.pack()
but = Button(text='create',command=ran)
but.pack()






x.mainloop()