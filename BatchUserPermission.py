#PPMSBatchPermissions
#v1.0 Jun 2018
#Python 2.7 (2016)
#Author : Christopher Hall, Wellcome Sanger Institute, christopher.hall@sanger.ac.uk
#License : GPLv3 https://www.gnu.org/licenses/gpl-3.0.html

#Add your details (line 15 & 21, url, apikey & id) and run this script.  
#It will take the details from the txt file and change these users permissions.
#The pumapi requires the login names for the users.  Your pumapi key needs user access permission. 
#You need to change the 'id' of the system you want changing and choose the level of the user in 'type'.  
#N=novice, A=Autonomous.

import requests

url='https://ppms.eu/xxx/pumapi/'
headers = {'content-type': 'application/x-www-form-urlencoded'}

with open('tochange.txt','r') as file:
    for line in file:
        line = line.replace("\n", "").replace("\r", "")
        payload = {'apikey': 'xxx', 'action': 'setright', 'id':'x', 'login': line, 'type':'N'}
        r = requests.post(url, data=payload, headers=headers)
