import tkinter as tk
from tkinter import ttk

# stats
country_data = {
    "Argentina": {"Capital": "Buenos Aires", "Currency": "Argentine Peso", "Continent": "South America", "Language": "Spanish"},
    "Australia": {"Capital": "Canberra", "Currency": "Australian Dollar", "Continent": "Oceania", "Language": "English"},
    "Brazil": {"Capital": "Brasilia", "Currency": "Brazilian Real", "Continent": "South America", "Language": "Portuguese"},
    "Canada": {"Capital": "Ottawa", "Currency": "Canadian Dollar", "Continent": "North America", "Language": "English, French"},
    "China": {"Capital": "Beijing", "Currency": "Renminbi (Yuan)", "Continent": "Asia", "Language": "Mandarin"},
    "France": {"Capital": "Paris", "Currency": "Euro", "Continent": "Europe", "Language": "French"},
    "India": {"Capital": "New Delhi", "Currency": "Indian Rupee", "Continent": "Asia", "Language": "Hindi, English"},
    "Japan": {"Capital": "Tokyo", "Currency": "Yen", "Continent": "Asia", "Language": "Japanese"},
    "Nigeria": {"Capital": "Abuja", "Currency": "Naira", "Continent": "Africa", "Language": "English"},
    "United Kingdom": {"Capital": "London", "Currency": "Pound Sterling", "Continent": "Europe", "Language": "English"}
}

# setup
root = tk.Tk()
root.title("Country Info Picker")
root.geometry("400x350")
root.configure(bg="#0B0B25") 

# widgets
title = tk.Label(root, text="Select A Country:", font=("Geograph", 16, "bold"), bg="#0B0B25", fg="white")
title.pack(pady=10)

result_label = tk.Label(root, text="", justify="left", font=("Geograph", 11, "bold"), bg="#0B0B25", fg="white")
result_label.pack(pady=20)

#  output
def show_info():
    selected = country_var.get()
    if selected in country_data:
        info = country_data[selected]
        result_label.config(text=f"Capital: {info['Capital']}\n"
                                 f"Currency: {info['Currency']}\n"
                                 f"Continent: {info['Continent']}\n"
                                 f"Language: {info['Language']}")

def toggle_theme():
    if root["bg"] == "#f0f9ff":
        root.configure(bg="#0B0B25")
        title.config(bg="#0B0B25", fg="white")
        result_label.config(bg="#0B0B25", fg="white")
    else:
        root.configure(bg="#f0f9ff")
        title.config(bg="#f0f9ff", fg="#0B0B25")
        result_label.config(bg="#f0f9ff", fg="#0B0B25")

# 5. UI Elements
country_var = tk.StringVar()
dropdown = ttk.Combobox(root, textvariable=country_var, state="readonly")
dropdown['values'] = list(country_data.keys())
dropdown.pack(pady=10)
dropdown.set("Select a Country")

show_btn = tk.Button(root, text="Show Info", command=show_info)
show_btn.pack(pady=10)

theme_btn = tk.Button(root, text="Toggle Theme", command=toggle_theme)
theme_btn.place(x=300, y=10)

root.mainloop()
