import tkinter as tk
import tkinter.messagebox
import tkinter.ttk
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


def checkbox():
    if(var.get()==0):
        c="not checked"
    else:
        c="checked"
    tkinter.messagebox.showinfo("info", "the checkbox is " + c)

#create controls and set properties
w = tk.Label(text="Width:")
w_input = tk.Entry()
h = tk.Label(text="Height:")
h_input = tk.Entry()
z_in = tk.Button(text="Zoom in",command=checkbox)
z_out = tk.Button(text="Zoom out")
checkbox = tk.Checkbutton(text="Preserve",variable=var)
p = tk.Canvas(width=50,height=50,bg="#00FF00")

w.grid(row=0, column=0, padx=10, pady=10)
w_input.grid(row=0, column=1, pady=10)
h.grid(row=1, column=0, padx=10, pady=10)
h_input.grid(row=1, column=1, pady=10)
checkbox.grid(row=2,column=0,columnspan=2,padx=0,pady=0,)
p.grid(row=0,column=2,rowspan=2,columnspan=2)
z_in.grid(row=2, column=2, padx=10, pady=10)
z_out.grid(row=2, column=3, padx=10, pady=10)

gui.mainloop()