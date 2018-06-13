These are scripts to automate the use of [PPMS](http://stratocore.com/) using Python.

You need to install the [requests](http://docs.python-requests.org/en/master/) package into python.  use `pip install 'requests'`

## Batch Booking

It takes the bookings as inputted into the .csv file and books them in PPMS.  An example .csv is included. 

## Batch Delete

The oposite of the booking script.  This one uses session IDs as inputtted via the .txt file.

## User Permissions

This will add or change user permissions _en masse_.  It requires a list of user logins as a .txt file.
