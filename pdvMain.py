from tkinter import *

root = Tk()
# ******* LOGO E NOME ********
lb_1 = Label(root, text='Discovery PDV')
cv = Canvas(root, width=20, height=20)

cv.grid(rowspan=2, columnspan=2)
lb_1.grid(row=0, columnspan=2)

cv.create_rectagle(0, 0, 20, 20, fill='green')

# ******* PARAMETROS ********
lb_2 = Label(root, text='Cartao')
lb_3 = Label(root, text='Valor')

en_1 = Entry(root)
en_2 = Entry(root)

lb_2.grid(row=1)
lb_3.grid(row=2)
en_1.grid(row=1, column=1)
en_2.grid(row=2, column=1)

root.mainloop()

#frame_1 = Frame(root)
#frame_2 = Frame(root)

#lb_1 = Label(root, text='Discovery PDV')
#lb_2 = Label(root,text='Valor')
#lb_3 = Label(root, text='Cod. Usuario')
#entry_1 = Entry(root)
#entry_2 = Entry(root)

#frame_1.pack()
#frame_2.pack()

#lb_1.pack(side=LEFT)
#lb_2.grid(row=0)
#lb_3.grid(row=1)
#entry_1.grid(row=0, column=1)
#entry_2.grid(row=1, column=1)

#lb_2.pack(side=LEFT)
#lb_3.pack(side=LEFT)


