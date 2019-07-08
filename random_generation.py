class RandomProbabilisticGenerator:
    def __init__(self, player):
        self.player = player
    
    def get_random_generator(self):
        l = [0, 1, 2, 3, 4, 5, 6, 'out']
        import random
        val = random.randint(0, 100)
        for key, value in self.player.probability.items():
            if val >= value[0] and val <= value[1]:
                return key
       