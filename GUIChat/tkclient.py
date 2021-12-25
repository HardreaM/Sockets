import socket
import threading
import tkinter as tk
from tkinter import messagebox

sock = socket.socket()

sock.connect(('127.0.0.1', 9090))

def get(sock, x):
    global main, top, root
    while True:
        print(True)
        data = sock.recv(400)
        print(data.decode("utf-8"))

def send():
    global sock
    data1 = data.get()
    sock.send(bytes(data1, encoding="utf-8"))

x = 0

class Application:
    @staticmethod
    def set_widgets(root_window, text):
        tk.Label(root_window).pack()
        tk.Label(root_window, text=text).pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Левый")
    root.geometry("600x650")

    top = tk.Toplevel()
    top.title("Правый")
    top.geometry("600x650")

    data = tk.StringVar()
    data_entry = tk.Entry(textvariable=data)
    data_entry.place(relx=.5, rely=.1, anchor="c")
    data_button = tk.Button(text="Send", command=send)
    data_button.place(relx=.5, rely=.5, anchor="c")

    main = Application()
    main.set_widgets(root, "Send")
    main.set_widgets(top, "Get")

    root.mainloop()

    t1 = threading.Thread(target=get, args=(sock, x), daemon=True)
    #t2 = threading.Thread(target=send, args=(sock, x), daemon=True)

    t1.start()
    #t2.start()

    t1.join()
    #t2.join()