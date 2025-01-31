# PROJECT DAHLIA


import random
import os
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
                Employee_names.remove(Delete)
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
    P.close()
except:
    print("error opening and/or reading Positions.txt (if this is your first time using the program this is normal because you haven't created positions yet)")
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
            New_Data_List = []
            for E in Employee_names:
                New_Data = str(Employee_names[n]) + '-title:'+str(Employees[E]['title'])+ '-Availability:'+ str(Employees[E]['availability']) + '-hours: ' + str(Employees[E]['hours'])
                if 'time_on' in Employees[E]:
                    New_Data += '-time_on:' + Employees[E]['time_on']
                if 'time_off' in Employees[E]:
                    New_Data += '-time_off:' + Employees[E]['time_off']
                if '\n' not in New_Data:
                    New_Data += '\n'
                New_Data_List.append(New_Data)
                n += 1
            print(New_Data_List)
            Employee_Data = open('Employee_Data.txt', 'w')
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
        try:
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
                B = A.split(' ')
                #del B[len(B) - 1]
                B = (' ').join(B)
                Employees[employee_name]['availability'] = B
                employee_hours = E[3].split(':')
                Employees[employee_name]['hours'] = employee_hours[1]
                print('good so far')
                print(Employees)
                try:
                    q = E[4].split(':')
                    l = q.pop(0)
                    Employees[l] = (':'.join(q))
                except:
                    pass
                try:
                    p = E[5].split(':')
                    s = p.pop(0)
                    splitter = p[1].split(',')
                    Employees[s] = (':'.join(p))
                except:
                    pass
        except:
            pass    
        r -= 1
    print(Employees)
except:
    print('Failed to extract Data from Employee_Data.txt')
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
            continue_status = ('An employee with this name has already been created in this position. Please enter "y" if you would like to edit the employee, otherwise you will be returned to the employee menu: ')
            if continue_status == 'y':
                Employee_names.remove(employee_name)
                del Employees[employee_name]
            else:
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
    Update()     


def Search_Employee(Employee):
    print(' ')
    print(Employee, 'is contained within Employee_Data')
    print(Employee, 'is set for a maximum of', Employees[Employee]['hours'], 'hours')
    print(Employee + "'s availability is as follows:", Employees[Employee]['availability'])
    print(Employee+"'s job title is:",Employees[Employee]['title'])
    if 'time_on' in Employees[Employee]:
        print(Employee, 'is set to be on for these days outside of their regular availability:', Employees[Employee]['time_on'])
    if 'time_off' in Employees[Employee]:
        print(Employee, 'is set to be off for these days/shifts', Employees[Employee]['time_off'])
    print(' ')

def Day_Assign(date, day, victims):
    availabilities = {1: [], 2: [], 3: [], 4: []}
    print(victims, 'victims')
    victims_increment = 0
    while victims_increment < len(victims):
        print('Any employees?', Employees[victims[victims_increment]])
        who = victims[victims_increment]
        avail = Employees[who]['availability'].split(' ')
        organized_availability = dict()
        for a in avail:
            g = a.split(':')
            print(g)
            try:
                organized_availability[g[0]] = g[1].split(',')
            except:
                print('O_A:', organized_availability)
                break
            # print('Organized availability: ', organized_availability)
        if day in organized_availability:
            for n in organized_availability[day]:
                print('n: ',n)
                n = int(n)
                availabilities[n].append(victims[victims_increment])

        try: # THIS MUST BE EDITED IN ORDER TO INCLUDE THE SHIFTS I BELEIVE (Jk i think its good) ((fuck dude i think you whole system doesnt work, you need to map it to the number somehow))
            org_on = dict()
            time_on = Employees[victims[victims_increment]]['time_on']  
            for t in time_on:
                tt = t.split(':')
                org_on[tt[0]] = tt[1].split(',')
            if date in org_on:
                for n in org_on:
                    n = int(n)
                    if victims[victims_increment] not in availabilities[n]:
                        availabilities[n].append(victims[victims_increment])
        
        except:
            pass
        try:
            org_off = dict()
            time_off = Employees[victims[victims_increment]]['time_off']
            for t in time_off:
                ty = t.split(':')
                org_off[ty[0]] = ty[1].split(',')
            if date in org_off:
                for n in org_off:
                    n = int(n)
                    if victims[victims_increment] in availabilities[n]:
                        availabilities[n].remove(victims[victims_increment])
        except:
            pass
        victims_increment += 1
    print('iterations documented: ',availabilities)
    return availabilities

