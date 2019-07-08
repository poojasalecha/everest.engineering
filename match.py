from team import Team
from player import Player, Batsman
from probability import Probability
from random_generation import RandomProbabilisticGenerator


class Match:
    
    """ match class """
    def __init__(self, no_of_balls,
                    no_of_wickets,
                    runs_to_win,
                    batting_team,
                    bowling_team, 
                    striker,
                    non_striker,
                    rest_players
                    ):
        self.no_of_balls = no_of_balls
        self.balls_left = no_of_balls
        self.no_of_wickets = no_of_wickets
        self.runs_to_win = runs_to_win
        self.batting_team = batting_team
        self.bowling_team = bowling_team
        self.striker = striker
        self.non_striker = non_striker
        self.rest_players = rest_players
        self.players_track = self.track_players_records()
        self.output = ['commentry', '{} overs left. {} runs to win'.format(no_of_balls//6, runs_to_win)]
    

    def main(self):
        while not self.is_game_over():
            """ random probabilistic ball result """ 
            bowl_result = RandomProbabilisticGenerator(self.striker).get_random_generator()
            self.evaulate_result(bowl_result)

        return self.match_result()

        
    def get_random_generator(self):

        """ random value of a ball """
        return RandomProbabilisticGenerator(self.striker).get_random_generator()


    def is_game_over(self):
        if not self.runs_to_win:
            return True
        if self.no_of_wickets == 1:
            return True
        if not self.balls_left:
            return True
        return False
    
    def is_over_completed(self):
        """ is over completed """
        if self.balls_left % 6 == 0:
            return True
        return False
    
    def evaulate_result(self, bowl_result):

        """ evaluate the result of the ball
        @param bowl result
         """
        try:
            bowl_result  = int(bowl_result)
        except:
            pass
        over_no = self.get_over_and_ball_no()
        self.balls_left  = self.balls_left - 1
        striker = self.striker
        striker.balls_faced += 1
        
        if bowl_result == 'out':
            self.player_out_codition(over_no, striker)
        elif (bowl_result == 0) or (bowl_result == 2) or (bowl_result == 4) or (bowl_result == 6):
            self.dot_two_four_or_six(bowl_result, over_no, striker)
        elif (bowl_result == 1) or (bowl_result == 3) or (bowl_result == 5):
            self.one_three_five(bowl_result, over_no, striker)
        
        if self.is_over_completed() and not self.is_game_over():
            self.output.append("{} overs left  {} to win".format((self.no_of_balls - self.balls_left) // 6, self.runs_to_win))

    def player_out_codition(self, over_no, striker):

        """ when player get out """
        self.no_of_wickets -= 1
        if self.no_of_wickets > 1:

            """ changing the striker condtion """
            if self.is_over_completed():
                self.striker = self.non_striker
                self.non_striker = self.next_player()
            else:
                self.striker = self.next_player()
        self.output.append("{} {} {}".format(over_no, striker.get_name(), "out"))
        striker.is_out = True
    
    def dot_two_four_or_six(self, bowl_result, over_no, striker):

        """ when player hits two, four six or play a dot ball"""

        if self.runs_to_win <= bowl_result:
            self.runs_to_win = 0
        else:
            self.runs_to_win -= bowl_result
        if self.is_over_completed():
            self.striker, self.non_striker = self.non_striker, self.striker
        self.commentry(over_no, striker.get_name(), bowl_result)
        striker.current_match_run += bowl_result
    
    def one_three_five(self, bowl_result, over_no, striker):
        """ when player hits one, three or five"""
        if self.runs_to_win <= bowl_result:
            self.runs_to_win = 0
        else:
            self.runs_to_win -= bowl_result
        if not self.is_over_completed():
                self.striker, self.non_striker = self.non_striker, self.striker
        self.commentry(over_no, striker.get_name(), bowl_result)
        striker.current_match_run += bowl_result

    def next_player(self):

        """ next player if someone is out """
        try:
            player = self.rest_players[0]
            player.came_to_bat = True
            self.rest_players.remove(player)
            return player
        except:
            pass
    
    def commentry(self, over_no, player_name, bowl_result):
        self.output.append("{} {} scores {} runs". format(over_no, player_name, bowl_result))

    def get_over_and_ball_no(self):
        bowls_bowled = self.no_of_balls - (self.balls_left-1)
        over_no, ball_no = bowls_bowled // 6, bowls_bowled % 6
        return str(over_no) + "." + str(ball_no)
    
    def match_result(self):
        if self.runs_to_win == 0:
            self.output.insert(0, "{} won by {} wickets and {} balls remaining".format(self.batting_team.get_name(), self.no_of_wickets, self.balls_left))
        else:
            self.output.insert(0, "{} won by {} runs".format(self.bowling_team.get_name(), self.runs_to_win-1))
        
        records = []
        for player in self.players_track:
            if player.came_to_bat:
                if player.is_out:
                    res = "{} - {} ({} balls)".format(player.get_name(),player.current_match_run, player.balls_faced)
                else:
                    res = "{} - {}* ({} balls)".format(player.get_name(), player.current_match_run,player.balls_faced )
                records.append(res)
        records.reverse()
        for record in records:
            self.output.insert(0, record)
        return self.output
    

    def track_players_records(self):

        """ track the player individual record """
        records = []
        records.append(self.striker)
        records.append(self.non_striker)
        for rest_player in self.rest_players:
            records.append(rest_player)
        return records




    

