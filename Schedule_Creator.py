# PROJECT DAHLIA

# METHODS: add employee, edit an employee (blacklist, whitelist, availability, ...), delete an employee, select dates for the schedule, 

import os
import sys
import random
#also import other things


quit = False


def Employee_menu():
    quit2 = False
    while quit2 == False:
        print('Welcome to the Employee Menu!')
        print('*' * 149)
        print("Please enter the number corresponding to the action you'd like to take\n")
        print("1: enter all positions this program will schedule for *DO THIS FIRST*")
        print('2: add an employee')
        print('3: edit an employee / specify time off or time on for an employee')
        print('4: search an employee')
        print('5: delete an employee')
        print('6: return to main menu')
        print('*' * 149)
        choice2 = input('')
        if choice2 == '1':
            Position_assign()
        if choice2 == '2':
            valid = False
            while valid == False:
                employee_type = ((input("What is the employee's job title? (for example: server, host/bus etc.) ")).strip()).lower()
                if employee_type in Positions:
                    valid = True
                else:
                    print('Invalid position, check spelling and try again')
            employee_name = ((input("what is the name of the employee? ")).title()).lower()
            if employee_name in Employee_names and Employees[employee_name]['title'] == employee_type:
                print('An employee with this name has already been created in this position. Returning to employee menu.')
            else:
                Add_Employee(employee_name, employee_type)
        if choice2 == '3':
            Edit_Employee()
        if choice2 == '4':
            Search = input("What employee would you like to view the information of?")
            if Search in Employees:
                Search_Employee(Search)
            else:
                print('there is no employee named', Search + '. returning to menu.')
        if choice2 == '5':
            Delete = input("What employee would you like to remove from Employee_Data?")
            if Delete in Employees:
                del Employees[Delete]
                x = 0
                while x < len(Employee_names):
                    if Employee_names[x] == Delete:
                        del Employee_names[x]
                        break
                    x += 1
                Update() 
            else:
                print('there is no employee named', Delete + '. returning to menu.')
        if choice2 == '6':
            print('returning to main menu')
            break

def Schedule_moderation():
    quit2 = False
    while quit2 == False:
        print('Welcome to the Schedule Moderation Menu!')
        print('*' * 149)
        print("Please enter the number corresponding to the action you'd like to take\n")
        print("1: Set the number of employees on for each shift for one position through the week")
        print("2: return to main menu")
        print('*' * 149)
        choice2 = input('')
        if choice2 == '1':
            valid = False
            while valid == False:
                set_position = input('What position would you like to set shifts for?')
                if set_position in Positions:
                    valid = True
                else:
                    print('Invalid position, check spelling and try again')
            Set_Shifts(set_position)
        if choice2 == '2':
            print('returning to main menu')
            quit2 = True
            break

def Schedule_generator():
    quit2 = False
    while quit2 == False:
        print('Welcome to the Schedule Creator!')
        print('*' * 149)
        print("Please enter the number corresponding to the action you'd like to take\n")
        print("1: Enter the week's dates and generate a schedule")
        print("2: Export schedule to review/print")
        print("3: return to main menu")
        print('*' * 149)
        choice2 = input()
        if choice2 == '1':
            Generate()
        if choice2 == '3':
            print('returning to main menu')
            break

try: 
    P = open('Positions.txt', 'r')
    Positions = P.readlines()
    p = 0
    while p < len(Positions):
        x = Positions[p].strip()
        Positions[p] = x
        p+=1
    print(Positions)
    P.close()
except:
    Positions = []

def Position_assign():
    global Positions
    Positions = ((input('please enter all positions you plan to create a schedule for.\nSeparate entries with spaces and ensure spelling is EXACTLY as you will enter it when adding employees.')).lower()).split(' ')
    Position_Upload = open('Positions.txt', 'w')
    for x in Positions:
        Position_Upload.write(x + '\n')
    Position_Upload.close()

def Update():
        try:
            n = 0
            Employee_Data = open('Employee_Data.txt', 'w')
            New_Data_List = []
            for E in Employee_names:
                New_Data = str(Employee_names[n]) + '-title:'+str(Employees[E]['title'])+ '-Availability:'+ str(Employees[E]['availability']) + '-hours: ' + str(Employees[E]['hours'])
                if 'time_on' in Employees[E]:
                    New_Data += '-time_on:' + Employees[E]['time_on']
                if 'time_off' in Employees[E]:
                    New_Data += '-time_off:' + Employees[E]['time_off']
                New_Data += '\n'
                New_Data_List.append(New_Data)
                n += 1
            print(New_Data_List)
            Employee_Data.writelines(New_Data_List)
            Employee_Data.close()
            print('Update completed successfully!')
        except:
            print("Update failed, an error occurred")

