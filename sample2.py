import tkinter
from tkinter import *

m = Tk()
def display():
    print("hello")

Text=Entry(m)

buttonClear= tkinter.Button(m ,text="C",width=10,height =3,command = display())
buttonDiv = tkinter.Button(m ,text="/",width=10,height =3,command = display())
buttonMul = tkinter.Button(m ,text="*",width=10,height =3,command = display())
buttonAdd = tkinter.Button(m ,text="+",width=10,height =3,command = display())


button7= tkinter.Button(m ,text="7",width=10,height =3,command = display())
button8 = tkinter.Button(m ,text="8",width=10,height =3,command = display())
button9 = tkinter.Button(m ,text="9",width=10,height =3,command = display())
buttonSub = tkinter.Button(m ,text="-",width=10,height =3,command = display())


button4 = tkinter.Button(m ,text="4",width=10,height =3,command = display())
button5 = tkinter.Button(m ,text="5",width=10,height =3,command = display())
button6 = tkinter.Button(m ,text="6",width=10,height =3,command = display())

button1 = tkinter.Button(m ,text="1",width=10,height =3,command = display())
button2 = tkinter.Button(m ,text="2",width=10,height =3,command = display())
button3 = tkinter.Button(m ,text="3",width=10,height =3,command = display())
buttonEqual = tkinter.Button(m ,text="=",width=10,height =3,command = display())

Text.grid(row = 1,sticky =W)

buttonClear.grid(row=2,column=0 ,pady =2)
buttonDiv.grid(row=2,column=1 ,pady =2)
buttonMul.grid(row=2,column=2 ,pady =2)
buttonAdd.grid(row=2,column=3 ,pady =2)

button7.grid(row=3,column=0 ,pady =2)
button8.grid(row=3,column=1 ,pady =2)
button9.grid(row=3,column=2 ,pady =2)
buttonSub.grid(row=3,column=3 ,pady =2)

button4.grid(row=4,column=0 ,pady =2)
button5.grid(row=4,column=1 ,pady =2)
button6.grid(row=4,column=2 ,pady =2)

button1.grid(row=5,column=0 ,pady =2)
button2.grid(row=5,column=1 ,pady =2)
button3.grid(row=5,column=2 ,pady =2)
buttonEqual.grid(row=5,column=3 ,pady =2)


#button.pack()
#button2.pack()
#Lb.pack()
m.mainloop()

