import tkinter as tk
from tkinter import font  as tkfont
from tkinter import PhotoImage
import data
from methods import Methods, Unit



class ESP_Calculator_app(tk.Tk):

    photo = "ESP_logo.png"

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.button_font = tkfont.Font(family='Helvetica', size=12, weight="bold", slant="italic")
        self.unit_font = tkfont.Font(family='Helvetica', size=9, weight="bold", slant="italic") #need to put this in

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
 
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
                                command = lambda: calculator.reader(units_array, 0))
        calc_button.grid(row=4, column = 0)

        #add the "back to main menu button"
        exit = tk.Button(self, text="Go to the main menu", font = controller.title_font, 
                         command=lambda: controller.show_frame("StartPage"))
        exit.grid(row=6)

class SpeedPage(tk.Frame):

    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        self.controller = controller

        #GUI Frames
        title_bl = tk.Frame(self)
        title_bl.grid(row = 0, column = 0, columnspan = 3, pady=15)
        left_bl = tk.Frame(self)
        left_bl.grid(row = 1, column = 0, padx=30, pady=40)
        right_bl = tk.Frame(self)
        right_bl.grid(row = 1, column = 1)
        results_bl = tk.Frame(self)
        results_bl.grid(row = 2, columnspan = 3, pady=15)
        buttons_bl = tk.Frame(self)
        buttons_bl.grid(row = 4, columnspan = 4)
        #add an extra frame for main buttons
        top_buttons_bl = tk.Frame(buttons_bl)
        top_buttons_bl.grid (row = 0, columnspan = 3, pady=10)

        label = tk.Label(title_bl, text="Shaft Speed Calculator", font=controller.title_font)
        label.grid(row = 0, sticky = 'nsew')



        #instantiating a Methods class
        calculator = Methods()

        #inititalize list of variables
        units_list = list() #holds all objects for clearing purposes
        rates_list = list()
        diameters_list = list()
        velocity_list = list()

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
        mm.conversion_rate = 1 #mm is master diameter unit
        inch.conversion_rate = (data.inch_to_m)*1000
        ft_s.conversion_rate = data.fs_to_ms
        m_s.conversion_rate = 1 #m/s is master velocity unit

        #add a "Rotational speed header"
        rot_header = tk.Label(left_bl, text="Rotational Speed", font=controller.title_font)
        rot_header.grid(row = 0, column =0, columnspan = 3, sticky = 'nsew')

        #add the RPM entry and unit
        rpm.frame = tk.Entry(left_bl)
        rpm.frame.grid(row = 1, column = 0)
        rpm_label = tk.Label(left_bl, text="Rev/m (RPM)", font=controller.button_font)
        rpm_label.grid(row = 1, column = 1, sticky = 'w')
        rates_list.append(rpm) #adds at master [0] spot
        units_list.append(rpm)

        #add the RPS entry and unit
        rps.frame = tk.Entry(left_bl)
        rps.frame.grid(row = 2, column = 0)
        rps_label = tk.Label(left_bl, text="Rev/s (RPS)", font=controller.button_font)
        rps_label.grid(row = 2, column = 1, sticky = 'w')
        rates_list.append(rps) #adds to [>0] slave spot
        units_list.append(rps)

        #add a "Diameter header"
        diam_header = tk.Label(right_bl, text="Shaft Diameter", font=controller.title_font)
        diam_header.grid(row = 0, column = 0, columnspan = 3, sticky = 'nsew')

        #add the mm diameter entry and unit
        mm.frame = tk.Entry(right_bl)
        mm.frame.grid(row =1, column = 0)
        mm_label = tk.Label(right_bl, text="millimeter (mm)", font=controller.button_font)
        mm_label.grid(row = 1, column = 1)
        diameters_list.append(mm) #adds to [0] master spot
        units_list.append(mm)

        #add the inches diameter entry and unit
        inch.frame = tk.Entry(right_bl)
        inch.frame.grid(row = 2, column = 0)
        inch_label = tk.Label(right_bl, text="Inch (in)", font=controller.button_font)
        inch_label.grid(row = 2, column = 1)
        diameters_list.append(inch) #adds to slave [>0] spot
        units_list.append(inch)

        #add a "Surface Velocity header"
        velocity_header = tk.Label(results_bl, text="Surface Velocity", font=controller.title_font)
        velocity_header.grid(row = 0, column = 0, columnspan = 3, sticky = 'nsew')

        #add the m/s diameter entry and unit
        m_s.frame = tk.Entry(results_bl)
        m_s.frame.grid(row = 1, column = 0)
        m_s_label = tk.Label(results_bl, text="meters per second (m/s)", font=controller.button_font)
        m_s_label.grid(row = 1, column = 1)
        velocity_list.append(m_s) #adds to master [0] spot
        units_list.append(m_s)

        #add the ft/s speed entry and unit
        ft_s.frame = tk.Entry(results_bl)
        ft_s.frame.grid(row = 2, column = 0)
        ft_s_label = tk.Label(results_bl, text="feet per second (ft/s)", font=controller.button_font)
        ft_s_label.grid(row = 2, column = 1) 
        velocity_list.append(ft_s) #adds to [>0] slave spot
        units_list.append(ft_s)

        #add the calculate button
        calc_button = tk.Button(top_buttons_bl, text = "Calculate", font = controller.button_font,
                                command = lambda: calculator.speed_read(units_list, rates_list, diameters_list, velocity_list))
        calc_button.grid(row = 0, column = 0, columnspan = 2, sticky = 'w', padx=5)

        #add the "clear all" button
        clear = tk.Button(top_buttons_bl, text="Clear", font = controller.button_font, command=lambda: calculator.clear_all(units_list))
        clear.grid(row = 0, column = 2, columnspan = 2, sticky = 'e')

        #return to home page
        button = tk.Button(buttons_bl, font = controller.title_font, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row = 1, column = 0, sticky = 'nsew')

class CurrencyPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is Currency", font=controller.title_font)
        label.grid()


        #make a list to hold currencies active
        active_currencies = list()

        #make a methods object for access to functions
        converter = Methods()

        #make currency units
        
        eur = Unit() #EURO is the master currency
        usd = Unit() #USD
        rmb = Unit() #Chinese Renminbi (yuan)

        eur.frame = tk.Entry(self)
        eur.frame.grid(row=1, column = 0)
        frame1 = tk.Label(self, text="EUR", font=controller.button_font)
        frame1.grid(row=2, column = 1)
        active_currencies.append(eur) #EUR is location zero and master

        usd.frame = tk.Entry(self)
        usd.frame.grid(row=2, column = 0)
        frame1 = tk.Label(self, text="USD", font=controller.button_font)
        frame1.grid(row=3, column = 1)
        active_currencies.append(usd)

        rmb.frame = tk.Entry(self)
        rmb.frame.grid(row=3, column = 0)
        frame1 = tk.Label(self, text="RMB", font=controller.button_font)
        frame1.grid(row=4, column = 1)
        active_currencies.append(rmb)

        usd.name = 'USD'
        eur.name = 'EUR'
        rmb.name = 'RMB'



        button1 = tk.Button(self, text="testcurr",
                            command=lambda: converter.currency_getrates(active_currencies),height=4, width = 20, pady=5)
        button1.grid()

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid()

class LengthPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        title_frame = tk.Frame(self)
        title_frame.grid(columnspan = 3)

        label = tk.Label(title_frame, text="Length Conversion Tool", font=controller.title_font)
        label.grid(row = 0, pady=15, column = 1)
        #Frame for the units
        units_frame = tk.Frame(title_frame)
        units_frame.grid(row=1, column = 1)
        #Frame to central justify buttons
        len_button_blk = tk.Frame(title_frame)
        len_button_blk.grid(row = 2, column = 1)

        #instantiating a Methods class
        calculator = Methods()

        #create a list to hold frames for clearing
        units_array = list()

        #initialize objects and conversion rates
        meter = Unit()
        mm = Unit()
        inch = Unit()
        cm = Unit()
        thou = Unit()
        mile = Unit()

        #grab conversion rates from data file
        meter.conversion_rate = data.m_to_m
        inch.conversion_rate= data.inch_to_m
        mm.conversion_rate= data.mm_to_m
        cm.conversion_rate= data.cm_to_m
        thou.conversion_rate= data.thou_to_m
        mile.conversion_rate= data.mile_to_m

        #add the meter entry and unit
        meter.frame = tk.Entry(units_frame)
        meter.frame.grid(row=0, columnspan = 2)
        frame1 = tk.Label(units_frame, text="meter", font=controller.button_font)
        frame1.grid(row=0, column = 2)
        units_array.append(meter)

        #add the inch entry and unit
        inch.frame = tk.Entry(units_frame)
        inch.frame.grid(row=1, columnspan = 2)
        frame1 = tk.Label(units_frame, text="inch", font=controller.button_font)
        frame1.grid(row=1, column = 2)
        units_array.append(inch)

        #add the millimeter entry and unit
        mm.frame = tk.Entry(units_frame)
        mm.frame.grid(row=2, columnspan = 2)
        frame1 = tk.Label(units_frame, text="mm", font=controller.button_font)
        frame1.grid(row=2, column = 2)
        units_array.append(mm)

        #add the centimeter entry and unit
        cm.frame = tk.Entry(units_frame)
        cm.frame.grid(row=3, columnspan = 2)
        frame1 = tk.Label(units_frame, text="cm", font=controller.button_font)
        frame1.grid(row=3, column = 2)
        units_array.append(cm)

        #add the thousandth entry and unit
        thou.frame = tk.Entry(units_frame)
        thou.frame.grid(row=4, columnspan = 2)
        frame1 = tk.Label(units_frame, text="thou", font=controller.button_font)
        frame1.grid(row=4, column = 2)
        units_array.append(thou)
        
        #add the mile entry and unit
        mile.frame = tk.Entry(units_frame)
        mile.frame.grid(row=5, columnspan = 2)
        frame1 = tk.Label(units_frame, text="mile", font=controller.button_font)
        frame1.grid(row=5, column = 2)
        units_array.append(mile)

        #add the calculate button
        calc_button = tk.Button(len_button_blk, text = "Calculate", font = controller.button_font,
                                command = lambda: calculator.reader(units_array, 0))
        calc_button.grid(row=0)

        #add the "clear all" button
        clear = tk.Button(len_button_blk, text="Clear", font = controller.button_font, command=lambda: calculator.clear_all(units_array))
        clear.grid(row = 0, column = 1)

        #add the "back to main menu button"
        exit = tk.Button(len_button_blk, text="Go to the main menu", font = controller.title_font,
                         command=lambda: controller.show_frame("StartPage"))
        exit.grid(row=1, column = 0, columnspan = 2)

if __name__ == "__main__":
    app = ESP_Calculator_app()
    app.mainloop()
