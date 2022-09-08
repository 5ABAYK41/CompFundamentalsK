import os
import csv_reader

def clear_terminal():
    os.system('cls')
# display top ranked song of a give day
def top_ranked():
    clear_terminal()
    print("Top ranked song")
    print("---------------")
    print('')
    date = input('Enter the required date (e.g:- 2021-11-06): ')
    csv_reader.get_top_ranked_song(date)

# print menu
def print_menu():
    print("Top in Billboard!")
    print("-----------------")
    print("1. Top ranked song")
    print("2. Artist with the most top ranked song")
    print("3. Songs with the longest number of weeks on the board")
    print("4. Song that has moved the most in ranking on the board")
    print("5. Exit")
    print('')
    # get the option number
    op = input("Enter the number of the option: ")
    if op == '1':
        top_ranked()
    elif op == '2':
        pass
    elif op == '3':
        pass
    elif op == '4':
        pass
    elif op == '5':
        pass
    else:
        clear_terminal()
        print('\x1b[0;39;43m' + 'OOPS! Invalid input' + '\x1b[0m')
        op = print_menu()

print_menu()
