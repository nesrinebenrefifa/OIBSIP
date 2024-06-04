import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox
import socket
import threading
class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.username = None
        self.setup_gui()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("Chat Application")

        self.username = self.get_username()

        self.chat_history = scrolledtext.ScrolledText(self.root, width=60, height=20)
        self.chat_history.pack(pady=10)

        self.message_entry = tk.Entry(self.root, width=50)
        self.message_entry.pack(side=tk.LEFT, padx=10)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def get_username(self):
        return simpledialog.askstring("Username", "Enter your username:", parent=self.root)

    # Reste du code...



    def send_message(self):
        message = self.message_entry.get()
        if message:
            try:
                self.client_socket.send(bytes(f"{self.username}: {message}", "utf-8"))
                self.message_entry.delete(0, tk.END)
            except Exception as e:
                messagebox.showerror("Error", f"Error sending message: {e}")

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                self.chat_history.insert(tk.END, f"{message}\n")
            except Exception as e:
                messagebox.showerror("Error", f"Error receiving message: {e}")
                break

    def start(self):
        try:
            self.client_socket.connect((self.host, self.port))
            self.client_socket.send(bytes(self.username, "utf-8"))
            threading.Thread(target=self.receive_messages).start()
            self.root.mainloop()
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to server: {e}")
            self.root.destroy()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.client_socket.close()
            self.root.destroy()

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 5555
    client = ChatClient(HOST, PORT)
    client.start()
