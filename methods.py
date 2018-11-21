import decimal

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

        #cycle through entries looking for a non-zero value. Save that value and location
        for objects in units_list:
            #Only read non-empty tk.entry objects
            if objects.frame.index("end") != 0:
                master_val = float(objects.frame.get())
                objects.value = master_val
                break

        for objects in units_list:
            if objects.value == master_val:
                continue
                #if this is the input, skip the loop step

            #Round the conversion to the current sig-figs
            decimal.Decimal.localcontext.prec()=len(str(abs(master_val)))
            #hard-coded a .05 conversion rate for test
            objects.value = decimal.Decimal(master_val*objects.conversion_rate)
            #clear the box to avoid appending an existing value
            objects.frame.delete(0,'end')
            #insert the value into the entry box
            objects.frame.insert(0, objects.value)

    #Clears all boxes using for loop (move to methods?)
    def clear_all(self, units_list):
        for frames in units_list:
            frames.frame.delete(0, 'end')