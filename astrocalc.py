from datetime import *
import ephem
import abysmal
"""if I am going to package this for anyone else to use, i am going to need to package pyephem as well"""


#define days & years
today = date.today()  
working_date = datetime.today()
#define solstices & equinoxes
last_solstice = ephem.previous_solstice(today) #calculate solstice date
last_solstice = last_solstice.datetime() #convert to datetime

previous_equinox = ephem.previous_equinox(today) #calculate equinox date
previous_equinox = previous_equinox.datetime() #convert to datetime

next_solstice = ephem.next_solstice(today) #calculate solstice date
next_solstice = next_solstice.datetime() #convert to datetime

next_equinox = ephem.next_equinox(today) #calculate equinox date
next_equinox = next_equinox.datetime() #convert to datetime

#calculate cross-quarter high days
def cross_quarter(last, next):
    midpoint=abs((next-last))/2
    midpoint=next-midpoint
    if last < midpoint < next: #this insures that midpoint falls between
        return midpoint        #the two endpoints 
    else:
        midpoint=abs((next-last))/2
        midpoint=last-midpoint
        return midpoint    

a_crossquarter = cross_quarter(last_solstice, previous_equinox)
b_crossquarter = cross_quarter(previous_equinox, next_solstice)
c_crossquarter = cross_quarter(next_solstice, next_equinox)


def celebrate():
    if next_solstice < next_equinox:
        if today < b_crossquarter.date():
            return b_crossquarter
        else:
            return next_solstice
    else:
        if today < b_crossquarter.date():
            return b_crossquarter
        else:
            return next_equinox           
next_high_date = celebrate()

# define zodiac sign for date
zodiacs = [(120, 'Capricorn'), (218, 'Aquarius'), (320, 'Pisces'), (420, 'Aries'), (521, 'Taurus'),
           (621, 'Gemini'), (722, 'Cancer'), (823, 'Leo'), (923, 'Virgo'), (1023, 'Libra'),
           (1122, 'Scorpio'), (1222, 'Sagittarius'), (1231, 'Capricorn')]

# define Ogham calendar sign for date
ogham_signs = [(119,'Birch'),(217,'Rowan'),(317,'Ash'),(414,'Alder'),(512,'Willow'),(609,'Hawthorn'),(717,'Oak'),
                (804,'Holly'),(901,'Hazel'),(929,'Apple'),(1027,'Ivy'),(1124,'Broom'),(1221,'Elder'),(1223,'Pine'),
                (1231,'Birch')]

# define planet for day of the week
seven_planets = [(0,'Moon'),(1,'Mars'),(2,'Mercury'),(3,'Jupiter'),(4,'Venus'),(5,'Saturn'),(6,'Sun')]

# define high days
high_days = [(2, 'Imbolc'), (3,'Spring Equinox'),(5,'Beltaine'),(6,'Summer Solstice'),
             (8, 'Lughnasadh'),(9,'Autumn Equinox'),(11,'Samhain'),(12,'Winter Solstice')]
def get_high_day(date):
    month_number = int(date.month)
    for z in high_days:
        if month_number == z[0]:
            return z[1]

# fetch planet name for day of week 
def get_seventh_sign(date):
    day_of_week = working_date.weekday()
    for z in seven_planets:
        if day_of_week == z[0]:
            return z[1]
planet = get_seventh_sign(working_date)
#iterate over a dictionary list 
def number_code_date(date,x):
    date_number = int("".join((str(date.date().month), '%02d' % date.date().day)))
    for z in x:
        if date_number < z[0]:
            return z[1]  
            
#calculates the time between two dates.
def daily_difference(first, second):
    #calculate number of days
    x = abs(second- first)
    #remove timedelta stamp
    daily_difference = x.days
    #produce results
    return daily_difference

#used to calaculate days passed or days to pass between high day and today
def passage(first, working_date):
    #determine if day is passed or coming
    if (first < working_date):
        return ": " +str(daily_difference(first, working_date)) + " days since " 
    elif (working_date < first):
        return  ": " + str(daily_difference(working_date, first)) + "  days until "
    elif (working_date == first):
        return "-------- This is today. --------"
    else:
        return "The Sky is falling."    

def sort_days():
    a = previous_equinox#.date()
    b = a_crossquarter#.date()
    c = last_solstice#.date()
    d = b_crossquarter#.date()
    e = next_equinox#.date()
    f = c_crossquarter#.date()
    g = next_solstice#.date()
    h = working_date
    order = sorted([a,b,c,d,e,f,g,h])
    return order
list_of_dates = sort_days() #produces ordered list of calculated days

seventh_sign = get_seventh_sign(working_date)
ogham_sign = number_code_date(working_date, ogham_signs)
sun_sign = number_code_date(working_date, zodiacs)
# big table of dates, sorted and labelled with time passage
for n in range(len(list_of_dates)):
	if list_of_dates[n] == working_date:
		print abysmal.get_Abysmal_Date(list_of_dates[n]), passage(list_of_dates[n], working_date), seventh_sign, sun_sign, ogham_sign 
	else:	
		print abysmal.get_Abysmal_Date(list_of_dates[n]), passage(list_of_dates[n], working_date), get_high_day(list_of_dates[n])

