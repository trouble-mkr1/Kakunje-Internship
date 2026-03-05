import tkinter as tk
import random

def password():
    length = int(e.get())
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-="
    password = ''.join(random.choice(chars) for _ in range(length))
    pswd.set(password)

root = tk.Tk()
root.title("Task 1: Random Password Generator")
root.geometry("500x500")
tk.Label(root, text="Enter Password Length: ").pack(pady=5)
e = tk.Entry(root)
e.pack(pady=5)
tk.Button(root, text="Generate Password", command=password).pack(pady=10)
pswd = tk.StringVar()
tk.Entry(root, textvariable=pswd, width=30).pack(pady=5)
root.mainloop()

###################################################################################################
###################################################################################################

import tkinter as tk

def tables():
    n = int(e.get())

    for i in range(1, 11):
        r.insert(tk.END, f"{n} x {i} = {n*i}\n")

root = tk.Tk()
root.title("Task 2: Multiplication Table Generator ")
root.geometry("500x500")
tk.Label(root, text="Enter a Number:").pack(pady=5)
e = tk.Entry(root)
e.pack(pady=5)
tk.Button(root, text="Generate Table", command=tables).pack(pady=10)
r = tk.Text(root, height=10, width=25)
r.pack(pady=5)

root.mainloop()
###################################################################################################
###################################################################################################

import tkinter as tk
import random

def roll():
    n = random.randint(1, 6)
    r.set(f"Dice Rolled: {n}")

root = tk.Tk()
root.title("Task 3: Simple Dice Rolling Simulator ")
root.geometry("200x200")
tk.Button(root, text="Roll Dice", command=roll).pack(pady=20)
r = tk.StringVar()
tk.Label(root, textvariable=r, font=("Arial", 14)).pack(pady=10)
root.mainloop()

###################################################################################################
###################################################################################################

import tkinter as tk
import random

n = random.randint(1, 10)

def guess():
    guess = int(e.get())

    if guess == n:
        r.set("Correct Guess!")
    else:
        r.set("Wrong Guess! Try Again.")

root = tk.Tk()
root.title("task 4: Random Number Guessing Game ")
root.geometry("300x300")
tk.Label(root, text="Guess a Number between 1 to 10").pack(pady=5)
e = tk.Entry(root)
e.pack(pady=5)
tk.Button(root, text="Check", command=guess).pack(pady=10)
r = tk.StringVar()
tk.Label(root, textvariable=r).pack(pady=5)
root.mainloop()

###################################################################################################
###################################################################################################

import tkinter as tk

def count():
    t = text.get("1.0", tk.END)
    words = len(t.split())
    chars = len(t.strip())
    r.set(f"Words: {words} \t Characters: {chars}")

root = tk.Tk()
root.title("Task 5: Word Counter")
root.geometry("400x350")
text = tk.Text(root, height=10, width=40)
text.pack(pady=10)
tk.Button(root, text="Count", command=count).pack(pady=5)
r = tk.StringVar()
tk.Label(root, textvariable=r).pack(pady=5)
root.mainloop()