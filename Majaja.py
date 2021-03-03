import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, LEFT, SINGLE, TRUE, X
from typing import Optional


def on_select(event):
    print('[DEBUG] event: ', event)
    print('[DEBUG] event.widget: ', event.widget)
    print('[DEBUG] event.widget.get(): ', event.widget.get())

    selected = event.widget.get()

    conbobox_values = {
        'A': ['A1', 'A2', 'A3'],
        'B': ['B1', 'B2', 'B3'],
        'C': ['C1', 'C2', 'C3']
    }

    listbox.delete(0, 'end')
    for item in combobox_values[selected]:
        listbox.insert('end', item)
        
    


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

combobox = ttk.Combobox(top_frame, values=['A', 'B', 'C'])
combobox.pack(side=tk.LEFT)
combobox.bind('<<ComboboxSelected>>', on_select)

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
