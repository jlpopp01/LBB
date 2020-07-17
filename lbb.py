import datetime

#check to see if user would like to make an entry

"""the variables are acting a fool. you need to figure this out"""

class Entry:

    def __init__(self, date, note):
        self.date = str(date)
        self.note = note

def lbb():
    while True:
        entry = input("Would you like to make an entry? Y/N format. N to Quit. ").lower()
        if entry == 'y':
            date = input("What date would you like to save? Please use MM-DD-YYYY format. ")
            note = input('What note would you like to save? Keep it short and sweet, 250 character limit.  ')
        elif entry == 'n':
            break 


#lbb() #activate

lbb()



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

print(date + " " + note)
