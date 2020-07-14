import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pandas as pd
import math

root = tk.Tk()
root.geometry("300x400")
root.resizable(0,0)
root.title("Calculator")
icon="C:\\Users\\sanjaneeta\\Desktop\\calculator\\cal.ico"
root.wm_iconbitmap(icon)
his={}
val = ""
#manu bar

def history():
    global his
    h=pd.DataFrame(his.items(),columns=["Equation","ANS"])
    root2=tk.Tk()
    root2.geometry("250x400+300+300")
    root2.resizable(0,0)
    root2.title("History")
    root2.wm_iconbitmap("C:\\Users\\sanjaneeta\\Desktop\\calculator\\cal.ico")
    Label(root2,text=h).pack()
cal=Frame(root)
Menubar=Menu(cal)
filemenu=Menu(Menubar,tearoff=0)
Menubar.add_cascade(label="File",menu=filemenu)
filemenu.add_command(label="view history",command=history)
root.config(menu=Menubar)

#is over function
    #number
def e0(event):
    btn0.configure(bg="grey")
def l0(event):
    btn0.configure(bg="white")

def e1(event):
    btn1.configure(bg="grey")
def l1(event):
    btn1.configure(bg="white")

def e2(event):
    btn2.configure(bg="grey")
def l2(event):
    btn2.configure(bg="white")

def e3(event):
    btn3.configure(bg="grey")
def l3(event):
    btn3.configure(bg="white")

def e4(event):
    btn4.configure(bg="grey")
def l4(event):
    btn4.configure(bg="white")

def e5(event):
    btn5.configure(bg="grey")
def l5(event):
    btn5.configure(bg="white")

def e6(event):
    btn6.configure(bg="grey")
def l6(event):
    btn6.configure(bg="white")

def e7(event):
    btn7.configure(bg="grey")
def l7(event):
    btn7.configure(bg="white")

def e8(event):
    btn8.configure(bg="grey")
def l8(event):
    btn8.configure(bg="white")

def e9(event):
    btn9.configure(bg="grey")
def l9(event):
    btn9.configure(bg="white")
    #operator

def eplus(event):
    btnplus.configure(bg="grey")
def lplus(event):
    btnplus.configure(bg="white")

def eminus(event):
    btnminus.configure(bg="grey")
def lminus(event):
    btnminus.configure(bg="white")

def emult(event):
    btnmult.configure(bg="grey")
def lmult(event):
    btnmult.configure(bg="white")

def ediv(event):
    btndiv.configure(bg="grey")
def ldiv(event):
    btndiv.configure(bg="white")

def eequal(event):
    btnequal.configure(bg="grey")
def lequal(event):
    btnequal.configure(bg="white")

def ec(event):
    btnc.configure(bg="grey")
def lc(event):
    btnc.configure(bg="white")

def ed(event):
    btnd.configure(bg="grey")
def ld(event):
    btnd.configure(bg="white")

def ep(event):
    btnp.configure(bg="grey")
def lp(event):
    btnp.configure(bg="white")

def edel(event):
    btndel.configure(bg="grey")
def ldel(event):
    btndel.configure(bg="white")

#number's

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

# operator's
def btn_p_isclicked():
    global val
    val = val + "^"
    data.set(val)

def btn_s_isclicked():
    global val
    val = "√" + val
    data.set(val)

def btn_del_isclicked():
    global val
    l=len(val)
    a=val[0:(l-1)]
    val=a
    data.set(val)

def btn_d_isclicked():
    global val
    val = val + "."
    data.set(val)

def btn_plus_clicked():
    global val
    val = val + "+"
    data.set(val)

def btn_minus_clicked():
    global val
    val = val + "-"
    data.set(val)

def btn_mult_clicked():
    global val
    val = val + "*"
    data.set(val)

def btn_div_clicked():
    global val
    val = val + "/"
    data.set(val)

def btn_c_pressed():
    global A,operator,val
    val = ""
    data.set(val)

#equal

def result():
    global val, his
    k=val
    if "√" in val:
        l=len(val)
        a=val[1:l]
        val=a
        if "√" in val:
            messagebox.showerror("Error","Invalid syntax")
            val=""
            data.set(val)
        else:
            va=float(val)
            val=math.sqrt(va)
            val=str(val)
            v=val
            his[k]=v
            data.set(val)
    if "^" in val:
        val=val.replace("^","**")
        val=eval(val)
        v=val
        his[k]=v
        val=str(val)
        data.set(val)
    else:
        val=eval(val)
        v=val
        his[k]=v
        val=str(val)
        data.set(val)


data = StringVar()
lbl = Label(root,text = "0",anchor = SE,font = ("Verdana", 20),textvariable = data,background = "#000000",fg = "#ffffff")
lbl.pack(expand = True, fill = "both")

# row's

btnrow1 = Frame(root)
btnrow1.pack(expand = True, fill = "both")

btnrow2 = Frame(root)
btnrow2.pack(expand = True, fill = "both")