Employee_names = []
Employees = dict()

try: 
    Data = open('Employee_Data.txt', 'r')
    read = Data.readlines()
    count = 0
    r = len(read)
    while r > 0:
        E = (read[count]).split('-')
        count += 1
        employee_name = E[0]
        if employee_name not in Employee_names:
            Employee_names.append(employee_name)
            employee_title = E[1].split(':')
            Employees[employee_name] = {'title': employee_title[1]}
            employee_availability = E[2].split(':')
            del employee_availability[0]
            A = (':').join(employee_availability)
            A = A.split(' ')
            del A[len(A) - 1]
            A = (' ').join(A)
            Employees[employee_name]['availability'] = A
            employee_hours = E[3].split(':')
            Employees[employee_name]['hours'] = employee_hours[1]
            try:
                q = E[4].split(':')
                r = str(q[0])
                del q[0]
                Employees[r] = (':'.join(q[1])).split(' ')
            except:
                literally_nothing = True
            try:
                p = E[5].split(':')
                s = str(p[0])
                del [p[0]]
                Employees[s] = (':'.join(p[1])).split(' ')
            except:
                literally_nothing = True
        r -= 1
    print(Employees)
except:
    Employees = dict()


def Day_Availability(days_available):
    shifts_str = ''
    days_complete = 0
    while days_complete < len(days_available):
        Valid_shifts = False
        while Valid_shifts == False:
            print('please specify shifts for', days_available[days_complete] + ': ', end = '')
            shifts = (input()).split()
            print(shifts)
            z = 0
            while z < len(shifts):
                if shifts[z] == '1' or shifts[z] == '2' or shifts[z] == '3' or shifts[z] == '4':
                    z += 1
                    Valid_shifts = True
                else:
                    print("Invalid shifts, please re-enter this Employee's available shifts for", days_available[days_complete])
                    Valid_shifts = False
                    shifts_str = ''
                    z = 100000  
        shiftsies = ''
        o = 1
        for i in shifts:
            shiftsies += str(i)
            if o < len(shifts):
                shiftsies += ','
            o += 1
        shifts_str += days_available[days_complete] + ':' + shiftsies + ' '
        days_complete += 1
    return shifts_str  

def Add_Employee(employee_name, employee_type):
    if employee_name in Employee_names:
        if Employees[employee_name]['title'] == employee_type:
            print('An employee with this name has already been created in this position. Returning to employee menu.')
            return
    valid_day = False
    while valid_day == False:
        days_available = (((input('Please enter the days of the week this employee is able to work \n\
                           (Please separate days via spaces and shorten days to the first 3 letters of the word): ')).strip()).lower()).split(' ')
        for x in days_available:
            if x != 'mon' and x != 'tue' and x != 'wed' and x != 'thu' and x != 'fri' and x != 'sat' and x != 'sun':
                print('Entry invalid, Try again')
            else:
                valid_day = True
    print('PLEASE NOTE!! in order to properly enter available time slots:\n"1" marks opening availability,\n"2" marks morning availability,\n"3" marks swing availability,\n"4" marks closing availability\n\tPlease separate entries with spaces')
    print(days_available)
    if employee_name not in Employee_names:
        Employee_names.append(employee_name)
    days_str = Day_Availability(days_available)
    addition = {'title': employee_type, 'availability': days_str, 'hours': 40}
    Employees[employee_name] = addition
    print(employee_name, 'has been added to the list of Employees.')
    print(Employees)
    Update()
    cont = (input('Enter "y" to add another employee, else type any other key to return to exit the Add_Employee() function.')).lower()
    if cont != 'y':
        
        return
    elif cont == 'y':
        employee_type = ((input("What is the employee's job title? (for example: server, host/bus etc.) ")).strip()).lower()
        employee_name = ((input("what is the name of the employee? ")).title()).lower()
        Add_Employee(employee_name, employee_type)
    


