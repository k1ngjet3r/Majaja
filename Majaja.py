import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, LEFT, SINGLE, TRUE, X
from typing import Optional


def Redirecting(*args):
    sel = function_combobox.get()
    if sel == 'A':
        var.set((1, 2, 3))
    elif sel == 'B':
        var.set((11, 22, 33))
    elif sel == 'C':
        var.set((111, 222, 333))
    query_listbox.config(listvariable=var)


window = tk.Tk()
window.title("Bakery")
window.resizable(False, False)

connection_lebel = tk.Label(window, text='Connection')
connection_lebel.pack()

connection_frame = tk.Frame(window)
connection_frame.pack(side=tk.TOP)

connection_var = [
    ("Online", 1),
    ("Offline", 2)]

connection_v = tk.IntVar()

for connection, num in connection_var:
    connection_rb = tk.Radiobutton(connection_frame, text=connection,
                                   variable=connection_v, value=num)
    connection_rb.pack(side=tk.LEFT)

sign_lebel = tk.Label(window, text='Sign Status')
sign_lebel.pack()

sign_frame = tk.Frame(window)
sign_frame.pack(side=tk.TOP)

sign_var = [
    ("Sign-In", 1),
    ("Sign-Out", 2)]

sign_v = tk.IntVar()

for status, num in sign_var:
    sign_rb = tk.Radiobutton(sign_frame, text=status,
                             variable=sign_v, value=num)
    sign_rb.pack(side=tk.LEFT)


# top frame that contains function label and drop-down selecter (combobox)
top_frame = tk.Frame(window)
top_frame.pack(side=tk.TOP)
function_label = tk.Label(top_frame, text='Function')
function_label.pack(side=tk.LEFT)
function_combobox = ttk.Combobox(top_frame, values=['A', 'B', 'C'])
function_combobox.pack(side=tk.LEFT)

# middle that containing query label and a list box
query_label_frame = tk.Frame(window)
query_label_frame.pack(side=tk.TOP)
query_label = tk.Label(
    query_label_frame, text='Query:                                                       ')
query_label.pack()

query_listbox_frame = tk.Frame(window)
query_listbox_frame.pack(side=tk.TOP)

var = tk.StringVar()
# var.set((1, 2, 3))

query_listbox = tk.Listbox(
    query_listbox_frame, listvariable=var, selectmode=SINGLE, yscrollcommand=TRUE, width=28)
query_listbox.pack(side=tk.RIGHT)

send_btn_frame = tk.Frame(window)
send_btn_frame.pack(side=tk.BOTTOM)

send_btn = tk.Button(send_btn_frame, text='Send', width=10)
send_btn.pack(fill=X)

Redirecting()


window.mainloop()
