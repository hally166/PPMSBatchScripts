#PPMS Batch Delete
#v1.0 Jun 2018
#Python 2.7 (2016)
#Author : Christopher Hall, Wellcome Sanger Institute, christopher.hall@sanger.ac.uk
#License : GPLv3 https://www.gnu.org/licenses/gpl-3.0.html

#Add your details (line 11&16, url, apikey & coreid) and run this script.  It will take the session numbers from the txt and delete the list of sessions from PPMS. 

import requests

url='https://ppms.eu/xxx/API2/'
headers = {'content-type': 'application/x-www-form-urlencoded'}

with open('todelete.txt', 'r') as todelete:
    for line in todelete:
        payload = {'apikey': 'xxx', 'action': 'SetSessionDelete', 'coreid': 'x', 'sessionid' :  line}
        r = requests.post(url, data=payload, headers=headers)
