# Simple Tkinter To-Do GUI
import tkinter as tk
from tkinter import simpledialog, messagebox

FILE = 'tasks_gui.txt'

def load_tasks():
    try:
        with open(FILE,'r') as f:
            return [line.strip() for line in f if line.strip()]
    except:
        return []

def save_tasks(tasks):
    with open(FILE,'w') as f:
        for t in tasks:
            f.write(t + '\n')

def add_task():
    t = simpledialog.askstring('Task', 'Enter task:')
    if t:
        listbox.insert(tk.END, t)
        save_tasks(list(listbox.get(0, tk.END)))

def remove_task():
    sel = listbox.curselection()
    if not sel:
        messagebox.showinfo('Info','Select a task first')
        return
    listbox.delete(sel[0])
    save_tasks(list(listbox.get(0, tk.END)))

root = tk.Tk()
root.title('To-Do App')
listbox = tk.Listbox(root, width=50)
listbox.pack(padx=10, pady=10)
btn_frame = tk.Frame(root)
btn_frame.pack(padx=10, pady=5)
tk.Button(btn_frame, text='Add', command=add_task).pack(side='left', padx=5)
tk.Button(btn_frame, text='Remove', command=remove_task).pack(side='left', padx=5)
for t in load_tasks():
    listbox.insert(tk.END, t)
root.mainloop()
