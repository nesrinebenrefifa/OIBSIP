import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

def create_database():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bmi_records
                 (id INTEGER PRIMARY KEY, weight REAL, height REAL, bmi REAL, category TEXT, date TEXT)''')
    conn.commit()
    conn.close()

def save_record(weight, height, bmi, category):
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO bmi_records (weight, height, bmi, category, date) VALUES (?, ?, ?, ?, datetime('now'))", 
              (weight, height, bmi, category))
    conn.commit()
    conn.close()

def view_history():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bmi_records")
    records = c.fetchall()
    conn.close()

    for record in records:
        print(record)

def plot_trend():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("SELECT date, bmi FROM bmi_records")
    records = c.fetchall()
    conn.close()

    dates = [record[0] for record in records]
    bmis = [record[1] for record in records]

    plt.plot(dates, bmis, marker='o')
    plt.xlabel('Date')
    plt.ylabel('BMI')
    plt.title('BMI Trend Over Time')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def calculate_bmi(weight, height):
    return weight / (height ** 2)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def on_calculate():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
        if weight <= 0 or height <= 0:
            raise ValueError
        
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        save_record(weight, height, bmi, category)
        
        label_result['text'] = f"BMI: {bmi:.2f}\nCategory: {category}"
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter positive numbers for weight and height.")

create_database()

app = tk.Tk()
app.title("BMI Calculator")
app.geometry("500x600")

tk.Label(app, text="Weight (kg):",font="20,bold", fg="blue",padx=20).grid(row=0, column=0)
entry_weight = tk.Entry(app)
entry_weight.grid(row=0, column=1)

tk.Label(app, text="Height (m):", font="20,bold",fg="blue",padx=20).grid(row=1, column=0)
entry_height = tk.Entry(app)
entry_height.grid(row=1, column=1)

tk.Button(app, text="Calculate", command=on_calculate, fg="blue",bg="yellow",font="20,bold",padx=20).grid(row=2, column=0, columnspan=2)
tk.Button(app, text="View History", command=view_history, fg="blue",bg="yellow",font="20,bold",padx=20, ).grid(row=3, column=0, columnspan=4)
tk.Button(app, text="Plot Trend", command=plot_trend , fg="blue",bg="yellow",font="20,bold",padx=20).grid(row=4, column=0, columnspan=2)

label_result = tk.Label(app, text="BMI: \nCategory: ")
label_result.grid(row=5, column=0, columnspan=2)

app.mainloop()
