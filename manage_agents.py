from agent import agent_object
import math

import matplotlib.pyplot as plt

# agents dict a dictionary containing the agent name and connected agents
def execute_agents(agents_dict, arms, total_time, ideal_reward, communication):

    agents_list = []

    for agent_name in agents_dict:
        agent_obj = agent_object()
        cur_agent_num = len(agents_list) + 1

        subset_beginning_index = ((cur_agent_num - 1) * math.ceil(len(arms) / len(agents_dict))) % len(arms)

        subset_ending_index = (cur_agent_num * math.ceil(len(arms) / len(agents_dict)) - 1) % len(arms)

        # cur_agent_arm_subset = arms[subset_beginning_index : subset_ending_index + 1]

        arms_copy = arms.copy()

        agent_obj.initialize_agent(arms_copy, agent_name, agents_dict[agent_name], ideal_reward)

        agents_list.extend([agent_obj])


    current_epoch_length = min(1, total_time)

    if not communication:
        current_epoch_length = total_time

    time_remaining = total_time - current_epoch_length >= 0

    last_run = not time_remaining

    current_recommended_arms = []

    while time_remaining or last_run:

        cur_values = [0 for i in agents_list[0].this_agent_ucb.values]
        cur_counts = [0 for i in agents_list[0].this_agent_ucb.counts]

        found_arm_indexes = []
        amount_played = []

        for agent in agents_list:
            cur_agent_arm_index = agent.execute_epoch(current_epoch_length)
            found_arm_indexes.extend([found_arm_indexes])
            #update counts like so, update values using formula present in UCB
            # cur_values = [(sum(i) / len(agents_list)) for i in zip(cur_values, agent.this_agent_ucb.values)]
            cur_amount_played = agent.this_agent_ucb.counts[cur_agent_arm_index] - agent.previous_counts[cur_agent_arm_index]
            amount_played.extend([cur_amount_played])

            cur_counts[cur_agent_arm_index] += cur_amount_played

        if communication:
            synched_counts = [x + y for x, y in zip(agents_list[0].previous_counts, cur_counts)]
            for agent in agents_list:

                # agent.this_agent_ucb.counts = cur_counts
                # agent.this_agent_ucb.values = cur_values
                for j in range(0, len(synched_counts)):
                    if synched_counts[j] == 0:
                        continue
                    agent.this_agent_ucb.values[j] = (((synched_counts[j] - 1) / synched_counts[j]) *
                                                               agent.this_agent_ucb.values[j] +
                                                               (1 / synched_counts[j]) * agent.this_agent_ucb.values[j])
                agent.this_agent_ucb.counts = synched_counts


        total_time -= current_epoch_length

        current_epoch_length *= 2

        time_remaining = total_time - current_epoch_length >= 0

        if not time_remaining and total_time > 0:
            last_run = True
            current_epoch_length = total_time
            continue

        if last_run:
            last_run = False

    plt.figure()



    for agent in agents_list:
        # plt.scatter(agent.cumulative_reward, label="Agent " + str(agent.name) + " reward")
        #plt.plot(agent.cumulative_reward, label="Agent " + str(agent.name) + " reward")
        # plt.scatter(agent.cumulative_regret, label="Agent " + str(agent.name) + " regret")
        plt.plot(agent.cumulative_regret, label="Agent " + str(agent.name) + " regret")

    agent_sum_list = []

    for agent in agents_list:
        if agent_sum_list == []:
            agent_sum_list = agent.cumulative_regret
            continue
        agent_sum_list = [sum(i) for i in zip(agent_sum_list, agent.cumulative_regret)]

    plt.plot(agent_sum_list, label="Cumulative Regret")
    plt.legend()
    plt.show()










    test = 2
