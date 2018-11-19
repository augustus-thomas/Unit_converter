from tkinter import *

#calling the tkinter window "master"
master = Tk()

path = "ESP_logo.png"

#creates an image
img = PhotoImage(file=path)

#attaches the image to a label to be inserted into the grid
label1 = Label(image = img)

#place selector buttons & image, and pad attractively
Button(master, text='Pressure', command=master.quit).grid(row=0, column=0, pady=10, padx = 10)
Button(master, text='Speed', command=master.quit).grid(row=0, column=1, pady=4, padx=10)
Button(master, text='Currency', command=master.quit).grid(row=2, column=0, pady=4, padx=10)
Button(master, text='Length', command=master.quit).grid(row=2, column=1, pady=4, padx=10)
label1.grid(row = 0, column = 3, columnspan = 5, rowspan = 3, sticky=W+E+S+N, padx=5, pady=5)

mainloop( )