def Edit_Employee():
    z = False
    while z == False:
        change = input('Enter the name of the employee you would like to change: ').lower()
        if change in Employee_names:
            z = True
        else:
            print(change, 'is not contained in the current list of employees. Returning to employee menu.')
            return
    change_availability = ((input("Enter 'y' if you would like to edit this employee's availability: ")).strip()).lower()
    change_hours = ((input("Enter 'y' if you would like to change this employee's weekly hour limit: ")).strip()).lower()
    if change_hours == 'y':
        numeric = False
        while numeric == False: 
            try:
                new_hours = int(input("what would you like this employee's hours per week limit to be?"))
                Employees[change]['hours'] = new_hours
                numeric = True
            except:
                print('Your input contained non-numeric characters and caused an exception. Try again.')
    if change_availability == 'y':
        print('Since you selected to change availability, you will first be directed to the same function as "add employee."')
        print("However, since you are only editing one employee, it is important that you do not type 'y' when you are finished")
        print("Once you exit from the 'Add_Employee,' you will be prompted for specific time on and off")
        Add_Employee(change, Employees[change]['title'])
        more_availability = input("Please enter 'y' if you would like to add specific dates of time on or off")
        if more_availability == 'y':
            add_time_on = input("Please enter 'y' if you would like to add specific dates of time on")
            if add_time_on == 'y': 
                days_on = input("please enter specific dates available in MM/DD/YY format separated by spaces:").split()
                time_on = Day_Availability(days_on)
                add_time_off = input("Please enter 'y' if you would like to add specific dates of time off")
                if add_time_off == 'y':
                    days_off = input("please enter specific dates available in MM/DD/YY format separated by spaces:").split()
                    time_off = Day_Availability(days_off)
                    Employees[change]['time_off'] = time_off
                Employees[change]['time_on'] = time_on
                Update(Employees[change]['availability'])     


def Search_Employee(Employee):
    print(Employee, 'is contained within Employee_Data')
    print(Employee, 'is set for a maximum of', Employees[Employee]['hours'])
    print(Employee + "'s availability is as follows:", Employees[Employee]['availability'])
    print(Employee+"'s job title is:",Employees[Employee]['title'])
    if 'time_on' in Employees[Employee]:
        print(Employee, 'is set to be on for these days outside of their regular availability:', Employees[Employee]['time_on'])
    if 'time_off' in Employees[Employee]:
        print(Employee, 'is set to be off for these days/shifts', Employees[Employee]['time_off'])

def Day_Assign(date, day, victims):
    availabilities = [{1: [], 2: [], 3: [], 4: []}]
    for v in victims:
        avail = Employees[v]['availability'].split(' ')
        organized_availability = dict()
        for a in avail:
            a.split(':')
            organized_availability[a[0]] = a[1].split(',')
        if day in organized_availability:
            for n in organized_availability:
                availabilities[n].append(v)
        try:
            org_on = dict()
            time_on = Employees[v]['time_on']
            for t in time_on:
                t.split(':')
                org_on[t[0]] = t[1].split(',')
            if date in org_on:
                for n in org_on:
                    if v not in availabilities[n]:
                        availabilities[n].append(v)
        except:
            literally_nothing = True
    return availabilities
    


def Generate():
    victims = []
    dates = dict()
    year = input('Please complete the current year: 20')
    sched = input('Please enter the position you would like to create the schedule for: ')
    print('(Yes this does mean the program will no longer work at the turn of the century)')
    dates['mon'] = input("please enter monday's date in MM/DD format for the schedule: ")
    dates['tue'] = input("please enter tuesday's date in MM/DD format for the schedule: ")
    dates['wed'] = input("please enter wednesday's date in MM/DD format for the schedule: ")
    dates['thu'] = input("please enter thursday's date in MM/DD format for the schedule: ")
    dates['fri'] = input("please enter friday's date in MM/DD format for the schedule: ")
    dates['sat'] = input("please enter saturday's date in MM/DD format for the schedule: ")
    dates['sun'] = input("please enter sunday's date in MM/DD format for the schedule: ")
    days_of_week = {1: 'mon', 2: 'tue', 3: 'wed', 4: 'thu', 5: 'fri', 6: 'sat', 7: 'sun'}
    increment = 1
    week_availabilities = dict()
    for E in Employee_names:
        if Employees[E]['title'] == sched:
            victims.append(E)
    for d in dates:
        date = str(d) + '/' + str(year)
        day = days_of_week[increment]
        week_availabilities[day] = Day_Assign(date, day, victims)
        increment += 1
    
        
    



try:
    input_shifts = open('Shift_Data', 'r')
    Shifts = input_shifts.readlines()
    input_shifts.close()
except:
    Shifts = []

