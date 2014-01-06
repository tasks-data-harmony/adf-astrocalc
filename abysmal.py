from datetime import *
import ephem

#establish today 
today = date.today()
working_date = datetime.today()

secondzerozero = ephem.Date('2012/12/21')
s00 = secondzerozero.datetime()
#establish date of origin
pin = ephem.next_solstice('2012')#establish date of origin 
strip_pin = pin.datetime() #convert to datetime for calculations


#define solstices & equinoxes
last_solstice = ephem.previous_solstice(working_date) #calculate solstice date
last_solstice = last_solstice.datetime() #convert to datetime

#calculates the time between two dates.
def daily_difference(first, second):
    #calculate number of days
    x = abs(second.date()- first.date())
    #remove timedelta stamp
    daily_difference = x.days
    #produce results
    return daily_difference

def get_Abysmal_Date(y):
	year = y.year 
	month = '12' 
	year = str(y.year)
	bah = year+'/'+ month
	Winter_Solstice = ephem.next_solstice(bah)
	Winter_Solstice = Winter_Solstice.datetime()
	if y == Winter_Solstice:
		return "New Year's Day"
	else:
		    x =  (daily_difference(s00, y)) 
		    year  = (Winter_Solstice.year - s00.year ) - 1
		    month = x/29
		    day = int((x/28.0 - month)*27.75)-1
		    if day > 27: #sometimes things go wrong
				month = month +1 # so we fudge the calculations
				day = day -28 #hopefully I will figure out how to do this better
		    if month == 13 and day == 28 and year%3 == 0:
				return "Leap Day"
		    elif month >= 13:
		        month = month -13
		    else:
		    	month = month #don't let the computer fool you, this is necessary to return to the calculations!
    	return "Y"+str(year) +"~M"+str(month)+"~D"+str(day)


