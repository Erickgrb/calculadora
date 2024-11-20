from tkinter import *
from tkinter import ttk


#Colors
color1 = "#323335" # black
color2 = "#E8EBF0" # white
color3 = "#083145" # blue
color4 = "#ADB2B4" # grey
color5 = "#F08A37" # orange


window = Tk()
window.title("Calculadora")
window.geometry("300x400")
window.config(bg=color1)


# Frames created
frame_screen = Frame(window, width=300, height=70, bg=color3)
frame_screen.grid(row=0, column=0)

frame_body = Frame(window, width=300, height=350, bg=color2)
frame_body.grid(row=1, column=0)


# Frames buttons

button_size = 12
font = "Arial"

b1 = Button(frame_body, text="C", width=16, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_body, text="%", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b2.place(x=150, y=0)
b3 = Button(frame_body, text="/", width=10, height=2, bg=color5, fg=color2, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b3.place(x=225, y=0)

b4 = Button(frame_body, text="7", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b4.place(x=0, y=70)
b5 = Button(frame_body, text="8", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b5.place(x=75, y=70)
b6 = Button(frame_body, text="9", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b6.place(x=150, y=70)
b7 = Button(frame_body, text="X", width=10, height=2, bg=color5, fg=color2, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b7.place(x=225, y=70)

b8 = Button(frame_body, text="4", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b8.place(x=0, y=140)
b9 = Button(frame_body, text="5", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b9.place(x=75, y=140)
b10 = Button(frame_body, text="6", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b10.place(x=150, y=140)
b11 = Button(frame_body, text="-", width=10, height=2, bg=color5, fg=color2, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b11.place(x=225, y=140)

b12 = Button(frame_body, text="1", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b12.place(x=0, y=210)
b13 = Button(frame_body, text="2", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b13.place(x=75, y=210)
b14 = Button(frame_body, text="3", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b14.place(x=150, y=210)
b15 = Button(frame_body, text="+", width=10, height=2, bg=color5, fg=color2, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b15.place(x=225, y=210)

b16 = Button(frame_body, text="0", width=16, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b16.place(x=0, y=280)
b17 = Button(frame_body, text=".", width=10, height=2, bg=color4, fg=color1, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b17.place(x=150, y=280)
b18 = Button(frame_body, text="=", width=10, height=2, bg=color5, fg=color2, font=(font, button_size, "bold"), relief=RAISED, overrelief=RIDGE)
b18.place(x=225, y=280)


window.mainloop()