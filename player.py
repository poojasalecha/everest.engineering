from abc import ABC as AbstractBaseClass
from probability import Probability

class Player(AbstractBaseClass):
    
    """ asbtract base class """

    def __init__(self, name, team , probability ,date_of_birth = None,
                role = None, matches_played = None,
                runs_scored = None, balls_faced = None,
                batting_average = None, strike_rate = None,
                highest_score = None, wickets_taken = None,
                balls_bowled = None, bowling_average = None):

        self.name = name
        self.team = team
        self.date_of_birth = date_of_birth
        self.role = role
        self.matches_played = matches_played
        self.runs_scored = runs_scored
        self.balls_faced = balls_bowled
        self.batting_average = batting_average
        self.strike_rate = strike_rate
        self.highest_score = highest_score
        self.wickets_taken = wickets_taken
        self.balls_bowled = balls_bowled
        self.bowling_average = bowling_average
        self.probability = Probability(probability).get_probability()
        self.current_match_run = 0
        self.balls_faced = 0
        self.is_out = False
        self.came_to_bat = False
        super().__init__()


    def get_name(self):
        pass

    def get_team_name(self):
        pass
    
    def get_probability(self):
        pass


class Batsman(Player):

    """ batsman class overrides player class """

    def get_name(self):
        return self.name
    
    def get_team_name(self):
        return self.team.get_name()

    def get_probability(self):
        return self.probability
    








    
        