from pynput import keyboard
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

def timestamp():
    return datetime.now().strftime('%d %H:%M:%S')

def on_press(key):
    frame.insert(f'{timestamp()} [{key}] + '"\n")

def on_release(key):
    frame.insert(f'{timestamp()} [{key}] - released')
    if key == keyboard.Key.esc:
        return False



#-----------------------------tkinter----------------------------------
root = tk.Tk()
root.title("password_simulator")
root.geometry("600x400")

folder_path_var = tk.StringVar()

label = tk.Label(root, text="", font=("Arial", 16))
label.pack(pady=10)

frame = tk.Text(root)
frame.pack(pady=5)

def listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

threading.Thread(target=listener, daemon=True).start()
root.mainloop()