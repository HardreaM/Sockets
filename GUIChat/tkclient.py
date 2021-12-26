import socket
import threading
import tkinter as tk
from tkinter import *

sock = socket.socket()

sock.connect(('127.0.0.1', 9090))

def get(sock, x):
    global top, textfield
    while True:
        data = sock.recv(400)
        
        set_widgets(top, data.decode("utf-8")+"\n", textfield)

        print(data.decode("utf-8"))

def send():
    global sock
    data1 = data.get()
    intro = str(sock.getsockname()[0]) + ":" + str(sock.getsockname()[1]) + " says: "
    sock.send(bytes(intro+data1, encoding="utf-8"))

def set_widgets(root_window, text, textfield):
        
    textfield.insert(END, text)

x = 0

t1 = threading.Thread(target=get, args=(sock, x), daemon=True)

t1.start()

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Send message")
    root.geometry("300x350")

    top = tk.Toplevel()
    top.title("Chat")
    top.geometry("600x650")

    scroll = tk.Scrollbar(top)
    scroll.pack(side=RIGHT, fill=Y)
    
    textfield = tk.Text(top, height=600, width=650, yscrollcommand=scroll.set)
    textfield.pack()
    textfield.insert(END, "Waiting...\n")

    data = tk.StringVar()
    data_entry = tk.Entry(textvariable=data)
    data_entry.place(relx=.5, rely=.1, anchor="c")
    data_button = tk.Button(text="Send", command=send)
    data_button.place(relx=.5, rely=.5, anchor="c")

    set_widgets(top, "Best python chat\n", textfield)

    root.mainloop()

