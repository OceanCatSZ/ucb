from numpy import sqrt, log

class ucb():
    def __init__(self, counts, values):
        self.counts = counts
        self.values = values
        return
    
    def initialize(self, arms):
        self.counts = [0 for col in range(arms)]
        self.values = [0 for col in range(arms)]
        return
    
    def bestarm(self):
        numArms = len(self.counts)
        for arms in range(numArms):
            if self.counts[arms] == 0:
                return arms
        
        ucbval = [0 for arm in range(numArms)]
        countTotal = sum(self.counts)
        
        for arms in range(numArms):
            ucbval[arms] = self.values[arms] + sqrt(2 * log(countTotal) / self.counts[arms])
        
        return ucbval.index(max(ucbval))
    
    def update(self, arm, reward):
        self.counts[arm] = self.counts[arm] + 1
        n = self.counts[arm]
        
        value = self.values[arm]
        new_value = ((n - 1) / n) * value + (1 / n) * reward
        self.values[arm] = new_value
        return
