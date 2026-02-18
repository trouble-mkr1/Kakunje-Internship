
import multiprocessing as mp

def num():
    for i in range(2, 11, 2):
        print(f"even number: {i}")
    
if __name__ == "__main__":
    p = mp.Process(target = num)
    p.start()
    p.join()
    print("main process finished")

# create a multiple process
def task(name):
    print(f"task {name} is running")

if __name__ == "__main__":
    processes = []
    for i in range(2):
        p = mp.Process(target=task, args = (i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    
    print("all tasks completed")



# Tkinter is a built in library used to design dashboards/UI
import tkinter as tk

def hello():
    l.config(text  = "hello from tkinter") #[7.1]this means that, the label "l" will get changed to what we changed it into in this function

#basic tk window
root = tk.Tk() #[1] this method creates a page named "root"
root.title("my first Tkinter app") #[2]creates a name for the page
root.geometry("300x200") #[4] to set the pixels, as in size of the page when run(breadth and height)

l = tk.Label(root, text = "click the button") # [5]"Label" creates a label in the page "root" and the text content in the label is "text = ..."
l.pack() #[6] this will ensure that the label as been applied and its visible in the page

b = tk.Button(root, text = "Click me", command = hello) # [7]the command is like the action, like when u click the button, it will run the function named "hello"
b.pack()


root.mainloop() #[3]to run the page



import tkinter as tk

def add():
    a = int(e1.get()) #get is a function to collect the value from the input and we convert it into int using "int()""
    b = int(e2.get())
    r.config(text = f"Result = {a+b}")


root = tk.Tk()
root.title("calculator")
root.geometry("300x300")
root.configure(bg = "lightblue") # any changes to the root, like page color, we should use the method "configure". only for changing the content like labels or buttons we use "config"
l1 = tk.Label(root, text = "enter first number", bg = "lightblue", fg = "red", font = ("Arial", 14)) # "bg" is background color and "fg" is for font color and "font" is (font name, size)
l1.pack(pady = "10") # to add a padding
e1 = tk.Entry(root, bg = "lightblue", fg = "red", insertbackground="white") # to create an input field, "insertbackground" is for the curser color
e1.pack(pady = "10")
l2 = tk.Label(root, text = "enter second number", bg = "lightblue", fg = "red", font = ("Arial", 14))
l2.pack(pady = "10")
e2 = tk.Entry(root, bg = "lightblue", fg = "red")
e2.pack(pady = "10")
b = tk.Button(root, text = "ADD", command = add, bg = "lightblue", fg = "red", font = ("Arial", 14),
              activebackground = "green", activeforeground="yellow") #active bg and fg are just the color changes when the button is clicked
b.pack(pady = "10")
r = tk.Label(root, text = "", bg = "lightblue", fg = "red", font = ("Arial", 14))
r.pack(pady = "10")
root.mainloop()



#create messasge box in tkinter
import tkinter as tk
from tkinter import messagebox

def show_msg():
    messagebox.showinfo('Info', "Tkinter is easy") # message box has 2 parameter (message box title, content)
    messagebox.showwarning("warning!!", "be careful") # error will have a different symbol in the pop up msg
    messagebox.showerror("error detected", "something went wrong")
    messagebox.askyesno("confirm?", "do u want to stop learning") # this is a pop up with 2 buttons, yes and no


root = tk.Tk()
root.title("messege box")
root.geometry("200x300")

b = tk.Button(root, text = "show message", command = show_msg)
b.pack()

root.mainloop()



import tkinter as tk

def login():
    if user.get() == "admin" and pwd.get() == "123":
        res.config(text = "Login succesfull")
    else:
        res.config(text = "Invalid Credentials")

root = tk.Tk()
root.title("Login")
root.geometry("500x600")
root.configure(bg = "white")

u = tk.Label(root, text = "Username", bg = "white", font = ("Calibri", 16))
u.pack()

user = tk.Entry(root)
user.pack(pady = "10")

p = tk.Label(root, text = "Password", bg = "white", font = ("Calibri", 16))
p.pack(pady = "10")

pwd = tk.Entry(root, show = "*")
pwd.pack(pady = "10")

l = tk.Button(root, text = "Login", command = login)
l.pack(pady = "10")

res = tk.Label(root, text = "", bg = "white")
res.pack()

root.mainloop()



#Grid Layout
import tkinter as tk

root = tk.Tk()
root.title("Login")
root.geometry("600x200")

tk.Label(root, text = "Username").grid(row=0, column=0)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root, text="password").grid(row=0, column=2)
tk.Entry(root).grid(row=0, column=3)

tk.Button(root, text = "submit").grid(row = 1, column=2)
root.mainloop()

#checkbox(can select 1 and more) and radio button(can select only 1)
import tkinter as tk

def show_choice():
    r.config(text = f"Selected choice is: {choice.get()}")

root = tk.Tk()
root.title("Checkbox and radio")

v = tk.IntVar() # we r creating a variable so that we know if boc is checked(1) or not(0)

cb = tk.Checkbutton(root, text = "I agree", variable=v)
cb.pack()

choice = tk.StringVar()
tk.Radiobutton(root, text = "Python", variable=choice, value="python").pack()
tk.Radiobutton(root, text = "JAVA", variable=choice, value="JAVA").pack()
tk.Button(root, text = "submit", command = show_choice).pack()

r = tk.Label(root, text="")
r.pack()

root.mainloop()

######################################################################################################

######################################################################################################

######################################################################################################

######################################################################################################
'''
Task 1: Create Window
· Create a Tkinter window
· Settitle as “Basic Tkinter”
· Setsize to 400 x 300
· Changewindow background color
'''
import tkinter as tk

root = tk.Tk()
root.title("Basic Tkinter")
root.geometry("400x300")
root.configure(bg = "black")

root.mainloop()

###############################################################################
###############################################################################
'''
Task 2: Simple Label
· Display text “Welcome to Tkinter”
· Changetext color
· Changebackground color
'''
import tkinter as tk

root = tk.Tk()
root.title("Task 2: Simple label")
root.geometry("400x300")
l = tk.Label(root, text = "Welcome to Tkinter", bg = "red", fg = "white")
l.pack()
root.mainloop()

###############################################################################
###############################################################################
'''
Task 3: Font Formatting
· Display your name in a Label
· Changefont size and style
'''
import tkinter as tk

root = tk.Tk()
root.title("Task 3: Font formatting")
l = tk.Label(root, text = "My name is Abdul", font = ("Impact", 23))
l.pack()
root.mainloop()

###############################################################################
###############################################################################
'''
Task 4: Multiple Labels
· Display 3 labels
· Eachlabel should have different text color
· Addpadding between labels
'''
import tkinter as tk

root = tk.Tk()
root.title("Task 4: Multiple label")
root.geometry("200x200")
l1 = tk.Label(root, text = "This text is in red", fg = "red")
l1.pack(pady = "10")
l2 = tk.Label(root, text = "This text is in brown", fg = "brown")
l2.pack(pady = "10")
l3 = tk.Label(root, text = "this text is in cyan", fg = "cyan")
l3.pack(pady = "10")
root.mainloop()

###############################################################################
###############################################################################
'''
Task 5: Simple Button
· Create a button with text “Submit”
· Changebutton background color
· Changetext color
'''
import tkinter as tk

root = tk.Tk()
root.title("Task 5: Simple button")
root.geometry("500x500")
b = tk.Button(root, text = "Submit", bg = "lightblue", fg = "purple")
b.pack()
root.mainloop()

###############################################################################
###############################################################################
'''
Task 6: Button Action
· Onbutton click, change label text
· Changelabel color on click
'''
import tkinter as tk

def changes():
    l.config(text = "this is after the label changes", bg = "lightgreen", fg = "blue")

root = tk.Tk()
root.title("Task 6: Button action")
root.geometry("500x500")
l = tk.Label(root, text = "label before change", bg = "red", fg = "white")
l.pack(pady = "10")
b = tk.Button(root, text = "Click to change the label text and color to something else", bg = "lightblue",
              fg = "purple", command = changes)
b.pack()
root.mainloop()

###############################################################################
###############################################################################
'''
Task 7: Entry Widget
· Create an Entry box
· Changebackground color
· Changetext color
'''
import tkinter as tk

root = tk.Tk()
root.title("Task 7: Entry Widget")
root.geometry("500x500")
e = tk.Entry(root, bg = "cyan", fg = "purple")
e.pack()
root.mainloop()

###############################################################################
###############################################################################
'''
Task 8: Read Input
· Takeuser name using Entry
· Display input using Label
'''
import tkinter as tk

def show():
    res.config(text = f"the username entered is {e.get()}")

root = tk.Tk()
root.title("Task 8: Read input")
root.geometry("500x500")
l = tk.Label(root, text = "Enter username")
l.pack()
e = tk.Entry(root, bg = "cyan", fg = "purple")
e.pack(pady = 5)
b = tk.Button(root, text = "Click to show the entered username below",command = show, fg = "blue")
b.pack()
res = tk.Label(root, text = "")
res.pack()
root.mainloop()

###############################################################################
###############################################################################
'''
Task 9: Grid Layout
· Create a simple form:
o Name
o Age
· Usegrid layout
'''
import tkinter as tk

root = tk.Tk()
root.title("Task 9: Grid Layout")
root.geometry("500x500")
tk.Label(root, text = "Enter Name").grid(row = 0, column = 0)
tk.Entry(root, bg = "cyan", fg = "purple").grid(row = 0, column = 1)
tk.Label(root, text = "Enter Age").grid(row = 1, column = 0)
tk.Entry(root, bg = "cyan", fg = "purple").grid(row = 1, column = 1)
root.mainloop()

###############################################################################
###############################################################################
'''
Task 10: Multiple Color Buttons
· Create 3 buttons:
o Red
o Green
o Blue
· Clicking each button should change window background color
'''
import tkinter as tk

def color1():
    root.configure(bg = "brown")
def color2():
    root.configure(bg = "yellow")
def color3():
    root.configure(bg = "purple")

root = tk.Tk()
root.title("Task 10: Multiple Color Buttons")
root.geometry("500x500")
b1 = tk.Button(root, text = "Click to change background to brown", command = color1)
b1.pack(pady = 5)
b2 = tk.Button(root, text = "Click to change background to yellow", command = color2)
b2.pack(pady = 5)
b3 = tk.Button(root, text = "Click to change background to purple", command = color3)
b3.pack()
root.mainloop()

###############################################################################
###############################################################################
'''
Task 11: Mouse Click
· Display text “Mouse Clicked” on button click
'''
import tkinter as tk

def show():
    l.config(text = "MOUSE CLICKED")

root = tk.Tk()
root.title("Task 11: Mouse Click")
root.geometry("500x500")
b = tk.Button(root, text = "Click button", bg = "lightblue", fg = "purple", command = show)
b.pack(pady = "5")
l = tk.Label(root, text = "")
l.pack()
root.mainloop()

###############################################################################
###############################################################################
'''
Task 12: Radio Button Selection
· Create radio buttons for Male / Female
· Display selected value on button click
'''
#checkbox(can select 1 and more) and radio button(can select only 1)
import tkinter as tk

def show_choice():
    r.config(text = f"Selected choice is: {choice.get()}")

root = tk.Tk()
root.title("Task 12: Radio Button Selection")
root.geometry("500x500")
choice = tk.StringVar()
tk.Label(root, text = "Select gender").pack()
tk.Radiobutton(root, text = "Male", variable=choice, value="MALE").pack()
tk.Radiobutton(root, text = "Female", variable=choice, value="FEMALE").pack()
tk.Button(root, text = "submit", command = show_choice).pack()
r = tk.Label(root, text="")
r.pack()

root.mainloop()

###############################################################################
###############################################################################
'''
Task 13: Message Box
· Showinfo, warning, and error messages
· Trigger messages using different buttons
'''
import tkinter as tk
from tkinter import messagebox

def info_msg():
    messagebox.showinfo('Info Message', "you have clicked the info button")
def warning_msg():
    messagebox.showwarning("warning Message!!", "you have clicked the warning button")
def error_msg():
    messagebox.showerror("ERROR MESSAGE!!!", "you have clicked the ERROR button")

root = tk.Tk()
root.title("Task 13: Message Box")
root.geometry("500x500")

b1 = tk.Button(root, text = "Click to show info", command = info_msg)
b1.pack(pady = 5)
b2 = tk.Button(root, text = "Click to show warning", command = warning_msg)
b2.pack(pady = 5)
b3 = tk.Button(root, text = "Click to error", command = error_msg)
b3.pack()

root.mainloop()

###############################################################################
###############################################################################
'''
Task 14: Confirmation Dialog
· Ask “Do you want to exit?”
· Closewindow only if user clicks Yes
'''
import tkinter as tk
from tkinter import messagebox

def confirm_msg():
    choice = messagebox.askyesno('Confirm Exit??', "you have clicked the exit button, are you sure you want to exit?")
    if choice:
        root.destroy()

root = tk.Tk()
root.title("Task 14: Confirm Dialogue")
root.geometry("500x500")

b1 = tk.Button(root, text = "Click to exit", bg = "lightblue", fg = "purple", command = confirm_msg)
b1.pack(pady = 5)

root.mainloop()

###############################################################################
###############################################################################
'''
Task 15: Theme Change
· Add button to switch between Light & Dark mode
'''
import tkinter as tk

def change():
    if root["bg"] == "white":
        root.config(bg="black")
        l.config(text = "The theme is now is Dark mode", bg="gray", fg="white")
        b.config(text="change to Light Mode", bg="gray", fg="white")
    else:
        root.config(bg="white")
        l.config(text = "The theme is now is Light mode")
        b.config(text="change to Dark Mode", bg="lightgray", fg="black")

root = tk.Tk()

root.title("Task 15: Theme Change")
root.geometry("500x500")
root.config(bg="white")
l = tk.Label(root, text = "The theme is now is Light mode", bg="lightgray", fg="black")
l.pack(pady = "5")
b = tk.Button(root, text="change to Dark Mode", command=change)
b.pack(pady= "5")

root.mainloop()

###############################################################################
###############################################################################