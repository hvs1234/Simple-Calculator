#Libraries
from tkinter import *
from tkinter import messagebox

#Application Setup
root = Tk()
root.title("Calculator")
root.resizable(False,False)
root.geometry("570x600+380+60")
root.configure(bg="#17161b")

#Functions
equation=""
def show(value): 
    global equation
    equation+=value
    l1.config(text=equation)

def clear():
    global equation
    equation=""
    l1.config(text=equation)

def calculate():
    global equation
    ans=""
    if(equation==""):
        messagebox.showwarning("Blank Input","Please put some value here!")
    if(equation!=""):
        try:
            ans=eval(equation)
        except:
            ans="error"
            if(ans=="error"):
                messagebox.showerror("Invalid","Invalid input")
            equation=""
    l1.config(text=ans)

#Application Creation
img1 = PhotoImage(file="E:\\pyImages\\calculator logo.png")
root.iconphoto(False,img1)
l1 = Label(root,width=25,height=2,text="",font=("monospace",30))
l1.pack()

Button(root,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",
            activebackground="#3697f5",activeforeground="#fff",command=lambda: clear()).place(x=10,y=100)
Button(root,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36", 
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("/")).place(x=150,y=100)
Button(root,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("%")).place(x=290,y=100)
Button(root,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("*")).place(x=430,y=100)

Button(root,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("7")).place(x=10,y=200)
Button(root,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("9")).place(x=290,y=200)
Button(root,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("-")).place(x=430,y=200)

Button(root,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("6")).place(x=290,y=300)
Button(root,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("+")).place(x=430,y=300)

Button(root,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("3")).place(x=290,y=400)
Button(root,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show("0")).place(x=10,y=500)

Button(root,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",
            activebackground="#2a2d36",activeforeground="#fff",command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",
            activebackground="#fe9037",activeforeground="#fff",command=lambda: calculate()).place(x=430,y=400)
root.mainloop()
