#!/usr/bin/env python3

# stdlib imports
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser

# local imports
from CoronaModel import Neighborhood
from graphics import make_canvas, ModularServer

'''
all_infection_levels = []
for j in range(100):
    # Run the model
    model = Neighborhood(10)
    for i in range(10):
        model.step()

    # Store the results
    for agent in model.schedule.agents:
        all_infection_levels.append(agent.level_of_infection)

    print("Run: %d" %j, all_infection_levels[-1])

plt.hist(all_infection_levels, bins=range(int(max(all_infection_levels))+1))
plt.show()

grid_model = Neighborhood(50, 10, 10)
for i in range(20):
    print("step: %d" %(i))
    model.step()

agent_counts = np.zeros((model.grid.width, model.grid.height))
for cell in model.grid.coord_iter():
    cell_content, x, y = cell
    agent_count = len(cell_content)
    agent_counts[x][y] = agent_count
plt.imshow(agent_counts, interpolation='nearest')
plt.colorbar()
plt.show()
'''


def main(args):
    """ main method """
    canvas = make_canvas(args.width, args.height)
    server = ModularServer(Neighborhood, [canvas], 'title',
                           {'N': args.numpeople,
                            'width': args.width,
                            'height': args.height})

    server.port = 8000
    server.launch()


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-n', '--numpeople', type=int, default=10,
                        help='number of agents in the simulation')
    parser.add_argument('--width', type=int, default=10)
    parser.add_argument('--height', type=int, default=10)

    args = parser.parse_args()
    main(args)
