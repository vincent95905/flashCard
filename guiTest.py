import tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = StartPage(container, self)
        self.frames[StartPage] = frame
        frame.grid(row=0, column=0, rowspan=12, columnspan=6, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()



class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        Btn = tk.Button(self, text="Sign In", command=self.qf).pack()

    def qf(self):
        print("coucou")


app = App()
app.mainloop()
