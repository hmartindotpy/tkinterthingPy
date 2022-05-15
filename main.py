import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
from tkinter import ttk
from tkinter import *
gui = tk.Tk()
gui.geometry("400x300")
window_width=400
window_height=300
screen_width = gui.winfo_screenwidth()
screen_height = gui.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
gui.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
gui.eval("tk::PlaceWindow . center")
gui.resizable(False,False)

var = tk.IntVar()

def save():
    pass
def load():
    pass
def checkbox():
    st = checkbox.state()
    if 'selected' in st:
        tkinter.messagebox.showinfo("info", "the checkbox is checked")
    else:
        tkinter.messagebox.showinfo("info", "the checkbox is not checked")

#create controls and set properties
w = tk.Label(text="Width:")
w_input = tk.Entry()
h = tk.Label(text="Height:")
h_input = tk.Entry()
z_in = tk.Button(text="Zoom in",command=checkbox)
z_out = tk.Button(text="Zoom out")
checkbox = ttk.Checkbutton(text="Preserve")
p = tk.Canvas(width=50,height=50,bg="#FF0000")
img = PhotoImage(file='C:/Users/rubik/Desktop/bis.png')
p.create_image(0,0,anchor=NW,image=img)
Var1 = StringVar()
frame = Frame(gui)
RBttn = Radiobutton(frame, text = "Option1", variable = Var1,
                    value = 1)
RBttn.grid(padx = 5, pady = 5)
RBttn2 = Radiobutton(frame, text = "Option2", variable = Var1,
                     value = 2)
RBttn2.grid(padx = 5, pady = 5)
mainmenu = Menu(frame)
mainmenu.add_command(label = "Save", command= save)  
mainmenu.add_command(label = "Load", command= load)
mainmenu.add_command(label = "Exit", command= gui.destroy)
vlist = ["Option1", "Option2", "Option3",
          "Option4", "Option5"]
 
Combo = ttk.Combobox(frame, values = vlist)
Combo.set("Pick an Option")
Combo.grid(padx = 5, pady = 5, row=5)
gui.config(menu = mainmenu)

w.grid(row=0, column=0, padx=10, pady=10)
w_input.grid(row=0, column=1, pady=10)
h.grid(row=1, column=0, padx=10, pady=10)
h_input.grid(row=1, column=1, pady=10)
checkbox.grid(row=2,column=0,columnspan=2,padx=0,pady=0,)
p.grid(row=0,column=2,rowspan=2,columnspan=2)
z_in.grid(row=2, column=2, padx=10, pady=10)
z_out.grid(row=2, column=3, padx=10, pady=10)

gui.mainloop()