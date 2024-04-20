#CSE 111 Final Project
#Author: Patrick O'Neill; Section 2

import csv # so that we can use data from the csv file 
import matplotlib.pyplot as plt #so that we can create charts based on the data
import numpy as np # so that we can label the charts with numbers 
from collections import Counter # so that we can get the top 5 players for a certain stastic 

PLAYER_NAME_INDEX = 0
REBOUNDS_INDEX = 22
ASSISTS_INDEX = 23
STEALS_INDEX = 24
BLOCKS_INDEX = 25
POINTS_INDEX = 28

def main():
    """
    This is the main function and it calls all the functions that are defined at the bottom of the program
    and it creates 6 different charts that displays data from the top 5 NBA players in 6 different statistical catgories 
    which are: points, rebounds, assists, blocks, steals, and one statistic of the user's choice. 
    """
    print('Welcome to my NBA statistic comparison program')
    print()
    print('In this program, I will display the top 5 players for each of the following stastics:\npoints\nrebounds\nassists\nblocks\nsteals\none stastic of your choice')
    print()
    print('Choose to show results for the top 5 players for one of the following stastics:')
    print()
    while True: 
        try:
            print('press "6" to see top 5 players for minutes per game') #because 6 is the index for minutes per game
            print('press "7" to see top 5 players for field goals made per game') # because 7 is the index for field goals per game
            print('press "10" to see top 5 players for 3pt field goals made per game') # because 10 is the index for 3pt field goals made per game
            print('press "13" to see top 5 players for 2pt field goals made per game') # because 13 is the index for 2pt field goals per game
            print('press "17" to see top 5 players for free throws made per game')# because 17 is the index for free throws made per game
            print('press "26" to see top 5 players for turn overs per game')# because 26 is the index for turnovers made per game 
            print()
            # this allows the user to press a number that represents a stastical category
            # the error handling prevents them from picking any number that's not within the "acceptables" list
            stat_of_choice = int(input('press your choice: '))
            acceptables = [6,7,10,13,17,26]
            if stat_of_choice not in acceptables:
                raise ValueError
            else:
                break
        except ValueError:
            print()
            print('must only press one of the following numbers:')
            print()        
    players_dict = read_dictionary('nba-player-stats-2019.csv',PLAYER_NAME_INDEX) 
    points_dict = create_dict(players_dict,POINTS_INDEX)
    assists_dict = create_dict(players_dict, ASSISTS_INDEX)
    rebounds_dict = create_dict(players_dict, REBOUNDS_INDEX)
    blocks_dict = create_dict(players_dict, BLOCKS_INDEX)
    steals_dict = create_dict(players_dict, STEALS_INDEX)
    stat_of_choice_dict = create_dict(players_dict, stat_of_choice)
    top_5_scorrers = rank(points_dict)
    top_5_passers = rank(assists_dict)
    top_5_rebounders = rank(rebounds_dict)
    top_5_blockers = rank(blocks_dict)
    top_5_stealers = rank(steals_dict)
    top_5_stat_of_choice = rank(stat_of_choice_dict)
    scorrers= keys(top_5_scorrers)
    passers = keys(top_5_passers)
    rebounders = keys(top_5_rebounders)
    blockers = keys(top_5_blockers)
    stealers = keys(top_5_stealers)
    top_5 = keys(top_5_stat_of_choice)

    #displays the chart for top 5 leaders in points per game
    fig, ax = plt.subplots()
    bottom = np.zeros(5)

    players = [
                scorrers[0],scorrers[1],scorrers[2],scorrers[3],scorrers[4]
            ]
    points = [
            top_5_scorrers[scorrers[0]], top_5_scorrers[scorrers[1]], top_5_scorrers[scorrers[2]], 
            top_5_scorrers[scorrers[3]], top_5_scorrers[scorrers[4]]
            ]


    bar_labels = ['red', 'blue', '_red', 'orange', 'green']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:green']

    for point in points:
        p = ax.bar(players, points, label=bar_labels, color=bar_colors)
        bottom += point
        ax.bar_label(p, label_type = 'center')

    ax.set_ylabel('Points per game \n(PPG)')
    ax.set_title('Top scorers in the NBA (2019)')

    plt.show()

    # displays the chart for the top 5 leaders in assists per game 
    fig, ax = plt.subplots()
    bottom = np.zeros(5)

    players = [
            passers[0],passers[1],passers[2],passers[3],passers[4]
            ]
    assists = [
                top_5_passers[passers[0]],top_5_passers[passers[1]], top_5_passers[passers[2]],
                top_5_passers[passers[3]],top_5_passers[passers[4]]
            ]
    bar_labels = ['red', 'blue', '_red', 'orange', 'green']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:green']
    for assist in assists:
        p = ax.bar(players,assists, label = bar_labels, color = bar_colors)
        bottom += assist
        ax.bar_label(p, label_type = 'center')

    ax.set_ylabel('Asists Per Game \n(APG)')
    ax.set_title('Top passers in the NBA (2019)')

    plt.show()

    # displays the chart for the top 5 leaders for rebounds per game
    fig, ax = plt.subplots()
    bottom = np.zeros(5)

    players = [rebounders[0],rebounders[1],rebounders[2], rebounders[3], rebounders[4]]
    rebounds = [
                top_5_rebounders[rebounders[0]],top_5_rebounders[rebounders[1]], top_5_rebounders[rebounders[2]],
                top_5_rebounders[rebounders[3]], top_5_rebounders[rebounders[4]]
            ]
    bar_labels = ['red', 'blue', '_red', 'orange', 'green']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:green']
    for assist in assists:
        p = ax.bar(players,rebounds, label = bar_labels, color = bar_colors)
        bottom += assist
        ax.bar_label(p, label_type = 'center')

    ax.set_ylabel('Rebounds Per Game \n(RPG)')
    ax.set_title('Top Rebounders in the NBA (2019)')

    plt.show()

    # displays the chart for the top 5 leaders in blocks per game 
    fig, ax = plt.subplots()
    bottom = np.zeros(5)

    players = [blockers[0],blockers[1],blockers[2], blockers[3], blockers[4]]
    blocks = [
                top_5_blockers[blockers[0]],top_5_blockers[blockers[1]], top_5_blockers[blockers[2]],
                top_5_blockers[blockers[3]], top_5_blockers[blockers[4]]
            ]
    bar_labels = ['red', 'blue', '_red', 'orange', 'green']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:green']
    for block in blocks:
        p = ax.bar(players,blocks, label = bar_labels, color = bar_colors)
        bottom += block
        ax.bar_label(p, label_type = 'center')

    ax.set_ylabel('Blocks Per Game \n(BPG)')
    ax.set_title('Top Blockers in the NBA (2019)')

    plt.show()

    #  displays the chart for the top 5 leaders in steals per game 
    fig, ax = plt.subplots()
    bottom = np.zeros(5)

    players = [stealers[0],stealers[1],stealers[2], stealers[3], stealers[4]]
    steals = [
                top_5_stealers[stealers[0]],top_5_stealers[stealers[1]], top_5_stealers[stealers[2]],
                top_5_stealers[stealers[3]], top_5_stealers[stealers[4]]
            ]
    bar_labels = ['red', 'blue', '_red', 'orange', 'green']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:green']
    for steal in steals:
        p = ax.bar(players,steals, label = bar_labels, color = bar_colors)
        bottom += steal
        ax.bar_label(p, label_type = 'center')

    ax.set_ylabel('Steals Per Game \n(SPG)')
    ax.set_title('Leaders in Steals in the NBA (2019)')

    plt.show()

    # displays the chart for the top 5 leaders in the stastical category of the user's choosing 
    fig, ax = plt.subplots()
    bottom = np.zeros(5)

    players = [top_5[0], top_5[1], top_5[2], top_5[3], top_5[4]]
    steals = [
                top_5_stat_of_choice[top_5[0]],top_5_stat_of_choice[top_5[1]], top_5_stat_of_choice[top_5[2]],
                top_5_stat_of_choice[top_5[3]], top_5_stat_of_choice[top_5[4]]
            ]
    bar_labels = ['red', 'blue', '_red', 'orange', 'green']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange', 'tab:green']
    for steal in steals:
        p = ax.bar(players,steals, label = bar_labels, color = bar_colors)
        bottom += steal
        ax.bar_label(p, label_type = 'center')

    ax.set_ylabel('Your Statistic of choice')
    ax.set_title('Leaders in NBA (2019)')

    plt.show()

