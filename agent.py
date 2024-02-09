import collections
from ucb_algo import ucb


class agent_object():

    def initialize_agent(self, arms, name, neighbor_agents, ideal_reward):
        self.Sn = arms
        self.name = name
        self.chosen_arms = [0 for i in range(0, len(self.Sn))]
        self.neighbor_agents = neighbor_agents
        self.ideal_reward = ideal_reward
        self.cumulative_regret = [0]
        self.cumulative_reward = [0]
        self.this_agent_ucb = ucb([], [])
        self.this_agent_ucb.initialize(len(arms))
        self.previous_counts = []

    def execute_epoch(self, cur_epoch_duration):
        self.previous_counts = self.this_agent_ucb.counts.copy()
        for timestep in range(0, cur_epoch_duration):
            chosen_arm = self.this_agent_ucb.bestarm()
            chosen_arm_reward = self.Sn[chosen_arm].calculate()

            self.cumulative_reward.extend([chosen_arm_reward + self.cumulative_reward[-1]])

            self.chosen_arms[chosen_arm] += 1

            self.cumulative_regret.extend([self.ideal_reward - chosen_arm_reward + self.cumulative_regret[-1]])

            self.this_agent_ucb.update(chosen_arm, chosen_arm_reward)

        x_arm = self.chosen_arms.index(max(self.chosen_arms)) # swap out with other arms
        return x_arm
