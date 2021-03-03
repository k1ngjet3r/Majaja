import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, LEFT, SINGLE, TRUE, X
from typing import Optional
from adb_command import online, offline, sign_in, sign_out
import os

def Adb_command():
    query = query_listbox.get(query_listbox.curselection())
    query = query.replace(' ', '\ ')
    frame = 'adb shell am start -n com.google.android.carassistant/com.google.android.apps.gsa.binaries.auto.app.voiceplate.VoicePlateActivity -e query '
    os.system(frame+query)
    print(frame+query)

def on_select(event):
    print('[DEBUG] event: ', event)
    print('[DEBUG] event.widget: ', event.widget)
    print('[DEBUG] event.widget.get(): ', event.widget.get())

    selected = event.widget.get()

    combobox_values = {
        'Call': ['Call Ava Max', 'Call Ava', 'Call Starbucks'],
        'Msg': ['SMS John', 'SMS John Smith', 'Send message to John', 'Send message to John Smith'],
        'Navi': ['Navigate to Taipei 101', 'Starbucks', 'Coffee shop']
    }

    query_listbox.delete(0, 'end')
    for item in combobox_values[selected]:
        query_listbox.insert('end', item)
        
    


window = tk.Tk()
window.title("MAJAJA")
window.resizable(False, False)

connection_lebel = tk.Label(window, text='Connection')
connection_lebel.pack()

connection_frame = tk.Frame(window)
connection_frame.pack(side=tk.TOP)

connection_var = [
    ("Online", 1, online),
    ("Offline", 2, offline)]

connection_v = tk.IntVar()

for connection, num, cmd in connection_var:
    connection_rb = tk.Radiobutton(connection_frame, text=connection, variable=connection_v, value=num, command=cmd)
    connection_rb.pack(side=tk.LEFT)

sign_lebel = tk.Label(window, text='Sign Status')
sign_lebel.pack()

sign_frame = tk.Frame(window)
sign_frame.pack(side=tk.TOP)

sign_var = [
    ("Sign-In", 1, sign_in),
    ("Sign-Out", 2, sign_out)]

sign_v = tk.IntVar()

for status, num, cmd in sign_var:
    sign_rb = tk.Radiobutton(sign_frame, text=status, variable=sign_v, value=num, command=cmd)
    sign_rb.pack(side=tk.LEFT)


# top frame that contains function label and drop-down selecter (combobox)
top_frame = tk.Frame(window)
top_frame.pack(side=tk.TOP)
function_label = tk.Label(top_frame, text='Function')
function_label.pack(side=tk.LEFT)

combobox = ttk.Combobox(top_frame, values=['Call', 'Msg', 'Navi'])
combobox.pack(side=tk.LEFT)
combobox.bind('<<ComboboxSelected>>', on_select)

# middle that containing query label and a list box
query_label_frame = tk.Frame(window)
query_label_frame.pack(side=tk.TOP)
query_label = tk.Label(
    query_label_frame, text='Query')
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

send_btn = tk.Button(send_btn_frame, text='Send', width=10, command=Adb_command)
send_btn.pack(fill=X)





window.mainloop()
