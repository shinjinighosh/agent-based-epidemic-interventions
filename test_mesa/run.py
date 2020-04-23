#!/usr/bin/env python3

from CoronaModel import CoronaModel
import matplotlib.pyplot as plt

test_model = CoronaModel(10)

for i in range(10):
    print('\nstep', i, end='\t')
    test_model.step()

agent_infection_level = [a.level_of_infection for a in test_model.schedule.agents]
plt.hist(agent_infection_level)
plt.show()
