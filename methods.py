class Unit:
    value = 0
    conversion_rate = 0.05
    name = "name"
    frame = 0

    def convert(self, rate):
        value = value * conversion_rate


class Methods:
    in_val = 0
    c_rate = 0
    out_val = 0

    #Simply applies the appropriate conversion rate
   #Reads the entry, performs conversion, places result in output box (move to methods?)
    def reader(self, units_list):
        i=0
        #cycle through entries looking for a non-zero value. Save that value and location
        for objects in units_list:
            if objects.frame.index("end") != 0:
                master_val = float(objects.frame.get())
                objects.value = master_val
                print(master_val)
                master_location = i
                break
            i+=1 

        for objects in units_list:
            if objects.value == master_val:
                continue
                #if this is the input, skip the loop step

            #hard-coded a .05 conversion rate for test
            objects.value = float(master_val)*objects.conversion_rate
            #clear the box before appending the value
            objects.frame.delete(0,'end')
            #Round the value and insert into the box
            objects.frame.insert(0, round(objects.value))