Formatting_Data_1 = dict()
morn_swingers = []
def Morning_Assignments(params, availables):
    
    morning_ppl = []
    through_swing = []
    #print(params) #the debugging journey took you here, you need to figure out why the first line in the next for loop is out of range
    print(availables)
    for day in params:
        openers = []
        print(availables, 'availables^^')
        open_candidates = availables[day][1]
        opener_count = int(params[day]['open_ppl'])
        if len(open_candidates) > opener_count:
            do_for = len(open_candidates) - opener_count
            while do_for > 0:
                random_selection = random.randint(0, (len(open_candidates)) - 1)
                del open_candidates[random_selection]
                do_for -= 1
        else:
            print('Insufficient number of employees available to open on', day)
        go_for = len(open_candidates)
        while go_for > 0:
            opener_addition = open_candidates[go_for - 1]
            openers.append([opener_addition, params[day]['open_time']])
            go_for -= 1
        print(openers)
        # while opener_count > 0:
        #     random_selection = random.randint(0, (len(open_candidates)) - 1)
        #     opener_addition = open_candidates.pop(random_selection)
        #     openers.append([opener_addition, params[day]['open_time']])
        #     opener_count -= 1
        #     if len(openers) == int(params[day]['open_ppl']):
        #         opener_count = -1
        #     elif len(open_candidates) == 0:
        #         print('Insufficient number of employees available to open on', day)
        #         opener_count = 0
        try:
            morn_candidates = int(params[day][2])
            for candidate in morn_candidates:
                if candidate in openers:
                    morn_candidates.remove(candidate)
            for m in params[day]['excess_morn_data']:
                start = m[0]
                morn_count = int(m[1])
                while morn_count > 0:
                    random_selection = random.randint(0, (len(morn_candidates) - 1))
                    morn_addition = morn_candidates.pop(random_selection)
                    morning_ppl.append([morn_addition, start])
                    if len(morn_candidates) == 0:
                        print('Insufficient number of employees available to work on', day, 'morning.')
                        morn_count = 0         
        except:
            pass

        try:
            swing_candidates = openers + morning_ppl
            for swinger in swing_candidates:
                if swinger not in availables[day][3]:
                    swing_candidates.remove(swinger)
            morn_to_swing_count = int(params[day]['swing_morn_count'])
            while morn_to_swing_count > 0:
                random_selection = random.randint(0, (len(swing_candidates) - 1))
                swing_addition = swing_candidates.pop(random_selection)
                through_swing.append([swing_addition, params[day]['swing_start']])
                morn_swingers.append(swing_addition)  
        except:
            pass

        
        morn_end = params[day]['morn_end']
        try:
            swinger_end = params[day]['swing_end']
        except:
            pass
        Formatting_Data_1[day] = dict()
        for person in openers:
            if person[0] in through_swing:
                scheduled_output = str(person[1]) + '-' + str(swinger_end)
            else:
                scheduled_output = str(person[1]) + '-' + str(morn_end)
            Formatting_Data_1[day][person[0]] = scheduled_output
        for person in morning_ppl:
            if person[0] in through_swing:
                scheduled_output = str(person[1]) + '-' + str(swinger_end)
            else:
                scheduled_output = str(person[1]) + '-' + str(morn_end)
            Formatting_Data_1[day][person[0]] = scheduled_output
    return(Formatting_Data_1)


Formatting_Data_2 = dict()
def Night_Assignments(params, availables):
    night_ppl = []
    swing_starters = []
    for day in params:
        night_candidates = availables[day][4]
        night_count = int(params[day]['night_count'])
        while (night_count > 0) and (len(night_candidates) > 0):
            random_selection = (random.randint(0, (len(night_candidates)))) - 1
            night_addition = night_candidates.pop(random_selection)
            night_ppl.append(night_addition)
            night_count -= 1
            if len(night_ppl) == int(params[day]['night_count']):
                night_count = -1
            elif len(night_ppl) == 0:
                print('Insufficient number of employees available to work on the afternoon/night of', day)
                night_ppl = 0
        try:
            swing_candidates = night_ppl[:]
            for swinger in swing_candidates:
                if swinger not in availables[day][3]:
                    swing_candidates.remove(swinger)
                if swinger in morn_swingers:
                    swing_candidates.remove(swinger)
            swing_to_night_count = int(params[day]['swing_start_count'])
            while (swing_to_night_count > 0) and (len(swing_candidates) > 0):
                random_selection = (random.randint(0, (len(swing_candidates)))) - 1
                swing_addition = swing_candidates.pop(random_selection)
                swing_starters.append(swing_addition)
                swing_to_night_count -= 1
            swing_start_time = params[day]['swing_start']
        except:
            pass
            
        night_start_time = params[day]['night_start']

        for person in night_ppl:
            if person in swing_starters:
                scheduled_output = str(swing_start_time)
            else:
                scheduled_output = str(night_start_time)
            Formatting_Data_2[day] = {person: scheduled_output}
    return(Formatting_Data_2)




