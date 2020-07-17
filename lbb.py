import datetime

#check to see if user would like to make an entry

"""
the while loop now checks the conditions but it still doesnt return to the beginning. 
will start a file and write to it
still only writes the most recent entry
"""

class Entry:

    def __init__(self, date, note):
        self.date = date
        self.note = note

while True:
    entry = input("Would you like to make an entry? Y/N format. N to Quit. ").lower()
    if entry == 'y':
        date = input("What date would you like to save? Please use MM-DD-YYYY format. ")
        try:
            datetime.datetime.strptime(date, '%m-%d-%Y')
        except ValueError:
            print("Wrong format, please try again")
        note = input('What note would you like to save? Keep it short and sweet, 250 character limit.  ')
        if len(note) > 280:
            print("Twitter rules here, keep it short.")
    elif entry == 'n':
        break 


f = open("lbb.txt", "a")
f.write( " \n" + date + " " + note)
f.close()


print(date + " " + note)
