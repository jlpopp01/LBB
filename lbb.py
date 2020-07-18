import datetime
#for date verification

"""
the while loop now checks the conditions but it still doesnt return to the beginning. 
will start a file and write to it
still only writes the most recent entry
"""

#set up some variables
class Entry:

    def __init__(self, date, note):
        self.date = date
        self.note = note

#get a loop going - can make an entry or exit
while True:
    entry = input("Would you like to make an entry? Y/N format. N to Quit. ").lower()
    if entry == 'y':
        date = input("What date would you like to save? Please use MM-DD-YYYY format. ")
        try:
            datetime.datetime.strptime(date, '%m-%d-%Y')
        except ValueError:
            print("Wrong format, please try again")
#this should be throwing it back to the date var...
        note = input('What note would you like to save? Keep it short and sweet, 250 character limit.  ')
        if len(note) > 280:
            print("Twitter rules here, keep it short.")
#this should be throwing it back to the note var 
#create and write to file
        f = open("lbb.txt", "a")
        f.write( " \n" + date + " " + note)
        f.close()
    elif entry == 'n':
        break 

#print entry
print(date + " " + note)