btnrow3 = Frame(root)
btnrow3.pack(expand = True, fill = "both")

btnrow4 = Frame(root)
btnrow4.pack(expand = True, fill = "both")

btnrow5 = Frame(root)
btnrow5.pack(expand = True, fill = "both")

# row 1

btnc = Button(btnrow1,text = "C",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_c_pressed)
btnc.pack(side = LEFT, expand = True, fill = "both")

btnd = Button(btnrow1,text = ".",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_d_isclicked)
btnd.pack(side = LEFT, expand = True, fill = "both",)

btnp = Button(btnrow1,text = "^",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_p_isclicked)
btnp.pack(side = LEFT, expand = True, fill = "both",)

btns = Button(btnrow1,text = "√",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_s_isclicked)
btns.pack(side = LEFT, expand = True, fill = "both")

# row 2

btn1 = Button(btnrow2,text = "1",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_1_isclicked)
btn1.pack(side = LEFT, expand = True, fill = "both",)

btn2 = Button(btnrow2,text = "2",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_2_isclicked)
btn2.pack(side = LEFT, expand = True, fill = "both",)

btn3 = Button(btnrow2,text = "3",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_3_isclicked)
btn3.pack(side = LEFT, expand = True, fill = "both",)

btnplus = Button(btnrow2,text = "+",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_plus_clicked)
btnplus.pack(side = LEFT, expand = True, fill = "both",)

# row 3

btn4 = Button(btnrow3,text = "4",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_4_isclicked)
btn4.pack(side = LEFT, expand = True, fill = "both",)

btn5 = Button(btnrow3,text = "5",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_5_isclicked)
btn5.pack(side = LEFT, expand = True, fill = "both",)

btn6 = Button(btnrow3,text = "6",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_6_isclicked)
btn6.pack(side = LEFT, expand = True, fill = "both",)

btnminus = Button(btnrow3,text = "-",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_minus_clicked)
btnminus.pack(side = LEFT, expand = True, fill = "both",)

#row 4

btn7 = Button(btnrow4,text = "7",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_7_isclicked)
btn7.pack(side = LEFT, expand = True, fill = "both")

btn8 = Button(btnrow4,text = "8",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_8_isclicked)
btn8.pack(side = LEFT, expand = True, fill = "both")

btn9 = Button(btnrow4,text = "9",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_9_isclicked)
btn9.pack(side = LEFT, expand = True, fill = "both")

btnmult = Button(btnrow4,text = "*",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_mult_clicked)
btnmult.pack(side = LEFT, expand = True, fill = "both")
# row 5

btndel = Button(btnrow5,text = "Del",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_del_isclicked)
btndel.pack(side = LEFT, expand = True, fill = "both",)

btn0 = Button(btnrow5,text = "0",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_0_isclicked)
btn0.pack(side = LEFT, expand = True, fill = "both")

btnequal = Button(btnrow5,text = "=",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = result)
btnequal.pack(side = LEFT, expand = True, fill = "both")

btndiv = Button(btnrow5,text = "/",font = ("Verdana", 22),relief = GROOVE,bg="white",border = 0,command = btn_div_clicked)
btndiv.pack(side = LEFT, expand = True, fill = "both")

# is over function 2
    # number
btn0.bind("<Enter>",e0)
btn0.bind("<Leave>",l0)

btn1.bind("<Enter>",e1)
btn1.bind("<Leave>",l1)

btn2.bind("<Enter>",e2)
btn2.bind("<Leave>",l2)

btn3.bind("<Enter>",e3)
btn3.bind("<Leave>",l3)

btn4.bind("<Enter>",e4)
btn4.bind("<Leave>",l4)

btn5.bind("<Enter>",e5)
btn5.bind("<Leave>",l5)

btn6.bind("<Enter>",e6)
btn6.bind("<Leave>",l6)

btn7.bind("<Enter>",e7)
btn7.bind("<Leave>",l7)

btn8.bind("<Enter>",e8)
btn8.bind("<Leave>",l8)

btn9.bind("<Enter>",e9)
btn9.bind("<Leave>",l9)
    # operator
btnplus.bind("<Enter>",eplus)
btnplus.bind("<Leave>",lplus)

btnminus.bind("<Enter>",eminus)
btnminus.bind("<Leave>",lminus)

btnmult.bind("<Enter>",emult)
btnmult.bind("<Leave>",lmult)

btndiv.bind("<Enter>",ediv)
btndiv.bind("<Leave>",ldiv)

btnd.bind("<Enter>",ed)
btnd.bind("<Leave>",ld)

btnp.bind("<Enter>",ep)
btnp.bind("<Leave>",lp)

btndel.bind("<Enter>",edel)
btndel.bind("<Leave>",ldel)

btnequal.bind("<Enter>",eequal)
btnequal.bind("<Leave>",lequal)

btnc.bind("<Enter>",ec)
btnc.bind("<Leave>",lc)
root.mainloop()