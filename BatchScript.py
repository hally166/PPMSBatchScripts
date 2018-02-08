#Copyright (c) 2018 Genome Research Ltd.

#PPMSBatchBooking
#v1.0 Feb 2018
#Python 2.7 (2016)
#Author : Christopher Hall, Wellcome Sanger Institute, christopher.hall@sanger.ac.uk

#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

#Add your details and run this script.  It will take the details from the csv and book onto PPMS. 

import requests
import csv

#constants, cahnge url to match your own
url='https://ppms.eu/xxx/API2/'
headers = {'content-type': 'application/x-www-form-urlencoded'}

#booking function, use your API key and coreid
def booking():
    payload = {'apikey': 'xxx', 'action': 'SetSessionBooking', 
           'coreid': '2', 'systemid': system, 'projectid': '0', 'SE1': 'false', 'SE2': 'false', 
           'comment': '', 'repeat': '0', 'user': user, 'assisted': 'false', 'assistant': '0', 
           'form': '', 'start': startT, 'end': endT}
    r = requests.post(url, data=payload, headers=headers)

#read the csv and book sessions
csv_file= open('bookings.csv', "r")
read = csv.reader(csv_file)
next(read)
for row in read :
     startT=row[0]+'T'+row[1]
     endT=row[0]+'T'+row[2]
     system=row[3]
     user=row[4]
     booking()
csv_file.close()
