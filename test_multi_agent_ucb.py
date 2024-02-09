import random

import numpy as np

from scipy import stats
from arm import arm
from manage_agents import execute_agents

np.random.seed(seed=200)

random.seed(20)

if __name__ == '__main__':
    # arm_1 = arm()
    # arm_2 = arm()
    # arm_3 = arm()
    # arm_4 = arm()
    # arm_5 = arm()
    # arm_6 = arm()
    # arm_7 = arm()
    # arm_8 = arm()
    # arm_9 = arm()
    # arm_10 = arm()
    # arm_11 = arm()
    # arm_12 = arm()
    # arm_13 = arm()
    # arm_14 = arm()
    # arm_15 = arm()

    # data_normal = stats.norm.rvs(size=10000, loc=0, scale=1)
    # arm_1.initialize_arm(data_normal, 0)
    # data_normal_2 = stats.norm.rvs(size=10000, loc=5, scale=1)
    # arm_2.initialize_arm(data_normal_2, 5)
    # data_normal_3 = stats.norm.rvs(size=10000, loc=-5, scale=1)
    # arm_3.initialize_arm(data_normal_3, -5)
    # data_normal_4 = stats.norm.rvs(size=10000, loc=-10, scale=1)
    # arm_4.initialize_arm(data_normal_4, -10)
    # data_normal_5 = stats.norm.rvs(size=10000, loc=0, scale=1)
    # arm_5.initialize_arm(data_normal_5, 0)
    # data_normal_6 = stats.norm.rvs(size=10000, loc=100, scale=1)
    # arm_6.initialize_arm(data_normal_6, 100)
    # data_normal_7 = stats.norm.rvs(size=10000, loc=-100, scale=1)
    # arm_7.initialize_arm(data_normal_7, -100)
    # data_normal_8 = stats.norm.rvs(size=10000, loc=0, scale=1)
    # arm_8.initialize_arm(data_normal_8, 0)
    # data_normal_9 = stats.norm.rvs(size=10000, loc=0, scale=1)
    # arm_9.initialize_arm(data_normal_9, 0)
    # data_normal_10 = stats.norm.rvs(size=10000, loc=-100, scale=1)
    # arm_10.initialize_arm(data_normal_10, -100)
    # data_normal_11 = stats.norm.rvs(size=10000, loc=-100, scale=1)
    # arm_11.initialize_arm(data_normal_11, -100)
    # data_normal_12 = stats.norm.rvs(size=10000, loc=0, scale=1)
    # arm_12.initialize_arm(data_normal_12, 0)
    # data_normal_13 = stats.norm.rvs(size=10000, loc=0, scale=1)
    # arm_13.initialize_arm(data_normal_13, 0)
    # data_normal_14 = stats.norm.rvs(size=10000, loc=0, scale=1)
    # arm_14.initialize_arm(data_normal_14, 0)
    # data_normal_15 = stats.norm.rvs(size=10000, loc=0, scale=1)
    # arm_15.initialize_arm(data_normal_15, 0)

    # arms = [arm_1, arm_2, arm_3, arm_4, arm_5,
    #         arm_6, arm_7, arm_8, arm_9, arm_10,
    #         arm_11, arm_12, arm_13, arm_14, arm_15]

    arms = []
    for i in range(0, 50):
        bernoulli_param = random.random()
        data_bernoulli = stats.bernoulli.rvs(bernoulli_param, size=1000, loc=0)
        cur_arm = arm()
        cur_arm.initialize_arm(data_bernoulli, bernoulli_param * len(data_bernoulli))
        arms.extend([cur_arm])

    for i in range(0, len(arms)):
        arms[i].index = i

    agents = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"], "D": [], "E": [],
              "F": [], "G": [], "H":[], "I":{}, "J":[]}

    test_set_1 = [1, 2, 3]
    test_set_2 = [2, 4]

    test_set_1.extend(test_set_2)

    test_set_3 = list(set(test_set_1))

    execute_agents(agents, arms, 511, 1, True)
    #execute_agents(agents, arms, 511, 1, False)

    test = 2