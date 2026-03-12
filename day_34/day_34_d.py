import tkinter as tk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def check_quiz():

    student = name.get()
    correct = 0
    wrong = 0

    if q1.get() == "New Delhi":
        correct += 1
    else:
        wrong += 1

    if q2.get() == "Mars":
        correct += 1
    else:
        wrong += 1

    if q3.get().lower() == "ganga":
        correct += 1
    else:
        wrong += 1

    if q4.get().lower() == "7":
        correct += 1
    else:
        wrong += 1

    if q5.get() == "Python":
        correct += 1
    else:
        wrong += 1

    score = correct * 2

    data = {
        "Student": [student],
        "Correct": [correct],
        "Wrong": [wrong],
        "Score": [score]
    }

    df = pd.DataFrame(data)
    total = np.sum(df["Score"])
    result.config(text=f"Correct: {correct}\nWrong: {wrong}\nScore: {total}")

    plt.bar(["Correct","Wrong"], [correct,wrong])
    plt.title("Quiz Result")
    plt.show()


root = tk.Tk()
root.title("Quiz Result Analyzer")
root.geometry("500x500")

tk.Label(root,text="Student Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text = "__________________________________________________________").pack()

tk.Label(root, text="1. What is the capital of India?").pack()
q1 = tk.StringVar()
tk.Radiobutton(root, text = "Delhi", variable = q1, value = "Delhi").pack()
tk.Radiobutton(root, text = "New Delhi", variable = q1, value = "New Delhi").pack()

tk.Label(root, text="2. Which planet is also known as the \"Red Planet\"?").pack()
q2 = tk.StringVar()
tk.Radiobutton(root, text = "Mars", variable = q2, value = "Mars").pack()
tk.Radiobutton(root, text = "Venus", variable = q2, value = "Venus").pack()

tk.Label(root, text = "3. Which is the longest river in India?").pack()
q3 = tk.Entry(root)
q3.pack()

tk.Label(root, text = "4. How many continents are there in the world?").pack()
q4 = tk.Entry(root)
q4.pack()

tk.Label(root, text="5. Which is the best language for building AI?").pack()
q5 = tk.StringVar()
tk.Radiobutton(root, text = "Python", variable = q5, value = "Python").pack()
tk.Radiobutton(root, text = "Java", variable = q5, value = "Java").pack()

tk.Label(root, text = "__________________________________________________________").pack()

tk.Button(root, text = "Submit Quiz", command = check_quiz).pack(pady=20)

result = tk.Label(root, text="")
result.pack()

root.mainloop()