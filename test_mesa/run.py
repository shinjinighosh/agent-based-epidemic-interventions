#!/usr/bin/env python3

from CoronaModel import CoronaModel
import matplotlib.pyplot as plt
import numpy as np

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

grid_model = CoronaModel(50, 10, 10)
for i in range(20):
    print("Step: %d" %(i))
    model.step()

agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()
plt.show()
