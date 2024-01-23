from ucb_algo import ucb

def test_algorithm(ucb, arms, num_sims, steps):
    # arms are distrubutions, generating random numbers
    
    chosen_arms = [[0.0] * steps] * num_sims
    rewards = [[0.0] * steps] * num_sims
    cumulative_rewards = [[0.0] * steps] * num_sims
    sim_nums = [[0.0] * steps] * num_sims
    times = [[0.0] * steps] * num_sims
    
    for sim in range(num_sims):
        ucb.initialize(len(arms))
        
        for index in range(steps):
            sim_nums[sim][index] = sim
            times[sim][index] = index
            
            # Selection of best arm
            chosen_arm = ucb.bestarm()
            chosen_arms[sim][index] = chosen_arm
            
            # Engage chosen the best Arm and obtain reward info
            reward = arms[chosen_arm].calculate()
            rewards[sim][index] = reward
            
            if index == 0:
                cumulative_rewards[sim][index] = reward
            else:
                cumulative_rewards[sim][index] = cumulative_rewards[sim][index - 1] + reward
                
            ucb.update(chosen_arm, reward)
    
    return [sim_nums, times, chosen_arms, rewards, cumulative_rewards]