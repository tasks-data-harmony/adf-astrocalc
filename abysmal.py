from datetime import *
import ephem

#establish today 
today = date.today()
working_date = datetime.today()

secondzerozero = ephem.Date('2010/12/21') #full moon  total lunar eclipse on winter solstice
s00 = secondzerozero.datetime() #convert it to format that can math 
#establish date of origin
pin = ephem.next_solstice('2010/12/20')#establish date of origin 
strip_pin = pin.datetime() #convert to datetime for calculations
#print strip_pin 

#define solstices & equinoxes
last_solstice = ephem.previous_solstice(working_date) #calculate solstice date
last_solstice = last_solstice.datetime() #convert to datetime
#print last_solstice
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
		return "N~~Y~~~~D~~"
	else:
		    x =  (daily_difference(s00, y)) 
		    year  = (Winter_Solstice.year - s00.year ) 
		    #month = x/29
		    #print month
		    z = (daily_difference(last_solstice,y))
		    month = z/28
		    # month
		    #day = z/(month + 1)
		    #day = int(z/28.0 )
		    day = int((z/28.0 - month)*27.75)
		    #print day
		    if day > 365: #sometimes things go wrong
				month = month +1 # so we fudge the calculations
				if month >= 13:
					month = month -13
				day = day - 28 #hopefully I will figure out how to do this better
		    if month == 13 and day == 28 and year%3 == 0:
				return "Leap Day"
		    while month >= 13:
		        month = month - 13
		    else:
		    	month = month #don't let the computer fool you, this is necessary to return to the calculations!
    	return str(year) +"~"+str(month)+"~"+str(day)


second1 = ephem.Date('2010/12/22')
s1 = second1.datetime()
s11 = get_Abysmal_Date(s1)
#print s11
today0 = get_Abysmal_Date(working_date)
#print today0
