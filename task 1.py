import tkinter as tk
from tkinter import ttk, messagebox

# Conversion Logic
def convert_temp():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            c = temp
            f = (c * 9/5) + 32
            k = c + 273.15
        elif unit == "Fahrenheit":
            f = temp
            c = (f - 32) * 5/9
            k = c + 273.15
        elif unit == "Kelvin":
            k = temp
            c = k - 273.15
            f = (c * 9/5) + 32
        else:
            raise ValueError("Invalid unit")

        result_label.config(
            text=f"{c:.2f} °C\n{f:.2f} °F\n{k:.2f} K"
        )
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x350")
root.configure(bg="#1E005A")

# Heading
title = tk.Label(root, text="Temperature Converter", font=("Helvetica", 20, "bold"), fg="yellow", bg="#1E005A")
title.pack(pady=20)

# Input Frame
frame = tk.Frame(root, bg="#2A007F", padx=20, pady=20, bd=0)
frame.pack(pady=10)

# Temperature Entry
entry_temp = tk.Entry(frame, font=("Arial", 14), width=22, justify="center")
entry_temp.pack(pady=10)

# Unit Dropdown
combo_unit = ttk.Combobox(frame, font=("Arial", 14), values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_unit.current(0)
combo_unit.pack(pady=10)

# Convert Button
convert_button = tk.Button(frame, text="Convert", font=("Arial", 14, "bold"), bg="#28a745", fg="white", padx=10, pady=5, command=convert_temp)
convert_button.pack(pady=10, fill="x")

# Result Display
result_label = tk.Label(root, font=("Arial", 14), fg="#FFD700", bg="#1E005A")
result_label.pack(pady=10)

# Footer
footer = tk.Label(root, text="© 2025 Davupati Preethi. All rights reserved.", font=("Arial", 9), fg="lightgray", bg="#1E005A")
footer.pack(side="bottom", pady=10)

root.mainloop()
