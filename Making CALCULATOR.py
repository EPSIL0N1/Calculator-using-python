from tkinter import *

root=Tk()
root.title("Simple Calculator")

root.iconbitmap("C:/Users/hp/Documents/pps files/Python files/TKINTER MODULE/calculator_icon.ico")

e=Entry(root,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=50)

def button_press(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,current + str(number))

# def backspace():
#     current_1 = e.get()
#     now = current_1/10
#     e.delete(0,END)
#     e.insert(0,now)

def backspace():
    current_1 = str(e.get())
    newcurrent = current_1[:-1]
    # now = int(current_1/10)
    e.delete(0,END)
    e.insert(0,newcurrent)
    # current_2 = int(e.get())
    # if current_2 == 0:
    #     e.delete(0,END)


def point():
    number = float(e.get())
    e.delete(0,END)
    e.insert(0,str(number))
    backspace()
    

def add():
    global first_num 
    first_num=e.get()
    global math
    math = "add"
    e.delete(0,END)
    
def sub():
    global first_num 
    first_num=e.get()
    global math
    math = "sub"
    e.delete(0,END)
    
def mul():
    global first_num 
    first_num=e.get()
    global math
    math = "mul"
    e.delete(0,END)
    
def div():
    global first_num 
    first_num=e.get()
    global math
    math = "div"
    e.delete(0,END)

def power():
    global first_num 
    first_num=e.get()
    global math
    math = "power"
    e.delete(0,END)
    
def equals():
    second_num=e.get()
    e.delete(0,END)
    if math=="add":
        e.insert(0,float(first_num) + float(second_num))
    if math=="sub":
        e.insert(0,float(first_num) - float(second_num))
    if math=="mul":
        e.insert(0,float(first_num) * float(second_num))
    if math=="div":
        e.insert(0,float(first_num) / float(second_num))
    if math=="power":
        e.insert(0,float(first_num) ** float(second_num))


def clear():
    e.delete(0,END)


button_0=Button(root,padx=40,pady=20,text="0",command=lambda: button_press("0"))
button_1=Button(root,padx=40,pady=20,text="1",command=lambda: button_press("1"))
button_2=Button(root,padx=40,pady=20,text="2",command=lambda: button_press("2"))
button_3=Button(root,padx=40,pady=20,text="3",command=lambda: button_press("3"))
button_4=Button(root,padx=40,pady=20,text="4",command=lambda: button_press("4"))
button_5=Button(root,padx=40,pady=20,text="5",command=lambda: button_press("5"))
button_6=Button(root,padx=40,pady=20,text="6",command=lambda: button_press("6"))
button_7=Button(root,padx=40,pady=20,text="7",command=lambda: button_press("7"))
button_8=Button(root,padx=40,pady=20,text="8",command=lambda: button_press("8"))
button_9=Button(root,padx=40,pady=20,text="9",command=lambda: button_press("9"))
button_add=Button(root,padx=40,pady=20,text="+",fg="orange",command=add)
button_sub=Button(root,padx=40,pady=20,text="-",fg="orange",command=sub)
button_mul=Button(root,padx=40,pady=20,text="*",fg="orange",command=mul)
button_div=Button(root,padx=40,pady=20,text="/",fg="orange",command=div)
button_equals=Button(root,padx=85,pady=20,text="=",fg="white",bg="orange",command=equals)
button_clear=Button(root,padx=40,pady=20,text="Clear",fg="orange",command=clear)
button_backspace=Button(root,padx=40,pady=20,text="<-",fg="orange",command=backspace)
button_point=Button(root,padx=40,pady=20,text=".",fg="orange",command=point)
button_power=Button(root,padx=40,pady=20,text="^",fg="orange",command=power)


button_0.grid(row=5,column=1)
button_1.grid(row=4,column=0)
button_2.grid(row=4,column=1)
button_3.grid(row=4,column=2)
button_4.grid(row=3,column=0)
button_5.grid(row=3,column=1)
button_6.grid(row=3,column=2)
button_7.grid(row=2,column=0)
button_8.grid(row=2,column=1)
button_9.grid(row=2,column=2)
button_add.grid(row=4,column=3)
button_sub.grid(row=3,column=3)
button_mul.grid(row=2,column=3)
button_div.grid(row=1,column=3)
button_equals.grid(row=5,columnspan=2,column=2)
button_clear.grid(row=1,column=0)
button_backspace.grid(row=1,column=1)
button_point.grid(row=5,column=0)
button_power.grid(row=1,column=2)


root.mainloop()
