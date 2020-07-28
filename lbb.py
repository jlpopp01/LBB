import datetime
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
# this tests to see if the date input is valid
        note = input('What note would you like to save? Keep it short and sweet, 280 character limit.  ')
        if len(note) > 280:
            print("Twitter rules here. Nothing after 280. ")
            note[0:280]
            continue
#testing to see if the length is appropriate
#create and write to file
        f = open("lbb.txt", "a")
        f.write( " \n" + str(day) + " " + note)
        f.close()
        continue
    elif entry == 'n':
        print("Allons-y!")
        break 
#test for absolutely wrong input
    elif entry != 'y':
        print("That's not an option, let's try again. ")
        continue

'''this is a countdown that im working with and running circles with, don't mind it...

def datetime_to_int(day):
    return int(day.strftime("%Y%m%d"))

datetime_to_int(day)

countdown = datetime.datetime(day) - datetime.datetime.today()

print(countdown)
'''

print(note + " " + str(day) + " ")
