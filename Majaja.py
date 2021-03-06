'''
    This is version 0.0.1 Alpha

    Still updating the function and value to the function_value.json for Google Assistant Command query

    Current function including internet conncetion control, google account login or out control, create user, and Google Assistant command sender

    GUI is still not optimized, FYI
'''

from tkinter import Radiobutton, ttk
from tkinter.constants import ANCHOR, BOTH, LEFT, SINGLE, TOP, TRUE, X, Y
from typing import Optional
from adb_command import online, offline, sign_in, sign_out
from PIL import Image, ImageTk
import tkinter as tk
import os
import json
from random import randrange
from tts_engine import tts

img_list = ['gi_joe.jpg', 'gi_joe_majaja.jpg', 'gi_joe_meme_1.png', 'gi_joe_meme_2.jpg']

img_chosed = img_list[randrange(len(img_list))]


def creat_user():
    name = user_enrty.get()
    name = name.replace(' ', '\ ')
    frame = 'adb shell pm create-user '
    cmd = frame + name
    os.system('adb root')
    os.system(cmd)
    print(cmd)


def exe_command():
    mode = mode_var.get()
    query = query_listbox.get(query_listbox.curselection())
    mode_list = ['Speech Mode', 'Majami Mode']

    print('[MODE] {}'.format(mode_list[mode-1]))
    # if user selected "speech mode"
    if mode == 1:
        tts(query)
        print('[TTS] {}'.format(query))
    # if user selected "Majami mode"
    elif mode == 2:
        query = query.replace(' ', '\ ')
        frame = 'adb shell am start -n com.google.android.carassistant/com.google.android.apps.gsa.binaries.auto.app.voiceplate.VoicePlateActivity -e query '
        os.system(frame+query)
        print('[ADB] {}'.format(frame+query))


def on_select(event):
    print('[DEBUG] event: ', event)
    print('[DEBUG] event.widget: ', event.widget)
    print('[DEBUG] event.widget.get(): ', event.widget.get())

    selected = event.widget.get()

    # Load and read the command JSON file
    with open('function_value.json') as json_file:
        combobox_values = json.load(json_file)

    query_listbox.delete(0, 'end')
    for item in combobox_values[selected]:
        query_listbox.insert('end', item)




window = tk.Tk()
window.title("MAJAJA v0.0.1 Alpha")
window.resizable(False, False)

'''
    Frame that hold image
'''
img_frame = tk.Frame(window, width=500, height=200)
img_frame.pack(side=tk.LEFT, fill=tk.Y)
selected_image = Image.open(img_chosed)
selected_image = selected_image.resize((240, 180), Image.ANTIALIAS)
img = ImageTk.PhotoImage(selected_image)
panel = tk.Label(img_frame, image=img)
panel.pack()



'''
    Frame that hold connection and sign status control
'''
connection_sign_frame = tk.Frame(window, width=500)
connection_sign_frame.pack(side=tk.LEFT, fill=tk.Y)

status_label = tk.Label(connection_sign_frame, text='Status Control', width=22, font='Helvetica 10 bold')
status_label.pack()


connection_frame = tk.Frame(connection_sign_frame, borderwidth=2, relief='groove')
connection_frame.pack(side=tk.TOP)

connection_lebel = tk.Label(connection_frame, text='Connection', width=20, font='Helvetica 9 bold')
connection_lebel.pack()

connection_var = [
    ("Online", 1, online),
    ("Offline", 2, offline)]

connection_v = tk.IntVar()

for connection, num, cmd in connection_var:
    connection_rb = tk.Radiobutton(
        connection_frame, text=connection, variable=connection_v, value=num, command=cmd)
    connection_rb.pack(side=tk.LEFT)


sign_frame = tk.Frame(connection_sign_frame, borderwidth=2, relief='groove')
sign_frame.pack(side=tk.TOP)

sign_lebel = tk.Label(sign_frame, text='Sign Status', width=20, font='Helvetica 9 bold')
sign_lebel.pack()

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
user_rlt_frame.pack(side=tk.LEFT, fill=tk.Y)

user_label = tk.Label(user_rlt_frame, text='User/Security Control', width=22, font='Helvetica 10 bold')
user_label.pack()

create_user_frame = tk.Frame(user_rlt_frame, borderwidth=2, relief='groove')
create_user_frame.pack(side=tk.TOP, fill='y')
creat_user_lbl = tk.Label(create_user_frame, text='Create New User', font='Helvetica 9 bold')
creat_user_lbl.pack(side=tk.TOP)
user_name_label = tk.Label(create_user_frame, text='Name:')
user_name_label.pack(side=tk.LEFT)
user_enrty = tk.Entry(create_user_frame, width=12)
user_enrty.pack(side=tk.LEFT)
user_btn = tk.Button(create_user_frame, text='Create', command=creat_user)
user_btn.pack(side=tk.LEFT)


'''
    Frame that holds command control
'''

cmd_frame = tk.Frame(window, width=300)
cmd_frame.pack(side=tk.LEFT, fill=tk.Y)

# mode-selection frame
mode_frame = tk.Frame(cmd_frame)
mode_frame.pack()

mode_var = tk.IntVar(None, 1)

speech_mode = tk.Radiobutton(mode_frame, text='Speech Mode', variable=mode_var, value=1)
speech_mode.pack(side=tk.LEFT)

Majami_mode = tk.Radiobutton(mode_frame, text='Majami Mode', variable=mode_var, value=2)
Majami_mode.pack(side=tk.LEFT)


# top frame that contains function label and drop-down selecter (combobox)
top_frame = tk.Frame(cmd_frame)
top_frame.pack(side=tk.TOP)
function_label = tk.Label(top_frame, text='Function')
function_label.pack(side=tk.LEFT)

combobox = ttk.Combobox(top_frame, values=['Call', 'SMS', 'Navi', 'Radio'])
combobox.pack(side=tk.LEFT)
combobox.bind('<<ComboboxSelected>>', on_select)

query_listbox_frame = tk.Frame(cmd_frame)
query_listbox_frame.pack(side=tk.TOP)

var = tk.StringVar()
# var.set((1, 2, 3))

query_listbox = tk.Listbox(
    query_listbox_frame, listvariable=var, selectmode=SINGLE, width=35, height=8)
query_listbox.pack(side=tk.LEFT)

scrollbar = tk.Scrollbar(query_listbox_frame, orient="vertical")
scrollbar.config(command=query_listbox.yview)
scrollbar.pack(side="left", fill="y")

send_btn_frame = tk.Frame(cmd_frame)
send_btn_frame.pack(side=tk.TOP)

send_btn = tk.Button(send_btn_frame, text='Execute',
                     width=10, command=exe_command)
send_btn.pack(fill=X)

window.call('wm', 'attributes', '.', '-topmost', '1')

window.mainloop()
