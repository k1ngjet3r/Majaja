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
        'Call': ['Call Ava Max', 'Call Ava', 'Call Starbucks','call','call starbucks near my destination','call KFC near my destination','call starbucks in taipei','dial KFC in taipei','I need to call 0999123','I want to call 0999234','please dial 0999345','dial 0999456', 'call 0999567','please call 0999678',"dial john smith number",'please call john smith','dial smith','Call Hotels near my location','Call Gas Station near me'],
        'Msg': ['SMS John', 'SMS John Smith', 'Send message to John', 'Send message to John Smith'],
        'Navi': ['Navigate to Taipei 101', 'Starbucks', 'Coffee shop'],
        'Radio': ['Play FM Radio',"Play AM Radio", 'Play 1130', 'tune to 90.5 FM','Tune to 930 AM','Tune to 730 AM','Tune to 1000 AM','Previous Station','Next Station', 'Play car radio'],
        'SMS': ['Read New messages','Read messages']
    }

    query_listbox.delete(0, 'end')
    for item in combobox_values[selected]:
        query_listbox.insert('end', item)


window = tk.Tk()
window.title("MAJAJA")
window.resizable(False, False)

'''
    Frame that hold image
'''
img_frame = tk.Frame(window)
img_frame.pack(side=tk.LEFT)
selected_image = Image.open('gi_joe.jpg')
selected_image = selected_image.resize((240, 180), Image.ANTIALIAS)
img = ImageTk.PhotoImage(selected_image)
panel = tk.Label(img_frame, image=img)
panel.pack()

d1 = ttk.Separator(window, orient='vertical')
d1.pack(fill=tk.Y, expand=True)

'''
    Frame that hold connection and sign status control
'''
connection_sign_frame = tk.Frame(window)
connection_sign_frame.pack(side=tk.LEFT)

status_label = tk.Label(connection_sign_frame, text='Status Control')
status_label.pack()

connection_lebel = tk.Label(connection_sign_frame, text='Connection')
connection_lebel.pack()

connection_frame = tk.Frame(connection_sign_frame)
connection_frame.pack(side=tk.TOP)

connection_var = [
    ("Online", 1, online),
    ("Offline", 2, offline)]

connection_v = tk.IntVar()

for connection, num, cmd in connection_var:
    connection_rb = tk.Radiobutton(
        connection_frame, text=connection, variable=connection_v, value=num, command=cmd)
    connection_rb.pack(side=tk.LEFT)

sign_lebel = tk.Label(connection_sign_frame, text='Sign Status')
sign_lebel.pack()

sign_frame = tk.Frame(connection_sign_frame)
sign_frame.pack(side=tk.TOP)

sign_var = [
    ("Sign-In", 1, sign_in),
    ("Sign-Out", 2, sign_out)]

sign_v = tk.IntVar()

for status, num, cmd in sign_var:
    sign_rb = tk.Radiobutton(sign_frame, text=status,
                             variable=sign_v, value=num, command=cmd)
    sign_rb.pack(side=tk.LEFT)

'''
    Frame that holds user_related control
'''

user_rlt_frame = tk.Frame(window)
user_rlt_frame.pack(side=tk.LEFT)

user_label = tk.Label(user_rlt_frame, text='User/Security Control')
user_label.pack()

create_user_frame = tk.Frame(user_rlt_frame)
create_user_frame.pack(side=tk.TOP, fill='y')
user_name_label = tk.Label(create_user_frame, text='Name:')
user_name_label.pack(side=tk.LEFT)
user_enrty = tk.Entry(create_user_frame, width=10)
user_enrty.pack(side=tk.LEFT)
user_btn = tk.Button(create_user_frame, text='Create', command=creat_user)
user_btn.pack(side=tk.LEFT)

d2 = ttk.Separator(window, orient='vertical')
d2.pack(fill=tk.Y, expand=True)

'''
    Frame that holds command control
'''

cmd_frame = tk.Frame(window)
cmd_frame.pack(side=tk.LEFT)


# top frame that contains function label and drop-down selecter (combobox)
top_frame = tk.Frame(cmd_frame)
top_frame.pack(side=tk.TOP)
function_label = tk.Label(top_frame, text='Function')
function_label.pack(side=tk.LEFT)

combobox = ttk.Combobox(top_frame, values=['Call', 'Msg', 'Navi', 'Radio', 'SMS'])
combobox.pack(side=tk.LEFT)
combobox.bind('<<ComboboxSelected>>', on_select)

query_listbox_frame = tk.Frame(cmd_frame)
query_listbox_frame.pack(side=tk.TOP)

var = tk.StringVar()
# var.set((1, 2, 3))

query_listbox = tk.Listbox(
    query_listbox_frame, listvariable=var, selectmode=SINGLE, yscrollcommand=TRUE, width=35, height=8)
query_listbox.pack(side=tk.RIGHT)

send_btn_frame = tk.Frame(cmd_frame)
send_btn_frame.pack(side=tk.TOP)

send_btn = tk.Button(send_btn_frame, text='Majami',
                     width=10, command=Adb_command)
send_btn.pack(fill=X)

# for MacOS
window.call('wm', 'attributes', '.', '-topmost', '1')

# for Windows
# window.lift()

window.mainloop()
