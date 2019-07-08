from main import main
import sys


def case_1():
    team_1 = "bangalore"
    team_2  = "bangalore"
    no_of_balls = 34
    no_of_wickets = 5
    runs_to_win = 33
    result = main(team_1, team_2, no_of_balls, no_of_wickets, runs_to_win)
    if result != "Both teams can't be of same name":
        sys.exit("Some validation issues in the code!")

def case_2():
    team_1 = "bangalore"
    team_2  = "chennail"
    no_of_balls = 30
    no_of_wickets = 4
    runs_to_win = 33
    result = main(team_1, team_2, no_of_balls, no_of_wickets, runs_to_win)

    if not isinstance(result, list):
        sys.exit("Issues in the code!")


def input_test_cases():
    case_1()
    case_2()
    

if __name__ == "__main__":
    input_test_cases()