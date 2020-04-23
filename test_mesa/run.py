#!/usr/bin/env python3

from CoronaModel import CoronaModel
import matplotlib.pyplot as plt

# test_model = CoronaModel(10)

# for i in range(10):
    # print('\nstep', i, end='\t')
    # test_model.step()

# agent_infection_level = [a.level_of_infection for a in test_model.schedule.agents]
# plt.hist(agent_infection_level)
# plt.show()

all_infection_levels = []
for j in range(100):
    # Run the model
    model = CoronaModel(10)
    for i in range(10):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        all_infection_levels.append(agent.level_of_infection)

    print("Run: %d" %j, all_infection_levels[-1])

plt.hist(all_infection_levels, bins=range(int(max(all_infection_levels))+1))
plt.show()
