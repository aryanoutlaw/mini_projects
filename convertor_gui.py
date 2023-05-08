import tkinter as tk
import ttkbootstrap as ttk

def convert_miles_to_km():
    try:
        miles_input = float(entry_var.get())
        km_output = miles_input * 1.61
        output_var.set(f"{km_output:.2f} kilometers")
    except ValueError:
        output_var.set("Please enter a valid number")

def clear_fields():
    entry_var.set("")
    output_var.set("Output")

# window
window = ttk.Window(themename="cyborg")
window.title("Miles to Kilometers")
window.geometry("300x150")

# title
title_label = ttk.Label(
    master=window, text="Miles to Kilometers", font="calibri 24 bold")
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_var = tk.StringVar()
entry = ttk.Entry(
    master=input_frame, textvariable=entry_var, width=10, font="calibri 12")
entry.pack(side="left", padx=10)
convert_button = ttk.Button(
    master=input_frame, text="Convert", command=convert_miles_to_km)
convert_button.pack(side="left")
input_frame.pack(pady=10)

# output
output_var = tk.StringVar()
output_label = ttk.Label(
    master=window, text="Output", font="calibri 18", textvariable=output_var)
output_label.pack(pady=5)

# clear button
clear_button = ttk.Button(
    master=window, text="Clear", command=clear_fields)
clear_button.pack(pady=5)

# run
window.mainloop()
