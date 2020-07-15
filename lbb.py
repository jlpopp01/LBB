import datetime

#check to see if user would like to make an entry

date = input("What date would you like to save? Please use MM-DD-YYYY format. ")


def lbb():
    entry = []
    while True:
        entry = input("Would you like to make an entry? Y/N format. N to Quit. ").lower()
        if entry == 'y':
            make_note()
        elif entry == 'n':
            break 

#lbb() #activate


#this function checks to see if the date is valid
def is_valid_date(date):
    try:
        datetime.datetime.strptime(date, '%m-%d-%Y')
    except ValueError:
        print("Wrong format, please try again")

is_valid_date(date)

#this function will limit the characters

note = input('What note would you like to save? Keep it short and sweet, 250 character limit.  ')

def is_note_short(note):
    if len(note) > 250:
        print("Twitter rules here, keep it short.")


is_note_short(note)
#merge input into one object
#.join(date,note)

#write info to csv file
#fd = open(filename, "lbb.csv")
#input = raw_input(date + " , " + note)
#fd.write(input)

#or append to database
#.append(date + note) -> lbb.csv

print(date + " " + note)
