import collections
from ucb_algo import ucb


class agent_object():

    def initialize_agent(self, subset, name, neighbor_agents):
        self.Sn = subset
        self.name = name
        self.augmented_set = []
        self.all_indices = []
        self.chosen_arms = []
        self.neighbor_agents = neighbor_agents

    def execute_epoch(self, broadcast_set, cur_epoch_duration):
        self.augmented_set = []
        self.augmented_set.extend(self.Sn)
        self.augmented_set.extend(broadcast_set)
        self.augmented_set = list(set(self.augmented_set))
        this_epoch_ucb = ucb([], [])
        this_epoch_ucb.initialize(len(self.augmented_set))

        self.chosen_arms = [0 for i in range(0, len(self.augmented_set))]

        for timestep in range(0, cur_epoch_duration):
            chosen_arm = this_epoch_ucb.bestarm()
            chosen_arm_reward = self.augmented_set[chosen_arm].calculate()

            self.chosen_arms[chosen_arm] += 1

            this_epoch_ucb.update(chosen_arm, chosen_arm_reward)

        most_played_arm = self.chosen_arms.index(max(self.chosen_arms))

        return self.augmented_set[most_played_arm]
