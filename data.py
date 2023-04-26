#This file is for storing static conversion rates and possibly APIs if I go the currency route
from decimal import *
import os
from dotenv import load_dotenv

#Fetch CURRENCY_API_KEY stored in secret ./env/.env that is ignored
load_dotenv()
CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY')

#set precision to length of entry string
context = Context(prec = 10)
setcontext(context)


#pressure units
psi_to_psi = Decimal('1') #master converter psi/psi
mpa_to_psi = Decimal('145.038') #mpa/psi
torr_to_psi = Decimal('0.0193368') #torr/psi

#length units
m_to_m = Decimal('1') #master converter meter/meter
cm_to_m = Decimal('0.01') #m/cm
mm_to_m = Decimal('0.001') #m/mm
thou_to_m = Decimal('0.0000254') #m/thou
inch_to_m = Decimal('0.0254') #m/inch
mile_to_m = Decimal('1609.34') #m/mile

#speed units
rps_to_rpm = Decimal(60) #1 rps = 1/60 rpm
mm_to_inch = Decimal('0.0393701') #1 mm = 0.0393701 inches
fs_to_ms = Decimal('0.3048') #1 ft/s = 0.3048 m/s
