class Unit:
    value = 0
    conversion_rate = 0.05
    name = "name"
    frame = 0

    def convert(self, rate):
        value = value * conversion_rate


class Methods:

   #Reads the entry, performs conversion, places result in output box (move to methods?)
    def reader(self, units_list):

        #Grab psi.value if it is available
        if units_list[0].frame.index("end") != 0:
            master_val = float(units_list[0].frame.get())
            units_list[0].value = master_val

        #Search for what they did enter and get psi.value
        if units_list[0].frame.index("end") == 0:
            #cycle through entries looking for which was entered
            for objects in units_list:
                #Only read non-empty tk.entry objects
                if objects.frame.index("end") != 0:
                    master_val = float(objects.frame.get())
                    #caluclate psi from whatever was entered
                    units_list[0].value = master_val*objects.conversion_rate
                    break  
                    
        #calculate all other unit values from psi.value
        for objects in units_list:
            #do not edit the user-entered value
            if objects.value == master_val:
                continue
            objects.value = round(units_list[0].value/objects.conversion_rate, len(str(abs(master_val)))-2 )

        #print converted values to respective boxes
        for objects in units_list:
            #do not edit the user-entered value
            if objects.value == master_val:
                continue
            #clear the box to avoid appending an existing value
            objects.frame.delete(0,'end')
            #insert the Unit().value into the Unit().entry-box
            objects.frame.insert(0, objects.value)


    #Clears all boxes using for loop (move to methods?)
    def clear_all(self, units_list):
        for frames in units_list:
            frames.frame.delete(0, 'end')