import tkinter as tk
from tkinter import font  as tkfont
from tkinter import PhotoImage



class SampleApp(tk.Tk):

    photo = "ESP_logo.png"

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

 
        self.frames = {}
        for F in (StartPage, PressurePage, SpeedPage, CurrencyPage, LengthPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()




class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="ESP International - Engineering Unit Converter", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10, padx=10)

        logoPath = PhotoImage(file="ESP_logo.png")
        logo = tk.Label(self, image=logoPath)
        logo.photo = logoPath
        logo.pack(pady=10)

        button1 = tk.Button(self, text="Go to Pressure",
                            command=lambda: controller.show_frame("PressurePage"),height=4, width = 20, pady=5)
        button2 = tk.Button(self, text="Go to Speed",
                            command=lambda: controller.show_frame("SpeedPage"),height=4, width = 20, pady=5)
        button3 = tk.Button(self, text="Go to Currency",
                            command=lambda: controller.show_frame("CurrencyPage"),height=4, width = 20, pady=5)
        button4 = tk.Button(self, text="Go to Length",
                            command=lambda: controller.show_frame("LengthPage"),height=4, width = 20, pady=5)
        button1.pack()
        button2.pack()
        button3.pack()
        button4.pack()


class PressurePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Pressure", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class SpeedPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Speed", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class CurrencyPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Currency", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class LengthPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Length", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()



if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
