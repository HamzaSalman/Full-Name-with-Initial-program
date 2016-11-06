# Created by: Hamza Salman
# Created on: Novembor 2016
# Created for: ICS3U
# This program is a full name program.

def print_name(first, initial = ' ', last = ' '):
    
    if initial == ' ':
        print(first + ' ' + last)
    else:
        print(first + ' ' + ' ' + last)
        
first_name = raw_input('Enter your first name: ')
last_name = raw_input('Enter your last name: ')
initial_choice = raw_input('do you want to enter your initials? (y/n): ')
if initial_choice == 'y':
    initial_name = raw_input('Enter your initials: ')
    print_name(first_name, initial = initial_name, last = last_name)
else:
    print_name(first_name, last = last_name)

