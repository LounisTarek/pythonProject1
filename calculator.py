import tkinter
from tkinter import ttk

frm = tkinter.Tk()
frm.geometry('600x300')

fnt = 'none 30 bold'

lbn1 = ttk.Label(frm,text='num 1:',font=fnt)
lbn2 = ttk.Label(frm,text='num 2:',font=fnt)

sv1 = tkinter.StringVar()
sv2 = tkinter.StringVar()
txtn1 = ttk.Entry(frm,font=fnt,textvariable=sv1)
txtn2 = ttk.Entry(frm,font=fnt,textvariable=sv2)
sv1.set('0')
sv2.set('0')

def calcul(option):
    n1 = int(txtn1.get())
    n2 = int(txtn2.get())
    r = 0
    if option == '+': r = n1 + n2
    elif option == '-': r = n1 - n2
    elif option == '*': r = n1 * n2
    else:
        if n2 == 0: n2=1
        r = n1 / n2
    lbresultat['text']=(f'result: {n1}{option}{n2}={round(r,2)}')

lbn1.grid(row=0,column=0,pady=5,padx=5)
txtn1.grid(row=0,column=1)
lbn2.grid(row=1,column=0,pady=5,padx=5)
txtn2.grid(row=1,column=1)

btns=ttk.Style()
btns.configure('TButton',font=fnt,padding=10)
frame = tkinter.Frame(frm)

btnadd = ttk.Button(frame,text='+',width='5',command=lambda:calcul('+'))
btnsub = ttk.Button(frame,text='-',width='5',command=lambda:calcul('-'))
btnmul = ttk.Button(frame,text='*',width='5',command=lambda:calcul('*'))
btndiv = ttk.Button(frame,text='/',width='5',command=lambda:calcul('/'))

frame.grid(row=2,column=0,columnspan=2,pady=10)
btnadd.grid(row=0,column=0)
btnsub.grid(row=0,column=1)
btnmul.grid(row=0,column=2)
btndiv.grid(row=0,column=3)

lbresultat = ttk.Label(frame,text='result:',font=fnt)
lbresultat.grid(row=2,column=0,columnspan=4,pady=10)

frm.mainloop()
