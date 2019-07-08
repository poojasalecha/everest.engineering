
class Probability:

    def __init__(self, probability):
        self.probability = probability
    
    def get_probability(self):
        d = {}
        percent = 0
        for key, val in self.probability.items():
            d[key] = [percent, percent+val]
            percent = percent + val
        return d