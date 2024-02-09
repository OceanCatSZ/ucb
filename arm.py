import random

random.seed(5)
from scipy import stats

class arm():

    def initialize_arm(self, distribution, mean):
        self.distribution = distribution
        self.mean = mean
        self.index = -1


    def calculate(self):
        def is_one(num):
            return num == 1

        distribution_copy = self.distribution.copy()
        filtered_arr = list(filter(is_one, distribution_copy))
        #return len(filtered_arr) / 1000
        return self.distribution[random.randint(0, len(self.distribution) - 1)]



