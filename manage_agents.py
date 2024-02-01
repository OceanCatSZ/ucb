from agent import agent_object
import math

# agents dict a dictionary containing the agent name and connected agents
def execute_agents(agents_dict, arms, total_time):

    agents_list = []

    for agent_name in agents_dict:
        agent_obj = agent_object()
        cur_agent_num = len(agents_list) + 1

        subset_beginning_index = ((cur_agent_num - 1) * math.ceil(len(arms) / len(agents_dict))) % len(arms)

        subset_ending_index = (cur_agent_num * math.ceil(len(arms) / len(agents_dict)) - 1) % len(arms)

        cur_agent_arm_subset = arms[subset_beginning_index : subset_ending_index + 1]

        arm_indices = [i for i in range(subset_beginning_index, subset_ending_index + 1)]

        agent_obj.initialize_agent(cur_agent_arm_subset, agent_name, agents_dict[agent_name])

        agents_list.extend([agent_obj])


    current_epoch_length = 1

    time_remaining = total_time - current_epoch_length >= 0

    current_recommended_arms = []

    while time_remaining:

        cur_epoch_recommended_arms = []

        time_remaining = total_time - current_epoch_length >= 0

        for agent in agents_list:
            best_arm = \
                agent.execute_epoch(current_recommended_arms, current_epoch_length)
            cur_epoch_recommended_arms.extend([best_arm])

        current_recommended_arms = cur_epoch_recommended_arms

        total_time -= current_epoch_length

        current_epoch_length *= 2








    test = 2
