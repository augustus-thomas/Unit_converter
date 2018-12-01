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

      
        #r = requests.get('http://data.fixer.io/api/rates'
        #+ '?access_key=cc827772c076885116ef450ca0df6a16')
        
        # EUR * API_val = dest_curr
        r = {"success":True,"timestamp":1543611249,"base":"EUR","date":"2018-11-30","rates":{"AED":4.156758,"AFN":85.722462,"ALL":124.175712,"AMD":549.107895,"ANG":2.009238,"AOA":351.327257,"ARS":42.697485,"AUD":1.548938,"AWG":2.038656,"AZN":1.926628,"BAM":1.946884,"BBD":2.265833,"BDT":94.851021,"BGN":1.956503,"BHD":0.426596,"BIF":2055.064832,"BMD":1.131644,"BND":1.78351,"BOB":7.822317,"BRL":4.375897,"BSD":1.13204,"BTC":0.000284,"BTN":78.896487,"BWP":11.916658,"BYN":2.412443,"BYR":22180.215149,"BZD":2.281851,"CAD":1.504945,"CDF":1821.946654,"CHF":1.131196,"CLF":0.028345,"CLP":760.016289,"CNY":7.875154,"COP":3664.092328,"CRC":677.2831,"CUC":1.131644,"CUP":29.988556,"CVE":109.96125,"CZK":25.984014,"DJF":201.116151,"DKK":7.463337,"DOP":56.633151,"DZD":134.490233,"EGP":20.259862,"ERN":16.97506,"ETB":31.810946,"EUR":1,"FJD":2.386128,"FKP":0.882581,"GBP":0.887892,"GEL":3.027192,"GGP":0.887917,"GHS":5.621897,"GIP":0.882581,"GMD":56.010747,"GNF":10388.488926,"GTQ":8.713826,"GYD":236.655019,"HKD":8.854987,"HNL":27.595175,"HRK":7.389577,"HTG":83.438919,"HUF":323.707099,"IDR":16245.479878,"ILS":4.220017,"IMP":0.887917,"INR":78.915214,"IQD":1347.787563,"IRR":47647.855443,"ISK":139.396299,"JEP":0.887917,"JMD":143.42495,"JOD":0.803019,"JPY":128.485125,"KES":116.05049,"KGS":79.045743,"KHR":4571.840662,"KMF":489.213837,"KPW":1018.51195,"KRW":1267.441262,"KWD":0.344269,"KYD":0.943316,"KZT":422.680645,"LAK":9669.895214,"LBP":1709.857376,"LKR":202.394896,"LRD":178.917129,"LSL":15.458684,"LTL":3.34145,"LVL":0.68452,"LYD":1.578687,"MAD":10.781739,"MDL":19.403206,"MGA":4096.550333,"MKD":61.718756,"MMK":1790.883056,"MNT":2955.902457,"MOP":9.121331,"MRO":403.997167,"MUR":39.033828,"MVR":17.484322,"MWK":822.993532,"MXN":23.054754,"MYR":4.730162,"MZN":69.432039,"NAD":15.458679,"NGN":411.918671,"NIO":36.643047,"NOK":9.732706,"NPR":126.093435,"NZD":1.646723,"OMR":0.435722,"PAB":1.13204,"PEN":3.828921,"PGK":3.680275,"PHP":59.366449,"PKR":158.660628,"PLN":4.291929,"PYG":6727.399238,"QAR":4.120358,"RON":4.655813,"RSD":118.2006,"RUB":75.834952,"RWF":990.188176,"SAR":4.245818,"SBD":9.258886,"SCR":15.434531,"SDG":53.895703,"SEK":10.306988,"SGD":1.552733,"SHP":1.494792,"SLL":9449.224694,"SOS":657.485332,"SRD":8.439841,"STD":23821.776958,"SVC":9.904994,"SYP":582.796852,"SZL":15.45867,"THB":37.288076,"TJS":10.663422,"TMT":3.960753,"TND":3.306833,"TOP":2.546255,"TRY":5.912616,"TTD":7.629712,"TWD":34.906118,"TZS":2603.010792,"UAH":31.90145,"UGX":4213.679165,"USD":1.131644,"UYU":36.676985,"UZS":9385.852646,"VEF":281290.111344,"VND":26396.040329,"VUV":127.42595,"WST":2.928417,"XAF":653.004054,"XAG":0.079814,"XAU":0.000926,"XCD":3.058324,"XDR":0.819554,"XOF":658.616969,"XPF":119.105904,"YER":283.307395,"ZAR":15.693299,"ZMK":10186.154709,"ZMW":13.61032,"ZWL":364.790995}}

        #make sure the .get worked
        if r[0] != "success":True:
            self.clear_all(currencies)
            for objects in currencies:
                objects.frame.insert(0, 'Failure: No response from host')
            return

        #read the API output and set conversion rates from EUR
        for object in currencies:
            for unit in r:
                if unit[0] == object.name:
                    print ('well you got this far')
                # object.conversion_rate = 

        for objects in currencies:
            #Only read non-empty tk.entry objects
            if objects.frame.index("end") != 0:
                #grab the entered value and set its objects.value to that (avoids rounding later on)
                master_val = float(objects.frame.get())
                objects.value = master_val
                #set precision to the number of sigfigs entered
                context = Context(prec = self.find_sigfigs(objects.frame.get()), rounding = ROUND_UP)
                setcontext(context)

        #now the entry is in the .value of some object... must convert

       
        return

    def currency_convert(self, currencies):

        

        return