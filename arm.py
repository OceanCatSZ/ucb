import random

from scipy import stats

class arm():

    def initialize_arm(self, distribution):
        self.distribution = distribution
        self.index = -1


    def calculate(self):
        return self.distribution[random.randint(0, len(self.distribution) - 1)]



