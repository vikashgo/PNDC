import sys 
import subprocess 
from os import system 
system ('pip install --upgrade pip')

# module installation 
def install(package):

    subprocess.run([
        sys.executable, "-m", "pip", "-q", "install", package
    ])
    
install("phonenumbers")

import phonenumbers 

from phonenumbers import geocoder as GC
from phonenumbers import carrier as CR
from phonenumbers import timezone as TZ

def PHONE_NO_DETAILS() :

    number = input("Enter  Number With country code :")
    
    phone_no = phonenumbers.parse(number)
    
    DETAILS_1 = GC.description_for_number(phone_no , "en")
    
    DETAILS_2 = CR.name_for_number(phone_no , "en")
    
    DETAILS_3 = TZ.time_zones_for_number(phone_no)
    
    # Number Details 
    print (DETAILS_1)
    
    # Number Informatiom 
    print (DETAILS_2)
    
    # Number Time Zone 
    print (DETAILS_3)
    
#PHONE_NO_DETAILS()
    

if __name__ == "__main__" :
    PHONE_NO_DETAILS()
