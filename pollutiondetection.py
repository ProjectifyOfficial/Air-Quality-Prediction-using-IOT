from __future__ import print_function
import geocoder
from oauth2client.client import SignedJwtAssertionCredentials
from httplib2 import Http
import RPi.GPIO as GPIO
import time
import sys
import urllib2
import urllib
import json
import gspread

#from geopy.geocoders import Nominatim

i=2
a=26
GPIO.setmode(GPIO.BCM)
GPIO.setup(a,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
json_key = json.load(open('/home/pi/Desktop/Airpollution/crede.json'),strict=False) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds
file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("Airpollution").sheet1 # open sheet
all_cells = sheet.range('A1:C6')
#print all_cells

def doTransaction(address,lat,lon):
    apikey = 'nDWWt64tr8w-3WkA4ckTe5ZBTLU8mefwsapua9njpy'
    sender = 'TXTLCL'
    message = 'Pollution has been detected at \nlatitude: '+str(lat)+', longitude:'+str(lon)+"\n The predicted location identified is"+address  

    data = urllib.urlencode({'apikey':apikey,
                             'numbers':"<Enter your phone number",
                             'sender':sender,
                             'message':message})
    data = data.encode('utf-8')
    request = urllib2.Request("https://api.textlocal.in/send/?",data)
    fr = urllib2.urlopen(request).read()
    fr = json.loads(fr)
    print('Message sent status: ',fr["status"])
    

def action(pin):
      global i
      print('going')
      urllib2.urlopen('https://api.thingspeak.com/update?api_key=P3QN3VX5DFS2UYEU&field1=1')
      time.sleep(1)
      print('gas detected')
      g = geocoder.ip('me')
      sheet.update_cell(i,1,g.latlng[0])
      sheet.update_cell(i,2,g.latlng[1])
      i=i+1
      #location = geolocator.reverse('16.5167, 80.6667')
      #print("Predicted location is :", location.address) #
      #sheet.update_cell(i,3,location)
      doTransaction("Chalasani Nagar Kanuru, Vijayawada, Andhra Pradesh 520007", g.latlng[0], g.latlng[1])
      return


GPIO.add_event_detect(a,GPIO.RISING)
GPIO.add_event_callback(a,action)
try:
    while True:
        print('gas detected')
        urllib2.urlopen('https://api.thingspeak.com/update?api_key=P3QN3VX5DFS2UYEU&field1=0')
        time.sleep(1)
except Exception as e:
    print(e)
    GPIO.cleanup()
    sys.exit()
