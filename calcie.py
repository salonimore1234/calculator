from tkinter import *


# to print our numbers
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()
    elif text == "c":
        scvalue.set("")
        screen.update()
        pass
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("644x900")
root.wm_iconbitmap("calculator-icon_34473.ico")
root.title("Calculator by Saloni")
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)


f = Frame(root,bg="grey")
b = Button(f, text="9", padx=21, pady=10, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=21, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="7", padx=21, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f, text="6", padx=21, pady=10, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=21, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="4", padx=21, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f, text="3", padx=21, pady=10, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=21, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="1", padx=21, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="grey")

b = Button(f, text="0", padx=24, pady=10, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=24, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=24, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f, text="/", padx=20, pady=10, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="%", padx=20, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=20, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f, text="c", padx=20, pady=10, font="lucida 35 bold")

b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text=".", padx=20, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)

b = Button(f, text="00", padx=20, pady=10, font="lucida 35 bold")
b.pack(side=LEFT, padx=18, pady=12)
b.bind("<Button-1>", click)
f.pack()
root.mainloop()