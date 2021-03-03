import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTH, LEFT, SINGLE, TRUE, X
from typing import Optional
from adb_command import online, offline, sign_in, sign_out
import os
from PIL import Image, ImageTk

def creat_user():
    name = user_enrty.get()
    name = name.replace(' ', '\ ')
    frame = 'adb shell pm create_user '
    cmd = frame + name
    os.system('adb root')
    os.system(cmd)
    print(cmd)

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

img_frame = tk.Frame(window)
img_frame.pack(side=tk.LEFT)
selected_image = Image.open('gi_joe.jpg')
selected_image = selected_image.resize((240, 180), Image.ANTIALIAS)
img = ImageTk.PhotoImage(selected_image)
panel = tk.Label(img_frame, image=img)
panel.pack()



# window.resizable(False, False)

left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT)

right_frame = tk.Frame(window)
right_frame.pack(side=tk.LEFT)

create_user_frame = tk.Frame(left_frame)
create_user_frame.pack(side=tk.TOP)

user_enrty = tk.Entry(create_user_frame)
user_enrty.pack(side=tk.LEFT)

user_btn = tk.Button(create_user_frame, text='Create', command=creat_user)
user_btn.pack(side=tk.LEFT)

connection_lebel = tk.Label(left_frame, text='Connection')
connection_lebel.pack()

connection_frame = tk.Frame(left_frame)
connection_frame.pack(side=tk.TOP)

connection_var = [
    ("Online", 1, online),
    ("Offline", 2, offline)]

connection_v = tk.IntVar()

for connection, num, cmd in connection_var:
    connection_rb = tk.Radiobutton(connection_frame, text=connection, variable=connection_v, value=num, command=cmd)
    connection_rb.pack(side=tk.LEFT)

sign_lebel = tk.Label(left_frame, text='Sign Status')
sign_lebel.pack()

sign_frame = tk.Frame(left_frame)
sign_frame.pack(side=tk.TOP)

sign_var = [
    ("Sign-In", 1, sign_in),
    ("Sign-Out", 2, sign_out)]

sign_v = tk.IntVar()

for status, num, cmd in sign_var:
    sign_rb = tk.Radiobutton(sign_frame, text=status, variable=sign_v, value=num, command=cmd)
    sign_rb.pack(side=tk.LEFT)


# top frame that contains function label and drop-down selecter (combobox)
top_frame = tk.Frame(right_frame)
top_frame.pack(side=tk.TOP)
function_label = tk.Label(top_frame, text='Function')
function_label.pack(side=tk.LEFT)

combobox = ttk.Combobox(top_frame, values=['Call', 'Msg', 'Navi'])
combobox.pack(side=tk.LEFT)
combobox.bind('<<ComboboxSelected>>', on_select)

# middle that containing query label and a list box
# query_label_frame = tk.Frame(right_frame)
# query_label_frame.pack(side=tk.TOP)
# query_label = tk.Label(
#     query_label_frame, text='Query')
# query_label.pack()

query_listbox_frame = tk.Frame(right_frame)
query_listbox_frame.pack(side=tk.TOP)

var = tk.StringVar()
# var.set((1, 2, 3))

query_listbox = tk.Listbox(
    query_listbox_frame, listvariable=var, selectmode=SINGLE, yscrollcommand=TRUE, width=35, height=8)
query_listbox.pack(side=tk.RIGHT)

send_btn_frame = tk.Frame(right_frame)
send_btn_frame.pack(side=tk.TOP)

send_btn = tk.Button(send_btn_frame, text='Majami', width=10, command=Adb_command)
send_btn.pack(fill=X)





window.mainloop()
