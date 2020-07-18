'''
this file has the tests from the while loop wrote out into functions 
it actually returns you to put in the information again 
but im stuck
'''

import datetime

class Entry:

    def __init__(self, date, note):
        self.date = str(date)
        self.note = str(note)


def get_date():
    date = input("What date would you like to save? Please use MM-DD-YYYY format. ")
    try:
        datetime.datetime.strptime(date, '%m-%d-%Y')
    except ValueError:
        print("Wrong format, please try again")
        return get_date()

def get_note():
    note = input('What note would you like to save? Keep it short and sweet, 250 character limit.  ')
    if len(note) > 280:
        print("Twitter rules here, keep it short.")
        return get_note()

def entry():
    entry = input("Would you like to make an entry? Please answer with y or n. ").lower()
    if entry == 'y':
        get_date()
        get_note()
        return entry()
    elif entry == 'n':
        quit

print(str(get_date()) + str(get_note()))
