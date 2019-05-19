from tkinter import *

root = Tk()

class App():
    def quitbutton(self):
        button = Button(root, text='Quit', command=self.rootquit)
        button.grid(row=3, column=0)

    def rootquit(self):
        root.quit()

    def entry(self):
        global enter1
        global enter2
        enter1 = Entry(root)
        enter1.grid(row=1, column=0)
        enter2 = Entry(root)
        enter2.grid(row=1, column=1)


    def signin(self):
        get1 = enter1.get()
        file = open('output.txt', 'r')
        password = file.readline()
        if get1 == password:
            global label
            label = Label(root, text='You are in!')
            label.grid(row=0, column=0)

        if get1 != password:
            global label2
            label2 = Label(root, text='Sorry, password is incorrect.')
            label2.grid(row=0, column=0)

        if get1 == password:
            Event(label2.grid_forget())

        if get1 != password:
            Event(label.grid_forget())

        file.close()

    def signinbutton(self):
        button = Button(root, text='Sign In', command=self.signin)
        button.grid(row=2, column=0)

    def signup(self):
        file = open('output.txt', 'w')
        get1 = enter2.get()
        file.write(get1)
        file.close()
    def signupbutton(self):
        button = Button(root, text='Sign Up', command=self.signup)
        button.grid(row=2, column=1)

    def run(self):
        self.entry()
        self.signinbutton()
        self.signupbutton()
        self.quitbutton()

        root.mainloop()

app = App()
app.run()