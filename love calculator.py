import tkinter as tk
from tkinter import messagebox

def calculate_love():
    name1 = entry_name1.get()
    name2 = entry_name2.get()
    
    if not name1 or not name2:
        messagebox.showwarning("Input Error", "Both names must be entered!")
        return
    
    combine_string = name1 + name2
    lower_case_string = combine_string.lower()

    t = lower_case_string.count('t')
    r = lower_case_string.count('r')
    u = lower_case_string.count('u')
    e = lower_case_string.count('e')
    true = t + r + u + e

    l = lower_case_string.count('l')
    o = lower_case_string.count('o')
    v = lower_case_string.count('v')
    e = lower_case_string.count('e')
    love = l + o + v + e

    love_score = int(str(true) + str(love))

    if love_score < 10 or love_score > 90:
        result = f"Your score is {love_score}. You go together like Coke and Mentos!"
    elif 40 <= love_score <= 50:
        result = f"Your score is {love_score}. You are alright together."
    else:
        result = f"Your score is {love_score}."

    messagebox.showinfo("Love Calculator Result", result)

# Create main window
root = tk.Tk()
root.title("Love Calculator")

# Create input labels and fields
label_name1 = tk.Label(root, text="Your Name:")
label_name1.grid(row=0, column=0, padx=10, pady=10)
entry_name1 = tk.Entry(root, width=30)
entry_name1.grid(row=0, column=1, padx=10, pady=10)

label_name2 = tk.Label(root, text="Their Name:")
label_name2.grid(row=1, column=0, padx=10, pady=10)
entry_name2 = tk.Entry(root, width=30)
entry_name2.grid(row=1, column=1, padx=10, pady=10)

# Create calculate button
button_calculate = tk.Button(root, text="Calculate Love Score", command=calculate_love)
button_calculate.grid(row=2, column=0, columnspan=2, pady=20)

# Run the application
root.mainloop()
