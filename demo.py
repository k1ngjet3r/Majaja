'''
    this code is from
    https://blog.furas.pl/python-tkinter-how-to-update-widgets-using-value-selected-in-combobox.html?fbclid=IwAR15pWtIEdo0ST9BPw7nnTPrSJ6nHZVTU81Ez_RbfltHem3vCPkNm_t8Ta0
'''

import tkinter as tk
import tkinter.ttk as ttk

# --- functions ---


def on_select(event):
    print('[DEBUG] event:', event)
    print('[DEBUG] event.widget:', event.widget)
    print('[DEBUG] event.widget.get():', event.widget.get())
    print('---')

    selected = event.widget.get()

    label['text'] = selected

    button['text'] = selected

    entry.delete('0', 'end')  # remove previous content
    entry.insert('end', selected)

    combobox2_values = {
        'A': ['A1', 'A2', 'A3'],
        'B': ['B1', 'B2', 'B3'],
        'C': ['C1', 'C2', 'C3'],
    }

    combobox2['values'] = combobox2_values[selected]

    listbox.delete(0, 'end')  # remove previous content
    for item in combobox2_values[selected]:
        listbox.insert('end', item)

    values = combobox2_values[selected]
    values_str = ', '.join(values)

    # text.delete('1.0', 'end')  # remove previous content
    text.insert('end', selected + ': ' + values_str + '\n')

# --- main ---


root = tk.Tk()

combobox = ttk.Combobox(root, values=['A', 'B', 'C'])
combobox.pack()

combobox.bind('<<ComboboxSelected>>', on_select)

# --- other widgets ---

label = tk.Label(root, text='?')
label.pack()

button = tk.Button(root, text='?')
button.pack()

entry = tk.Entry(root)
entry.pack()
#entry.insert(0, '?')
#entry.insert('end', '?')

combobox2 = ttk.Combobox(root)
combobox2.pack()

listbox = tk.Listbox(root)
listbox.pack()

text = tk.Text(root, width=30, height=10)
text.pack()
#text.insert('1.0', '?\n')
#text.insert('end', '?\n')

# ---

root.mainloop()
