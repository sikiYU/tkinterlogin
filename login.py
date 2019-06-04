from tkinter import *
from passlib.hash import pbkdf2_sha256


root = Tk()

def quitbutton():
    root.quit()

def passwords():
    global label
    file = open('passwords.txt', 'r')
    password = file.read()
    label = Label(root, text=password)
    label.grid(row=0, column=4)
    button4.grid_remove()
    enter3.grid_remove()
    enter4.grid_remove()
    file.close()

def addpass():
    global enter3
    global button4
    global enter4
    enter3 = Entry(root)
    enter3.grid(row=0, column=1)
    enter4 = Entry(root, show='*')
    enter4.grid(row=1, column=1)
    button4 = Button(root, text='Enter', command=addpassword)
    button4.grid(row=5, column=4)
    label.grid_remove()

def addpassword():
    file = open('passwords.txt', 'a+')
    password = enter3.get()
    webpage = enter4.get()
    file.write(password)
    file.write(':')
    file.write(webpage)
    file.write('\n')
    file.close()

def signin():
    get1 = enter1.get()
    file = open('output.txt', 'r')
    password = file.readline()
    password2 = pbkdf2_sha256.verify(get1, password)
    button4 = Button(root, text='Back', command=back)
    button4.grid(row=5, column=3)
    button2.grid_remove()
    button3.grid_remove()
    enter1.grid_remove()
    enter2.grid_remove()
    if password2 == True:
        global button5
        global button6
        button5 = Button(root, text='View Passwords', command=passwords)
        button5.grid(row=2, column=3)
        button6 = Button(root, text='Add Passwords', command=addpass)
        button6.grid(row=3, column=3)

    if password2 == False:
        global label2
        label2 = Label(root, text='That is the wrong password')
        label2.grid(row=0, column=4)

    file.close()

def signup():
    global hash
    file = open('output.txt', 'w')
    get1 = enter2.get()
    hash = pbkdf2_sha256.hash(get1)
    file.write(hash)
    file.close()

def back():
    button2.grid()
    button3.grid()
    enter1.grid()
    enter2.grid()
    button5.grid_remove()
    button6.grid_remove()
    enter3.grid_remove()
    label.grid_remove()
    enter4.grid_remove()

button1 = Button(root, text='Quit', command=quitbutton)
button1.grid(row=5, column=5)

button2 = Button(root, text='Sign In', command=signin)
button2.grid(row=0, column=2)

button3 = Button(root, text='Sign Up', command=signup)
button3.grid(row=1, column=2)

enter1 = Entry(root, show='*')
enter1.grid(row=0, column=1)
enter2 = Entry(root, show='*')
enter2.grid(row=1, column=1)

root.mainloop()
