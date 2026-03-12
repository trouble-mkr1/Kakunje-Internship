import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def track():
    Date = date.get()
    Travel = int(travel.get())
    Food = int(food.get())
    Grocery = int(grocery.get())
    Misc = int(misc.get())

    data = {
        "Type": ["Travel", "Food", "Grocery", "Misc"],
        "Expense": [Travel, Food, Grocery, Misc]
    }
    df = pd.DataFrame(data)

    total = np.sum(df["Expense"])
    avg = np.mean(df["Expense"])
    result.config(text = f"Total Expense is {total}\n"\
                  "Average Expense is {avg}")

    plt.pie(df["Expense"], labels = df["Type"])
    plt.title(f"Expense chart for {Date}")
    plt.show()
    
root = tk.Tk()
root.title("Personal Expense Tracker")
root.geometry("500x500")
root.configure(bg = "white")

heading = tk.Label(text = "Personal Expense Tracker",
                   font = ("Calibri", 20, "bold"),
                   fg = "white", bg = "blue")
heading.pack(pady = "25")

tk.Label(root, text = "Enter the date").pack()
date = tk.Entry(root)
date.pack(pady = "20")

tk.Label(root, text = "Enter the Travel Expense").pack()
travel = tk.Entry(root)
travel.pack(pady = "10")

tk.Label(root, text = "Enter the Food Expense").pack()
food = tk.Entry(root)
food.pack(pady = "10")

tk.Label(root, text = "Enter the Grocery Expense").pack()
grocery = tk.Entry(root)
grocery.pack(pady = "10")

tk.Label(root, text = "Enter the Misc Expense").pack()
misc = tk.Entry(root)
misc.pack(pady = "10")

tk.Button(root, text = "Track Expense", command = track).pack()

result = tk.Label(root, text = "")
result.pack()

root.mainloop()