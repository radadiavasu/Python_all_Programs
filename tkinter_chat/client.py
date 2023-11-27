import tkinter as tk
from tkinter import messagebox
import socket
import threading

from server import ChatServer

class ChatClient:
    def __init__(self, root, host="localhost", port=5555):
        self.username = None
        self.client = None

        self.root = root
        self.root.title("Chat Program")

        self.login_page()

        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((host, port))
        except:
            messagebox.showinfo("Error", "Could not connect to the server.")

        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

    def login_page(self):
        self.username_label = tk.Label(self.root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        self.login_button = tk.Button(self.root, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        self.username = self.username_entry.get()
        if self.username != "":
            self.client.send(self.username.encode('utf-8'))
            self.username_label.pack_forget()
            self.username_entry.pack_forget()
            self.login_button.pack_forget()
            self.show_chat_page()
        else:
            messagebox.showinfo("Error", "Please enter a valid username.")

    def show_chat_page(self):
        self.message_frame = tk.Frame(self.root)
        self.message_frame.pack(pady=10)

        self.message_listbox = tk.Listbox(self.message_frame, width=50, height=20)
        self.message_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.message_frame, orient=tk.VERTICAL)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.message_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.message_listbox.yview)

        self.chat_entry = tk.Entry(self.root, width=50)
        self.chat_entry.pack()

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

        self.root.bind('<Return>', lambda event: self.send_message())

        self.chat_entry.focus()

    def send_message(self):
        message = self.chat_entry.get()
        if message != "":
            self.client.send(message.encode('utf-8'))
            self.chat_entry.delete(0, tk.END)
            self.chat_entry.focus()

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.message_listbox.insert(tk.END, message)
            except:
                messagebox.showinfo("Error", "Lost connection to the server.")
                self.client.close()
                self.root.quit()
                break

if __name__ == "__main__":
    root = tk.Tk()
    client = ChatServer