import tkinter as tk
from tkinter import font  as tkfont
from tkinter import PhotoImage
import data
from methods import Methods, Unit



class SampleApp(tk.Tk):

    photo = "ESP_logo.png"

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.button_font = tkfont.Font(family='Helvetica', size=12, weight="bold", slant="italic")

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

        #display label
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Pressure", font=controller.title_font)
        label.grid(row = 0, column = 0)

        #instantiating a Methods class
        calculator = Methods()

        #create a list to hold frames for clearing
        units_array = list()

        #initialize objects and conversion rates
        psi = Unit()
        mpa = Unit()
        torr = Unit()

        #grab conversion rates from data file
        psi.conversion_rate = data.psi_to_psi
        mpa.conversion_rate= data.mpa_to_psi
        torr.conversion_rate= data.torr_to_psi


        #add the psi entry and unit
        psi.frame = tk.Entry(self)
        psi.frame.grid(row=1, column = 0)
        frame1 = tk.Label(self, text="psi", font=controller.button_font)
        frame1.grid(row=1, column = 1)
        units_array.append(psi)

        #add the mpa entry and unit
        mpa.frame = tk.Entry(self)
        mpa.frame.grid(row=2, column = 0)
        frame2 = tk.Label(self, text = 'MPa', font=controller.button_font)
        frame2.grid(row=2, column = 1)
        units_array.append(mpa)

        #add the torr entry and unit
        torr.frame = tk.Entry(self)
        torr.frame.grid(row=3, column = 0)
        frame2 = tk.Label(self, text = 'Torr', font=controller.button_font)
        frame2.grid(row=3, column = 1)
        units_array.append(torr)

        #add the "clear all" button
        clear = tk.Button(self, text="Clear", font = controller.button_font, command=lambda: calculator.clear_all(units_array))
        clear.grid(row=5, column = 0)

        #add the calculate button
        calc_button = tk.Button(self, text = "Calculate", font = controller.button_font,
                                command = lambda: calculator.reader(units_array))
        calc_button.grid(row=4, column = 0)

        #add the "back to main menu button"
        exit = tk.Button(self, text="Go to the main menu", font = controller.title_font, 
                         command=lambda: controller.show_frame("StartPage"))
        exit.grid(row=6)





 



class SpeedPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Speed", font=controller.title_font)
        label.grid()
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid()

        #inititalize list of variables
        units_array = list()

        #initialize objects and conversion rates
        ft_s = Unit()
        m_s = Unit()
        inch = Unit()
        mm = Unit()
        rpm  = Unit()
        rps = Unit()

        #grab conversion rates from data file]
        rps.conversion_rate = data.rps_to_rpm
        rpm.conversion_rate = 1 #RPM is master rotational speed unit
        mm.conversion_rate = data.mm_to_inch
        inch.conversion_rate = 1 #Inch is master diameter unit
        ft_s.conversion_rate = data.fs_to_ms
        m_s.conversion_rate = 1 #m/s is master velocity unit

        #add a "Rotational speed header"
        frame1 = tk.Label(self, text="Rotational Speed", font=controller.title_font)
        frame1.grid()

        #add the RPM entry and unit
        rpm.frame = tk.Entry(self)
        rpm.frame.grid()
        frame1 = tk.Label(self, text="Rev/m (RPM)", font=controller.button_font)
        frame1.grid()
        units_array.append(rpm)

        #add the RPS entry and unit
        rps.frame = tk.Entry(self)
        rps.frame.grid()
        frame1 = tk.Label(self, text="Rev/s (RPS)", font=controller.button_font)
        frame1.grid()
        units_array.append(rps)

        #add a "Diameter header"
        frame1 = tk.Label(self, text="Shaft Diameter", font=controller.title_font)
        frame1.grid()

        #add the inches diameter entry and unit
        inch.frame = tk.Entry(self)
        inch.frame.grid()
        frame1 = tk.Label(self, text="Inch (in)", font=controller.button_font)
        frame1.grid()
        units_array.append(inch)

        #add the mm diameter entry and unit
        mm.frame = tk.Entry(self)
        mm.frame.grid()
        frame1 = tk.Label(self, text="millimeter (mm)", font=controller.button_font)
        frame1.grid()
        units_array.append(mm)

        #add a "Surface Velocity header"
        frame1 = tk.Label(self, text="Surface Velocity", font=controller.title_font)
        frame1.grid()

        #add the ft/s speed entry and unit
        ft_s.frame = tk.Entry(self)
        ft_s.frame.grid()
        frame1 = tk.Label(self, text="feet per second (ft/s)", font=controller.button_font)
        frame1.grid()
        units_array.append(ft_s)

        #add the m/s diameter entry and unit
        m_s.frame = tk.Entry(self)
        m_s.frame.grid()
        frame1 = tk.Label(self, text="meters per second (m/s)", font=controller.button_font)
        frame1.grid()
        units_array.append(m_s)

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
        label = tk.Label(self, text="Length Conversion Tool", font=controller.title_font)
        label.grid(row = 0, column = 0, columnspan = 4)
        label.grid_columnconfigure(1, weight = 1)

        #instantiating a Methods class
        calculator = Methods()

        #create a list to hold frames for clearing
        units_array = list()

        #initialize objects and conversion rates
        meter = Unit()
        cm = Unit()
        mm = Unit()
        thou = Unit()
        inch = Unit()
        mile = Unit()

        #grab conversion rates from data file
        meter.conversion_rate = data.m_to_m
        cm.conversion_rate= data.cm_to_m
        mm.conversion_rate= data.mm_to_m
        thou.conversion_rate= data.thou_to_m
        inch.conversion_rate= data.inch_to_m
        mile.conversion_rate= data.mile_to_m

        #add the meter entry and unit
        meter.frame = tk.Entry(self)
        meter.frame.grid(row=1, column = 1, sticky = tk.E)
        frame1 = tk.Label(self, text="meter", font=controller.button_font)
        frame1.grid(row=1, column = 2, sticky = tk.W)
        units_array.append(meter)

        #add the centimeter entry and unit
        cm.frame = tk.Entry(self)
        cm.frame.grid(row=2, column = 1, sticky = tk.E)
        frame1 = tk.Label(self, text="cm", font=controller.button_font)
        frame1.grid(row=2, column = 2, sticky = tk.W)
        units_array.append(cm)

        #add the millimeter entry and unit
        mm.frame = tk.Entry(self)
        mm.frame.grid(row=3, column = 1, sticky = tk.E)
        frame1 = tk.Label(self, text="mm", font=controller.button_font)
        frame1.grid(row=3, column = 2, sticky = tk.W)
        units_array.append(mm)

        #add the thousandth entry and unit
        thou.frame = tk.Entry(self)
        thou.frame.grid(row=4, column = 1, sticky = tk.E)
        frame1 = tk.Label(self, text="thousandths of an inch", font=controller.button_font)
        frame1.grid(row=4, column = 2, sticky = tk.W)
        units_array.append(thou)

        #add the inch entry and unit
        inch.frame = tk.Entry(self)
        inch.frame.grid(row=5, column = 1, sticky = tk.E)
        frame1 = tk.Label(self, text="inch", font=controller.button_font)
        frame1.grid(row=5, column = 2, sticky = tk.W)
        units_array.append(inch)
        
        #add the mile entry and unit
        mile.frame = tk.Entry(self)
        mile.frame.grid(row=6, column = 1, sticky = tk.E)
        frame1 = tk.Label(self, text="mile", font=controller.button_font)
        frame1.grid(row=6, column = 2, sticky = tk.W)
        units_array.append(mile)

        #add the calculate button
        calc_button = tk.Button(self, text = "Calculate", font = controller.button_font,
                                command = lambda: calculator.reader(units_array))
        calc_button.grid(row=8, column = 1, padx=2)

        #add the "clear all" button
        clear = tk.Button(self, text="Clear", font = controller.button_font, command=lambda: calculator.clear_all(units_array))
        clear.grid(row=9, column = 1)

        #add the "back to main menu button"
        exit = tk.Button(self, text="Go to the main menu", font = controller.title_font,
                         command=lambda: controller.show_frame("StartPage"))
        exit.grid(row=10, column =1)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
