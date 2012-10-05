from datetime import date, timedelta 
import ephem
"""if I am going to package this for anyone else to use, i am going to need to package pyephem as well"""
import dbus, gobject, dbus.glib #allows me to use Tomboy Notes as content

# Get the D-Bus session bus
bus = dbus.SessionBus()
# Access the Tomboy D-Bus object
obj = bus.get_object("org.gnome.Tomboy",
  "/org/gnome/Tomboy/RemoteControl")
# Access the Tomboy remote control interface
tomboy = dbus.Interface(obj, "org.gnome.Tomboy.RemoteControl")



#define days & years
today = date.today()  


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

#define moon phases
previous_new_moon = ephem.previous_new_moon(today)
previous_first_quarter_moon = ephem.previous_first_quarter_moon(today)
previous_full_moon = ephem.previous_full_moon(today)
previous_last_quarter_moon = ephem.previous_last_quarter_moon(today)
next_new_moon = ephem.next_new_moon(today)
next_first_quarter_moon = ephem.next_first_quarter_moon(today)
next_full_moon = ephem.next_full_moon(today)
next_last_quarter_moon = ephem.next_last_quarter_moon(today)

moon_phases = [
    ("New Moon", previous_new_moon),
    ("First Quarter Moon", previous_first_quarter_moon),
    ("Full Moon", previous_full_moon),
    ("Last Quarter Moon", previous_last_quarter_moon),
    ("New Moon", next_new_moon),
    ("First Quarter Moon", next_first_quarter_moon),
    ("Full Moon", next_full_moon),
    ("Last Quarter Moon", next_last_quarter_moon)
]

def ordered_moons():
    order = [sorted(moon_phases, key=lambda moon: moon[1])]
    return order

ordered_moons = ordered_moons()
            
#calculates the next high day in the orbit


# provide a label for the astronomical point
def label_point(x):
    if x.month == 2:
        label = "The February Feast"
        return label
    elif x.month == 3:    
        label = "The Spring Feast"
        return label
    elif x.month == 5:
        label = "The May Feast"
        return label
    elif x.month == 6:
        label = "The Summer Feast"
        return label
    elif x.month == 8:
        label = "The Autumn Feast"        
        return label
    elif x.month == 9:
        label = "The Fall Feast"
        return label
    elif x.month == 11:
        label = "The Novemeber Feast"
        return label
    elif x.month == 12:            
        label = "The Winter Feast"
        return label
    else:
        return "Time-Space ceases."

def tomboyNote(x):
    if x.month == 2:
        tomboyNote = tomboy.GetNoteContents(tomboy.FindNote("The February Feast"))
        return tomboyNote
    elif x.month == 3:
        tomboyNote = tomboy.GetNoteContents(tomboy.FindNote("The Spring Feast"))
        return tomboyNote
    elif x.month == 5:
        tomboyNote = tomboy.GetNoteContents(tomboy.FindNote("The May Feast"))
        return tomboyNote
    elif x.month == 6:
        tomboyNote = tomboy.GetNoteContents(tomboy.FindNote("The Summer Feast"))
        return tomboyNote
    elif x.month == 8:
        tomboyNote = tomboy.GetNoteContents(tomboy.FindNote("The Autumn Feast"))
        return tomboyNote
    elif x.month == 9:
        tomboyNote = tomboy.GetNoteContents(tomboy.FindNote("The Fall Feast"))
        return tomboyNote
    elif x.month == 11:
        tomboyNote = tomboy.GetNoteContents(tomboy.FindNote("The November Feast"))
        return tomboyNote
    elif x.month == 12:
        tomboyNote = tomboy.GetNoteContents(tomboy.FindNote("The Winter Feast"))
        return tomboyNote                             
    else:
        return "It's the End of the World as we know it."

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

        
        
#calculates the time between two dates.
def daily_difference(first, second):
    #calculate number of days
    x = abs(second- first)
    #remove timedelta stamp
    daily_difference = x.days
    #produce results
    return daily_difference

#used to calaculate days passed or days to pass between high day and today
def passage(first, today):
    days_since = " days since:"
    days_until = " days until:"
    #determine if day is passed or coming
    if (first < today):
        return days_since, daily_difference(first, today)
    elif (today < first):
        return  days_until, daily_difference(today, first)
    elif (today == first):
        return "******** This is today. *********"
    else:
        return "The Sky is falling."    

def sort_days():
    a = previous_equinox.date()
    b = a_crossquarter.date()
    c = last_solstice.date()
    d = b_crossquarter.date()
    e = next_equinox.date()
    f = c_crossquarter.date()
    g = next_solstice.date()
    order = sorted([a,b,c,d,e,f,g])
    return order
list_of_dates = sort_days() #produces ordered list of calculated days

        
# big table of dates, sorted and labelled with time passage
for n in range(len(list_of_dates)):
    print n+1, list_of_dates[n], label_point(list_of_dates[n]), passage(list_of_dates[n], today)    
    #print tomboyNote(list_of_dates[n])
print "Next High Day: ", tomboyNote(next_high_date) 
"""   
for n in range(len(ordered_moons)):
    print n+1, ordered_moons[n]"""   
#print tomboy.GetNoteContents(tomboy.FindNote("The Summer Feast"))    
# Display the contents of the note called Test
   
