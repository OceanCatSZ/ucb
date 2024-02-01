from scipy import stats
from arm import arm
from manage_agents import execute_agents

if __name__ == '__main__':
    arm_1 = arm()
    arm_2 = arm()
    arm_3 = arm()
    arm_4 = arm()
    arm_5 = arm()
    arm_6 = arm()
    arm_7 = arm()
    arm_8 = arm()
    arm_9 = arm()
    arm_10 = arm()
    arm_11 = arm()
    arm_12 = arm()
    arm_13 = arm()
    arm_14 = arm()
    arm_15 = arm()

    data_normal = stats.norm.rvs(size=10000, loc=0, scale=1)
    arm_1.initialize_arm(data_normal)
    data_normal_2 = stats.norm.rvs(size=10000, loc=5, scale=1)
    arm_2.initialize_arm(data_normal_2)
    data_normal_3 = stats.norm.rvs(size=10000, loc=-5, scale=1)
    arm_3.initialize_arm(data_normal_3)
    data_normal_4 = stats.norm.rvs(size=10000, loc=-10, scale=1)
    arm_4.initialize_arm(data_normal_4)
    data_normal_5 = stats.norm.rvs(size=10000, loc=0, scale=1)
    arm_5.initialize_arm(data_normal_5)
    data_normal_6 = stats.norm.rvs(size=10000, loc=100, scale=1)
    arm_6.initialize_arm(data_normal_6)
    data_normal_7 = stats.norm.rvs(size=10000, loc=-100, scale=1)
    arm_7.initialize_arm(data_normal_7)
    data_normal_8 = stats.norm.rvs(size=10000, loc=0, scale=1)
    arm_8.initialize_arm(data_normal_8)
    data_normal_9 = stats.norm.rvs(size=10000, loc=0, scale=1)
    arm_9.initialize_arm(data_normal_9)
    data_normal_10 = stats.norm.rvs(size=10000, loc=-100, scale=1)
    arm_10.initialize_arm(data_normal_10)
    data_normal_11 = stats.norm.rvs(size=10000, loc=-100, scale=1)
    arm_11.initialize_arm(data_normal_11)
    data_normal_12 = stats.norm.rvs(size=10000, loc=0, scale=1)
    arm_12.initialize_arm(data_normal_12)
    data_normal_13 = stats.norm.rvs(size=10000, loc=0, scale=1)
    arm_13.initialize_arm(data_normal_13)
    data_normal_14 = stats.norm.rvs(size=10000, loc=0, scale=1)
    arm_14.initialize_arm(data_normal_14)
    data_normal_15 = stats.norm.rvs(size=10000, loc=0, scale=1)
    arm_15.initialize_arm(data_normal_15
                          )
    arms = [arm_1, arm_2, arm_3, arm_4, arm_5,
            arm_6, arm_7, arm_8, arm_9, arm_10,
            arm_11, arm_12, arm_13, arm_14, arm_15]

    for i in range(0, len(arms)):
        arms[i].index = i

    agents = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}

    test_set_1 = [1, 2, 3]
    test_set_2 = [2, 4]

    test_set_1.extend(test_set_2)

    test_set_3 = list(set(test_set_1))

    execute_agents(agents, arms, 4096)

    test = 2