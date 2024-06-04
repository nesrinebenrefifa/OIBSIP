import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("500x500")
        self.label_length = tk.Label(master, text="Password Length: ",font="Tahoma 10 bold")
        self.label_length.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_length = tk.Entry(master, width=10)
        self.entry_length.grid(row=0, column=1, padx=10, pady=10)

        self.label_letters = tk.Label(master, text="Include Letters:")
        self.label_letters.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.var_letters = tk.BooleanVar()
        self.check_letters = tk.Checkbutton(master, variable=self.var_letters)
        self.check_letters.grid(row=1, column=1, padx=10, pady=10)

        self.label_numbers = tk.Label(master, text="Include Numbers:")
        self.label_numbers.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.var_numbers = tk.BooleanVar()
        self.check_numbers = tk.Checkbutton(master, variable=self.var_numbers)
        self.check_numbers.grid(row=2, column=1, padx=10, pady=10)

        self.label_symbols = tk.Label(master, text="Include Symbols:")
        self.label_symbols.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.var_symbols = tk.BooleanVar()
        self.check_symbols = tk.Checkbutton(master, variable=self.var_symbols)
        self.check_symbols.grid(row=3, column=1, padx=10, pady=10)

        self.button_generate = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.button_generate.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        self.label_result = tk.Label(master, text="")
        self.label_result.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        self.button_copy = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.button_copy.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        length = int(self.entry_length.get())
        use_letters = self.var_letters.get()
        use_numbers = self.var_numbers.get()
        use_symbols = self.var_symbols.get()

        characters = ''
        if use_letters:
            characters += string.ascii_letters
        if use_numbers:
            characters += string.digits
        if use_symbols:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "No character set selected.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        self.label_result.config(text=f"Generated Password: {password}")

    def copy_to_clipboard(self):
        passw = self.label_result.cget("text").split(": ")[1]
        pyperclip.copy(passw)
        messagebox.showinfo("Success", "Password copied to clipboard!")

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
