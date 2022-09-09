import os
import csv_reader
import sys

TOP_FOR_RANKED_SONGS = 5
TOP_FOR_WEEK_ON_BOARD = 10

def clear_terminal():
    os.system('cls')

# return to menu based on a keyboard input
def return_menu(__func,args=False):
    return_menu = input("Do you want to return menu?[Y/N]: ")
    if return_menu == "Y" or return_menu == "y" or return_menu == "yes":
        print_menu()
    elif return_menu == "N" or return_menu == "n" or return_menu == "no":
        if not args:
            __func(args)
        else:
            __func(args)
    else:
        clear_terminal()
        print('\x1b[0;39;43m' + 'OOPS! Invalid input' + '\x1b[0m')
        if not args:
            __func(True)
        else:
            __func(args,True)

# get the rank of the songs list
def get_rank(song):
    rank = int(song[1])
    return rank


# display top ranked song of a give day
def top_ranked(date=False,no_clear_terminal=False):
    if not no_clear_terminal:
        clear_terminal()
    print("Top Ranked Songs")
    print("---------------")
    print('')
    if not date:
        date = input('Enter the required date (e.g:- 2021-11-06): ')
    else:
        print('Enter the required date (e.g:- 2021-11-06):', date)
    songs = csv_reader.get_song_detail_by_date(date)
    songs.sort(key=get_rank)
    for song in songs[0:TOP_FOR_RANKED_SONGS]:
        print(song)
    return_menu(top_ranked,date)

def catch_unique(list_in):
   # intilize an empty list
   unq_list = []

   # Check for elements
   for x in list_in:
      # check if exists in unq_list
      if x not in unq_list:
         unq_list.append(x)
         # print list
   return unq_list
    
def top_artist(no_clear_terminal=False):
    if not no_clear_terminal:
        clear_terminal()
    print("Top Artists")
    print("---------------")
    print('')
    artists = csv_reader.get_song_detail_by_rank("1")
    artists_list = []
    for artist in artists:
        # print(artist)
        artists_list.append(artist[3])

    # get distict artists list
    set_res = set(artists_list)
    list_res = (list(set_res))
    print(list_res)
    return_menu(top_artist)

# get the week on board of the songs list
def get_week_on_board(song):
    week_on_board = int(song[6])
    return week_on_board

def top_weekon_board(no_clear_terminal=False):
    if not no_clear_terminal:
        clear_terminal()
    print("Top 10 Week On Board")
    print("---------------")
    print('')
    songs = csv_reader.get_all_songs()
    songs.sort(key=get_week_on_board)
    for song in songs[0:TOP_FOR_WEEK_ON_BOARD]:
        print(song)
    return_menu(top_weekon_board)

    


# print menu
def print_menu(no_clear_terminal=False):
    if not no_clear_terminal:
        clear_terminal()
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
        top_artist()
    elif op == '3':
        top_weekon_board()
    elif op == '4':
        pass
    elif op == '5':
        sys.exit()
    else:
        clear_terminal()
        print('\x1b[0;39;43m' + 'OOPS! Invalid input' + '\x1b[0m')
        op = print_menu(no_clear_terminal=True)

print_menu()
