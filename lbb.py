import datetime
import time
#for date verification

'''
Working on...
countdown to date
print date/note/countdown to terminal
'''

#set up some variables
class Entry:

    def __init__(self, entry, day, note):
        self.entry = entry
        self.day = day
        self.note = note


#get a loop going - can make an entry or exit
while True:
    entry = input("Would you like to make an entry? Y/N format. N to Quit ").lower()
    if entry == 'y':
        day = input("What date would you like to save? Please use YYYY-MM-DD format. ")
        try:
            day = datetime.datetime.strptime(day, '%Y-%m-%d')
        except ValueError:
            print("Wrong format, please try again")
            continue
#this throws it back if date invalid
        note = input('What note would you like to save? Keep it short and sweet, 280 character limit.  ')
        if len(note) > 280:
            print("Twitter rules here. Nothing after 280. ")
            note[0:280]
            continue
#this throws it back if note invalid
#create and write to file
        f = open("lbb.txt", "a")
        f.write( " \n" + str(day) + " " + note)
        f.close()
        continue
    elif entry == 'n':
        print("Allons-y!")
        break 
    elif entry != 'y':
        print("That's not an option, let's try again. ")
        continue
for day in entry:
    countdown = datetime.datetime(day) - datetime.datetime.today()

print(countdown)
print(note + " " + day + " ")
