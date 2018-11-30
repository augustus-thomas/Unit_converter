from decimal import *
from math import pi
import requests
import json
import urllib

class Unit:
    value = 0
    conversion_rate = 0.05
    frame = 0

    def convert(self, rate):
        value = value * conversion_rate


class Methods:

   #Reads the entry, performs conversion, places result in output box (move to methods?)
    def reader(self, units_list, exit_val):

        #Grab master.value if it is available
        if units_list[0].frame.index("end") != 0:
            master_val = float(units_list[0].frame.get())
            units_list[0].value = master_val

            #set precision to length of entry string
            context = Context(prec = self.find_sigfigs(units_list[0].frame.get()), rounding = ROUND_UP)
            setcontext(context)

        #Search for what they did enter and get psi.value
        if units_list[0].frame.index("end") == 0:
            #cycle through entries looking for which was entered
            for objects in units_list:
                #Only read non-empty tk.entry objects
                if objects.frame.index("end") != 0:
                    #grab the entered value and set its objects.value to that (avoids rounding later on)
                    master_val = float(objects.frame.get())
                    objects.value = master_val
                    #set precision to the number of sigfigs entered
                    context = Context(prec = self.find_sigfigs(objects.frame.get()), rounding = ROUND_UP)
                    setcontext(context)
                    #caluclate psi from whatever was entered
                    units_list[0].value = Decimal(Decimal(master_val)*objects.conversion_rate)
                    break    
        #calculate all other unit values from psi.value
        for objects in units_list:
            try:
                #do not edit the user-entered value
                if objects.value == master_val:
                    continue
                objects.value = Decimal(units_list[0].value)/Decimal(objects.conversion_rate)
            except Exception:
                return
        #use an exit value if this is a stage 1 calculation, not a terminal calculation
        if(exit_val == 1):
            return

        #print converted values to respective boxes
        for objects in units_list:
            #do not edit the user-entered value
            if objects.value == master_val:
                continue
            #clear the box to avoid appending an existing value
            objects.frame.delete(0,'end')
            #insert the Unit().value into the Unit().entry-box
            objects.frame.insert(0, objects.value)

    #Specialized read funcitonality for the velocity caluclator
    def speed_read(self, units_list, rates_list, diameters_list, velocity_list):
        #find available info without filling any boxes
        self.reader(rates_list, 0)
        self.reader(diameters_list, 0)
        self.reader(velocity_list, 0)

        #do math using the master values
        self.speed_math(rates_list[0], diameters_list[0], velocity_list[0])
        #put the velocity_list[0].value in the box so reader() can parse
        velocity_list[0].frame.delete(0,'end') #Delete anything in there
        velocity_list[0].frame.insert(0, velocity_list[0].value) #input the value
        #convert the velocity list in case they weren't entered
        self.reader(velocity_list, 0)

    #Specialized processing for the speed_read function
    #Only calculated TOWARDS velocity, not reverse
    def speed_math(self, rate_ob, diam_ob, speed_ob):
        #set precision to the number of sigfigs entered
        context = Context(prec = self.find_sigfigs(str(rate_ob.value)), rounding = ROUND_UP)
        setcontext(context)
        #master values conversion rate is constant: 
        speed_ob.value = (Decimal(rate_ob.value) *Decimal(pi) * Decimal(diam_ob.value))/60000
        #put the calculated value in m/s so that reader() can parse
        #clear the box to avoid appending an existing value
        speed_ob.frame.delete(0,'end')
        #insert the Unit().value into the Unit().entry-box
        speed_ob.frame.insert(0, speed_ob.value)

    #Returns the number of sig figs found in a number
    def find_sigfigs(self, num):
        #if sci-notation is used, drop to lowercase
        num = num.lower()
        if ('e' in num):
            #in sci-notation, the sig figs appear on the left of the e
            myStr = num.split('e')
            return len( myStr[0] ) - 1 # to compenstate for the decimal point
        else:
            #make a copy of the string with added sig figs in e notation, then strip the e.
            n = ('%.*e' %(8, float(num))).split('e')
            if '.' in num:
                #create a copy with no decimals
                s = num.replace('.','')
                #number of zeros to add back in
                l = len(s) - len(s.rstrip('0'))
                #take all zeros off the copy.
                #Add on all the zeros supposed to be there?
                n[0] = n[0].rstrip('0') + ''.join(['0' for num in range(l)])
            else:
                #the user had no trailing zeros so just strip them all
                n[0] = n[0].rstrip('0')
            #pass back to the beginning to parse - we want at least 4 sig figs
        return max(self.find_sigfigs('e'.join(n)), 4)

    #Clears all boxes using for loop
    def clear_all(self, units_list):
        for frames in units_list:
            frames.frame.delete(0, 'end')
 
    def currency_getrates(self, currencies):
        # "convert" endpoint - convert any amount from one currency to another
        # using real-time exchange rates

      
        r = requests.get('http://data.fixer.io/api/rates'
        + '?access_key=cc827772c076885116ef450ca0df6a16')
        
        for objects in currencies
            #Only read non-empty tk.entry objects
            if objects.frame.index("end") != 0:
                #grab the entered value and set its objects.value to that (avoids rounding later on)
                master_val = float(objects.frame.get())
                objects.value = master_val
                #set precision to the number of sigfigs entered
                context = Context(prec = self.find_sigfigs(objects.frame.get()), rounding = ROUND_UP)
                setcontext(context)
       # http://data.fixer.io/api/convert
       # ? access_key = API_KEY
       # & from = GBP
       # & to = JPY
        #& amount = 25
        
        return

        #? access_key = YOUR_ACCESS_KEY
        # & from = USD
        #& to = EUR
        #& amount = 25