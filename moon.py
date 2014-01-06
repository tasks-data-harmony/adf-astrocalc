from datetime import *
import ephem
#import astrocalc

#define days & years
today = date.today()  
working_date = datetime.today()

previous_new_moon = ephem.previous_new_moon(today)
previous_new_moon = previous_new_moon.datetime()
print previous_new_moon

next_new_moon = ephem.next_new_moon(today)
next_new_moon = next_new_moon.datetime()
print next_new_moon

def daily_difference(first, second):
    #calculate number of days
    x = abs(second.date()- first.date())
    #remove timedelta stamp
    daily_difference = x.days
    #produce results
    return daily_difference

def passage(first, working_date):
    #determine if day is passed or coming
    if (first < working_date):
        return str(daily_difference(first, working_date)) + " days since " 
    elif (working_date < first):
        return str(daily_difference(working_date, first)) + "  days until "
    elif (working_date == first):
        return "-------- This is today. --------"
    else:
        return "The Sky is falling."   
        
new_moon_cycle = daily_difference(previous_new_moon, next_new_moon)
from_today = daily_difference(previous_new_moon, working_date)
print str(from_today)+ "/"+str(new_moon_cycle)

