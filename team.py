
class Team:
    
    """ team class
    @params 
        name
        isBatting
    """
    def __init__(self, name, is_batting = False):
        self.name = name
        self.is_batting = is_batting
        super().__init__()
    
    def get_name(self):
        return self.name
    
    def is_batting(self):
        return self.is_batting



