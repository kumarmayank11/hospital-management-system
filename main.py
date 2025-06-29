import tkinter as tk
from tkinter import ttk, messagebox

patients = []

def add_patient():
    name = name_entry.get()
    age = age_entry.get()
    disease = disease_entry.get()
    if name and age and disease:
        patients.append({"name": name, "age": age, "disease": disease})
        update_listbox()
        clear_fields()
    else:
        messagebox.showwarning("Input Error", "All fields are required!")

def update_listbox():
    patient_listbox.delete(0, tk.END)
    for p in patients:
        patient_listbox.insert(tk.END, f"{p['name']} | Age: {p['age']} | Disease: {p['disease']}")

def clear_fields():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    disease_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Hospital Management System")
root.geometry("500x400")

tk.Label(root, text="Patient Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Age").pack()
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root, text="Disease").pack()
disease_entry = tk.Entry(root)
disease_entry.pack()

tk.Button(root, text="Add Patient", command=add_patient).pack(pady=10)

patient_listbox = tk.Listbox(root, width=50)
patient_listbox.pack(pady=10)

root.mainloop()
