from tkinter import *

root = Tk()
root.title("Crypto Prices")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def grab_btc():
    return

def grab_ETH():
    return

def grab_ADA():
    return

def grab_DOT():
    return

def grab_SOL():
    return

def grab_LINK():
    return

def grab_LUNA():
    return

def grab_UNI():
    return

def grab_XRP():
    return

#Define Buttons

button_1= Button(root, text="BTC", padx=40, pady=20, command=grab_btc)
button_2= Button(root, text="ETH", padx=40, pady=20, command=grab_ETH)
button_3= Button(root, text="ADA", padx=40, pady=20, command=grab_ADA)
button_4= Button(root, text="DOT", padx=40, pady=20, command=grab_DOT)
button_5= Button(root, text="SOL", padx=40, pady=20, command=grab_SOL)
button_6= Button(root, text="LINK", padx=40, pady=20, command=grab_LINK)
button_7= Button(root, text="LUNA", padx=40, pady=20, command=grab_LUNA)
button_8= Button(root, text="UNI", padx=40, pady=20, command=grab_UNI)
button_9= Button(root, text="XRP", padx=40, pady=20, command=grab_XRP)

#put buttons on screen

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

root.mainloop()