import sys

from match import Match
from team import Team
from player import Batsman


def get_players_probability():
    """ players probability """
    return {
        'Kirat Boli': { '0':5, '1':30, '2':25, '3':10, '4':15, '5':1 ,'6':9,'out':5 },
        'N.S Nodhi': { '0':10, '1':40, '2':20, '3':5, '4':10, '5':1, '6':4, 'out':10 },
        'R Rumrah': { '0':20, '1':30, '2':15, '3':5, '4':5, '5':1, '6':4, 'out':20 },
        'Shashi Henra': { '0':30, '1':25, '2':5, '3':0, '4':5, '5':1, '6':4, 'out':30 }
    }

def get_inputs():
    """ take inputs from the user """ 
    team_1 = str(input("Enter Batting Team: "))
    team_2 = str(input("Enter Bowling Team: "))
    no_of_balls = input("Enter No of Balls: ")
    no_of_wickets = input("Enter no of wickets: ")
    runs_to_win = input("Enter runs to win: ")

    return team_1, team_2, no_of_balls, no_of_wickets, runs_to_win

def create_team(team, is_batting=True):
    return Team(team, is_batting)

def create_batsman(player_name, team, probability):
    return Batsman(player_name, team, probability)


def validation(team_1, team_2, no_of_balls, no_of_wickets, runs_to_win):

    """ validation of team name, balls, wickets and runs to win """
    if team_1 == team_2:
        return "Both teams can't be of same name"
    try:
        no_of_balls = int(no_of_balls)
    except Exception:
        return "no of balls should be an integer"

    try:
        no_of_wickets = int(no_of_wickets)
    except Exception as e:
        return "no of wickets should be an integer"

    try:
        runs_to_win = int(runs_to_win)
    except Exception as e:
        return "no of runs should be an integer"

def main(team_1, team_2, no_of_balls, no_of_wickets, runs_to_win):
    
    """ main func """
    val = validation(team_1, team_2, no_of_balls, no_of_wickets, runs_to_win)
    if val:
        return val

    no_of_balls = int(no_of_balls)
    no_of_wickets = int(no_of_wickets)
    runs_to_win = int(runs_to_win)

    team_1 = create_team(team_1, True)
    team_2 = create_team(team_2, False)
    
    players_probability = get_players_probability()

    player_1 = create_batsman("Kirat Boli", team_1, players_probability["Kirat Boli"])
    player_1.came_to_bat = True

    player_2 = create_batsman("N.S Nodhi", team_1, players_probability["N.S Nodhi"])
    player_2.came_to_bat = True

    player_3 = create_batsman("R Rumrah", team_1, players_probability["R Rumrah"])
    player_4 = create_batsman("Shashi Henra", team_1, players_probability["Shashi Henra"])

    striker = player_1
    non_striker = player_2
    rest_players = [player_3, player_4]

    match = Match(no_of_balls, no_of_wickets, runs_to_win, team_1, team_2, striker, non_striker, rest_players)

    output = match.main()
    return output

    

if __name__ == "__main__":

    """ calling the main func """
    team_1, team_2, no_of_balls, no_of_wickets, runs_to_win = get_inputs()
    results = main(team_1, team_2, no_of_balls, no_of_wickets, runs_to_win)
    for result in results:
        print (result)
