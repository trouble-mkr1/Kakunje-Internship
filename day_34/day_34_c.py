import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze():

    data = {
        "Name": [],
        "Category": [],
        "Copies": []
    }

    Name = name.get()
    category = cat.get()
    copies = int(n.get())

    data["Name"].append(Name)
    data["Category"].append(category)
    data["Copies"].append(copies)
    df = pd.DataFrame(data)

    total = np.sum(df["Copies"])
    avg = np.mean(df["Copies"])

    result.config(text=f"Total Books: {total}\nAverage Copies: {avg}")

    plt.bar(df["Category"], df["Copies"])
    plt.xlabel("Category")
    plt.ylabel("Copies")
    plt.title("Category-wise Book Distribution")
    plt.show()

root = tk.Tk()
root.title("Library Book Data Analyzer")
root.geometry("500x500")

tk.Label(root, text="Library Book Analyzer",
         font=("Arial",16,"bold")).pack(pady=30)

tk.Label(root, text="Book Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Select Category").pack()
cat = tk.StringVar()
tk.Radiobutton(root, text="Fiction", variable=cat, value="Fiction").pack()
tk.Radiobutton(root, text="Sci-Fi", variable=cat, value="Sci-Fi").pack()
tk.Radiobutton(root, text="History", variable=cat, value="History").pack()

tk.Label(root, text="Number of Copies").pack()
n = tk.Entry(root)
n.pack()

tk.Button(root, text="Submit", command=analyze).pack(pady=10)

result = tk.Label(root, text="")
result.pack(pady=10)

root.mainloop()