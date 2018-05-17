import csv

events = []
dates = []
starttime = []
endtime = []


def eventcsvread():
    try:
        with open('events.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                events.append(row[0])
                dates.append(row[1])
                starttime.append(row[2])
                endtime.append(row[3])

    except FileNotFoundError:
        open('events.csv', 'w')
        eventcsvread()
            

def eventcsvwrite():
    with open('events.csv', 'a', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        event_name = input('Event name: ')
        event_date = input('Event date: ')
        start_time = input('Start time: ')
        end_time = input('Endtime: ')
        filewriter.writerow([event_name, event_date, start_time, end_time])


def eventview():
    v = int(input('\nEvent number: '))
    v -= 1
    print('\nEvent: ', events[v])
    print('Date: ', dates[v])
    print('Time: ', starttime[v], 'till', endtime[v])


def eventllist():
    namelen = len(events)
    listnum = 1
    for i in range(0, namelen):
        print(listnum, '. ', events[i])
        listnum += 1


def eventlistclear():
    events.clear()
    dates.clear()
    starttime.clear()
    endtime.clear()


def eventadd():
    eventcsvwrite()
    eventlistclear()
    eventcsvread()
    

def eventdelete():
    file = open('events.csv', 'r')
    lines = file.readlines()
    file.close()
    delnum = int(input('Events number to delete: '))
    delnum -= 1
    del lines[delnum]
    open('Events.csv', 'w').writelines(lines)
    eventlistclear()
    eventcsvread()


def events_command_menu():
    print('COMMAND MENU')
    menuchoices = [
        'list - Display all events',
        'view - View an event',
        'add - Add an event',
        'del - Delete an event',
        'exit - Exit program'
        ]
    size = len(menuchoices)
    for i in range(0, size):
        print(menuchoices[i])


events_command_dict = {
    'list': eventllist,
    'view': eventview,
    'add': eventadd,
    'del': eventdelete
    }


