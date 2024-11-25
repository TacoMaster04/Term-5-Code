from tkinter import *
from tkinter import ttk

window = Tk()

menubar = Menu(window)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_cascade(label="New")
fileMenu.add_cascade(label="Save")
fileMenu.add_separator()
fileMenu.add_cascade(label="Exit", command=window.quit)


editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_cascade(label="Cut")
editMenu.add_cascade(label="Copy")
editMenu.add_separator()
editMenu.add_cascade(label="Paste")


scrollbar = Scrollbar(window, orient="vertical")
scrollbar.pack(side="right", fill=Y)

window.geometry("400x400+500+100")
# window.resizable(False, False)
# window.maxsize(1000, 600)
# window.minsize(1000, 600)
window.title("CAIB Lab 7")
window.config(background="white")
window.config(menu=menubar)


frame1 = Frame(width=200, height=400, bg="darkred")
frame1.place(x=1, y=1)

frame2 = Frame(width=200, height=400, bg="darkblue")
frame2.place(x=200, y=1)

button1 = Button(frame1, text="Click Me", width=10, height=2, foreground="white", background="black", cursor="star")
button1.place(x=50, y=50)

button2 = Button(frame2, text="Click Me", width=10, height=2, foreground="white", background="black", cursor="heart")
button2.place(x=50, y=50)

label = Label(frame1, text="Hello World", font=("Arial", 15), foreground="white", background="black")
label.place(x=50, y=100)

entry1 = Entry(frame1, width=10, font=("Arial", 15))
entry1.place(x=50, y=150)

dropdown1 = ttk.Combobox(frame1, values=["Option 1", "Option 2", "Option 3"])
dropdown1.place(x=50, y=200)

dropdown2 = ttk.Combobox(frame2, values=["Option 1", "Option 2", "Option 3"], state="readonly")
dropdown2.place(x=50, y=250)

mainloop()