def read_dictionary(filename, key_column_index):
    """
    This function convers a csv file into a dictornary, and the index that 
    you plug into the function will determine the key value of the dictionary
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    with open(filename, 'rt') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            if len(row_list) != 0:
                key = row_list[key_column_index]
                dictionary[key] = row_list
    return dictionary

def create_dict(dictionary, index):
    """
    This function transforms a compound dictionary into a single-item 
    dictionary, so that we're able to compare players based on a statistical  
    category. The item that will be in the new dicitonary is dependant upon the index 
    of the compound dictionary. 
    """
    dict = {}
    for stat,record in dictionary.items():
        stat = float(record[index])
        players= record[0]
        dict[players]= stat
    return dict


def keys(dict):
    """
    This function takes a dictionary and makes a list that contains
    all the keys of that dictonary, so that we can display the neames of the top
    5 players of a stastical category on a chart. 
    """
    dict_list = list(dict.keys())
    return dict_list 

def rank(dictionary):
    """
    This function takes a dictionary created from the create_dict function and 
    converts that dictionary into a smaller dictionary that contains players with 
    with the top 5 values of a certain stastical category. 
    """
    ranking = dict(Counter(dictionary).most_common(5))
    return ranking

# calls the main function so that the program will run 
if __name__ == "__main__":
    main()

