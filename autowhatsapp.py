import pywhatkit
import datetime
from Whatpy import  webdmclose 


current_time = datetime.datetime.now()
 

pywhatkit.sendwhatmsg("+919819535276", "Message-2", current_time.hour, current_time.minute+1)

# webbrowser.open('http://example.com') 
# webdmclose("+919819535276", "Message-2");