def Generate():
    victims = []
    dates = dict()
    year = input('Please complete the current year: 20')
    scheduled_position = input('Please enter the position you would like to create the schedule for: ')
    validity = False
    while validity == False: #ensures the entered position actually exists so the program doesn't crash (yippee)
        if scheduled_position not in Positions:
            print('The position you entered is not contained in Positions.txt. Try again:')
            scheduled_position = input('Please enter the position you would like to create the schedule for: ')
        else: 
            validity = True
    schedule_parameters = Recall_Parameters(scheduled_position)
    print('(Yes this does mean the program will no longer work at the turn of the century)')
    dates['mon'] = '02/03' #input("please enter monday's date in MM/DD format for the schedule: ")
    dates['tue'] = '02/04' #input("please enter tuesday's date in MM/DD format for the schedule: ")
    dates['wed'] = '02/05' #input("please enter wednesday's date in MM/DD format for the schedule: ")
    dates['thu'] = '02/06' #input("please enter thursday's date in MM/DD format for the schedule: ")
    dates['fri'] = '02/07' #input("please enter friday's date in MM/DD format for the schedule: ")
    dates['sat'] = '02/08' #input("please enter saturday's date in MM/DD format for the schedule: ")
    dates['sun'] = '02/09' #'input("please enter sunday's date in MM/DD format for the schedule: ")
    dow = {1: 'mon', 2: 'tue', 3: 'wed', 4: 'thu', 5: 'fri', 6: 'sat', 7: 'sun'}
    increment = 1
    week_availabilities = dict()
    for E in Employee_names:
        if Employees[E]['title'] == scheduled_position:
            victims.append(E)
    for d in dates:
        date = str(d) + '/' + year
        day = dow[increment]
        week_availabilities[day] = Day_Assign(date, day, victims)
        increment += 1
    morning_assigns = Morning_Assignments(schedule_parameters, week_availabilities)
    night_assigns = Night_Assignments(schedule_parameters, week_availabilities)
    header = ' ' * 11 + f"|   monday  {str(dates['mon']):^12}||  tuesday  {str(dates['tue']):^12}|| wednesday {str(dates['wed']):^12}||  thursday {str(dates['thu']):^12}||   friday  {str(dates['fri']):^12}||  saturday {str(dates['sat']):^12}||   sunday  {str(dates['sun']):^12}||\n"
    formatted_shift_assignments = dict()
    for v in victims:
        str_to_write = ''
        day = 1
        while day <= 7:
            try:
                print(morning_assigns[dow[day]][v])
                str_to_write += f'{morning_assigns[dow[day]][v]:^11}' + '|'
            except:
                str_to_write += ' ' * 11 + '|'
            try:
                str_to_write += f'{night_assigns[dow[day]][v]:^11}' + '||'
            except:
                str_to_write += ' ' * 11 + '||'
            day += 1
            print('day: ', day, end = ' ')
        formatted_shift_assignments[v] = str_to_write
    strings_to_write = [header]
    for person in victims:
        strings_to_write.append(f'{person:^11}' + '|' + formatted_shift_assignments[person] + '\n')
    file_to_open = str(scheduled_position) + '_schedule_' + str(dates['mon'] + '-' + str(dates['sun'])) + '.txt'

    #os.makedirs(os.schedules(file_to_open), exists_ok=True)
    EL_FINAL = open("balls.txt", "w")
    EL_FINAL.writelines(strings_to_write)
    EL_FINAL.close()
    









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
        Parameters = dict()
        for r in raw_data:

            #setup stuff:
            setup = r.split('   ')
            data = setup[1].split(';')

            #open stuff:
            open_stuff = data[0].split('-')
            open_data = open_stuff[1].split(' ')

            open_time = open_data[0]
            open_ppl = open_data[1]

            #morning stuff:
            if len(data[1]) > 11:
                morn_stuff = data[1].split('-')
                morn_stripped = morn_stuff[1].strip()
                morn_split = morn_stripped.split(' ')
                x = len(morn_split)
                morn_info = []
                while x > 1:
                    morn_info.append([morn_split[0], morn_split[1]])
                    del morn_split[1]
                    del morn_split[0]
                    x -= 2

            morn_end_setup = data[2].split('-')
            morn_end = morn_end_setup[1]

            #swing stuff:
            try:
                swing_stuff = data[3].split('-')

                swing_night_stuff = swing_stuff[1].split(' ')
                swing_night_start = swing_night_stuff[0]
                swing_night_count = swing_night_stuff[1]

                swing_morning_stuff = swing_stuff[2].split(' ')
                swing_morn_end = swing_morning_stuff[0]
                swing_morn_count = swing_morning_stuff[1]
            except: 
                print('swing data for', setup[0], 'could not be extracted')

            #night stuff:
            night_stuff = data[4].split('-')
            night_data = night_stuff[1].split(' ')

            night_start = night_data[0]
            night_count = night_data[1].strip()

            #formatting to return schedule information:
            Parameters[setup[0]] = {
                'open_time': open_time, 
                'open_ppl': open_ppl,  
                'morn_end': morn_end, 
                'night_start': night_start,
                'night_count': night_count
            }
            try:
                Parameters[setup[0]]['excess_morn_data'] = morn_info
            except:
                pass
            try: #swing things must be made conditionals
                if swing_night_start == '':
                    raise
                Parameters[setup[0]]['swing_start'] = swing_night_start
                Parameters[setup[0]]['swing_start_count'] = swing_night_count
                Parameters[setup[0]]['swing_end'] = swing_morn_end
                Parameters[setup[0]]['swing_morn_count'] = swing_morn_count
            except:
                pass
    except:
        print('An error occurred extracting the Shift_Data file for', position)
    return(Parameters)



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
        print("\nThanks and gig 'em!\n")
