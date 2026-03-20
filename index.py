from tkinter import *
import datetime
root = Tk()

root.geometry("400x400")
root.config(bg="black")
root.title("Digital Clock")

design = Frame(root, bg="black",highlightbackground="red",highlightthickness=2)
design.place(relx=0.5, rely=0.5, anchor="center",height=350, width=350)

def clock():
    
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M:%S %p")
    current_date = now.strftime("%A\n%d %B %Y")
    label.config(text=current_time + "\n" + current_date)
    label.after(1000, clock)

label = Label(design, bg="black", fg="cyan",font=("Arial", 35, "bold"))
label.place(relx=0.5, rely=0.5, anchor="center")

clock()
root.mainloop()