def Set_Shifts(position):
    Shifties = {position:{'mon-thu': {'open':'', 'morning':'', 'swing':'', 'night':''}, 'fri':{'open':'', 'morning':'', 'swing':'', 'night':''}, 'sat':{'open':'', 'morning':'', 'swing':'', 'night':''}, 'sun':{'open':'', 'morning':'', 'swing':'', 'night':''}}}
    days = ['mon-thu','fri','sat','sun']
    D = 0
    for S in Shifties[position]:
        print("Please specify the opening time for", days[D] + ', as well as the amount of', position + 's you would like to have on at this time. Please separate entries with a space:', end = '')
        Shifties[position][days[D]]['open'] = input(' ')
        mornings = input("Please specify other morning shift start times. Press enter twice if you do not want any more employees to come in after open. Separate entries with a space: ").split(' ')
        morn_str = ''
        if mornings != '':
            morn_starts = []
            for x in mornings:
                print('Please enter the number of employees you would like to come in at', x + ':', end = '')
                numba = input(' ')
                morn_starts.append(numba)
            a = 0
            while a < len(mornings):
                morn_str += mornings[a] + ' ' + morn_starts[a] + ' '
                a += 1
        morn_str += ';'
        morn_end = input('Please enter the time you would like the morning shift to end: ')
        morn_str += 'end-'+str(morn_end)
        Shifties[position][days[D]]['morning'] = morn_str
        print('Please specify the start and the end of the swing shift for', S + '. If this day does not have a swing shift, simply press enter three times. separate entries with a space: ', end = '')
        try: 
            swings = input(' ').split(' ')
            start = input('How many afternoon shifts would you like to start during swing? ')
            end = input('How many morning shifts would you like to go through the swing shift? ')
            swing_start = swings[0] + ' ' + start
            swing_end = swings[1] + ' ' + end
            Shifties[position][days[D]]['swing'] = swing_start + '-' + swing_end
        except:
            literally_nothing = True
        Shifties[position][days[D]]['night'] = input('Please enter the start time of the night shift and the number of night shifts separated by a space: ')
        D += 1
        print(' ')
    Shifties[position]['mon'] = Shifties[position]['mon-thu']
    Shifties[position]['tue'] = Shifties[position]['mon-thu']
    Shifties[position]['wed'] = Shifties[position]['mon-thu']
    Shifties[position]['thu'] = Shifties[position]['mon-thu']
    days = ['fri','sat','sun','mon', 'tue', 'wed', 'thu']
    D = 0
    del Shifties[position]['mon-thu']
    for S in Shifties[position]:
        write_str = S + '  ' + 'open-' + Shifties[position][days[D]]['open'] + ';morning-' + Shifties[position][days[D]]['morning'] + ';swing-' + Shifties[position][days[D]]['swing'] + ';night-' + Shifties[position][days[D]]['night'] + '\n'
        Shifts.append(write_str)
        D += 1
    write_shifts = open(str(position) + '_Shift_Data.txt', 'w')
    write_shifts.writelines(Shifts)
    write_shifts.close()

def Recall_Parameters(position):
    try:
        reading = open(str(position) + '_Shift_Data.txt', 'r')
        raw_data = reading.readlines()
        Parameters = []
        for r in raw_data:
            #opening stuff
            setup = r.split('   ')
            data = setup[1].split(';')
            open_stuff = data[0].split('-')
            open_stuff[1].split(' ')
            open_time = open_stuff[1][0]
            open_ppl = open_stuff[1][1]
            #morning stuff
            if len(data[1]) > 11:
                morn_stuff = data[1].split('-')
                morn_stuff[1].split(' ')
                x = len(morn_stuff[1])
                morn_keys = dict()
                while x > 1:
                    morn_keys[morn_stuff[1][0]] = morn_stuff[1][1]
                    del morn_stuff[0]
                    del morn_stuff[1]
                    x -=   
            #swing stuff
            swing_stuff = data[2].split('-')
                

    except:
        print('An error occurred accessing the Shift_Data file for', position)
            
while quit == False:
    print('Howdy! welcome to the schedule maker!')
    print("If you're a first time user or need any help, please type 'help' on the menu screen for a list of instructions to this program")
    print("*" * 149)
    print("Please enter the number corresponding to the action you'd like to take\n")
    print('1: Edit/update employee information')
    print('2: Moderate schedule parameters')
    print('3: Create a new schedule')
    print('4: Exit the program')

    # print('1: add an employee')
    # print('2: edit an employee')
    # print("3: enter the week's dates")
    # print('4: export schedule to review/print')
    # print('5: update previous employee data')
    # print('6: edit the number of employees on for each shift')
    # print('7: search an employee')
    print("*" * 149)
    choice = input()
    if choice == '1':
        Employee_menu()
    elif choice == '2':
        Schedule_moderation()
    elif choice == '3':
        Schedule_generator()
    elif choice == '4':
        quit = True
