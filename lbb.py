import datetime

#check to see if user would like to make an entry

"""can access vars now. tests work but do not kick back to reenter. does not save to anything right now, so loop will only print most recent entry"""

class Entry:

    def __init__(self, date, note):
        self.date = str(date)
        self.note = note

while True:
    entry = input("Would you like to make an entry? Y/N format. N to Quit. ").lower()
    if entry == 'y':
        date = input("What date would you like to save? Please use MM-DD-YYYY format. ")
        note = input('What note would you like to save? Keep it short and sweet, 250 character limit.  ')
    elif entry == 'n':
        break 


#this function checks to see if the date is valid
def is_valid_date(date):
    try:
        datetime.datetime.strptime(date, '%m-%d-%Y')
    except ValueError:
        print("Wrong format, please try again")

is_valid_date(date)

#this function will limit the characters



def is_note_short(note):
    if len(note) > 280:
        print("Twitter rules here, keep it short.")


is_note_short(note)

f = open("lbb.txt", "w")
f.write(date + " " + note)
f.close()


print(date + " " + note)
