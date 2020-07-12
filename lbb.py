#if database?
lbb = []

#Gather info from user I think this might need to be in the while loop
#entry = input("Would you like to make an entry? Y/N format. N to Quit. ")
date = input("What date would you like to save? Please use MM/DD/YYYY format. ")
note = input('What note would you like to save? Keep it short and sweet, 250 character limit.  ')

#run loop until quit
#while (entry='Y'):
    #continue

# check to make sure the entry is valid per perimeters
#if (entry='N'):
    #break
    elif (input != MM/DD/YYY):
    print("Wrong format, please try again")
    elif (len(note) > 250 characters):
    print("Keep it short and cover the topic")

#merge input into one object
.join(date,note)

#write info to csv file
fd = open(filename, "lbb.csv")
input = raw_input(date + " , " + note)
fd.write(input)

#or append to database
.append(date + note) -> lbb.csv

#print entries
print (lbb)

def lbb():
    entry = []
    while True:
        entry = input("Would you like to make an entry? Y/N format. N to Quit. ").lower()
        if entry == 'n':
            break
