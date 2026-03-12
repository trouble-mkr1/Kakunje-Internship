import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def analyze_marks():
    Name = name.get()
    Python = int(python.get())
    Java = int(java.get())
    C = int(c.get())
    Sql = int(sql.get())

    data = {
        "Subject": ["Python", "JAVA", "C", "SQL"],
        "Marks": [Python, Java, C, Sql]
    }
    df = pd.DataFrame(data)

    total = np.sum(df["Marks"])
    avg = np.mean(df["Marks"])
    highest = np.max(df["Marks"])
    lowest = np.min(df["Marks"])
    result.config(text = f"Total marks: {total}\n Average marks: {avg}\n Highest marks: {highest}\n Lowest marks: {lowest}")

    plt.bar(df["Subject"], df["Marks"])
    plt.title(f"{Name} - Subject wise Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.show()

root = tk.Tk()
root.title("Student Result Analysis System")
root.geometry("500x500")
root.configure(bg = "white")

heading = tk.Label(root, text = "STUDENT RESULT ANALYSIS SYSTEM",
                   font = ("Calibri", 20, "bold"),
                   fg = "white", bg = "blue")
heading.pack()

tk.Label(root, text = "Student Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text = "Python marks:").pack()
python = tk.Entry(root)
python.pack()

tk.Label(root, text = "JAVA marks:").pack()
java = tk.Entry(root)
java.pack()

tk.Label(root, text = "C marks:").pack()
c = tk.Entry(root)
c.pack()

tk.Label(root, text = "SQL marks:").pack()
sql = tk.Entry(root)
sql.pack()

tk.Button(root, text = "Analyze result", command = analyze_marks).pack()

result = tk.Label(root, text = "")
result.pack()

root.mainloop()