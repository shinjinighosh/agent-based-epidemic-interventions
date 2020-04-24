#!/usr/bin/env python3

# stdlib
import random


# mesa stuff
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

from Person import Person


class Neighborhood(Model):
    """A model of a neighborhood with some number of agents."""

    def __init__(self, N=10, width=None, height=None):
        """ Neighborhood: a neighborhood containing people

            Parameters
            ----------
            N:
                number of people in the neighborhood
            width:
                width of the (rectangular) neighborhood area
            height:
                height of the (rectangular) neighborhood area
        """
        super().__init__()
        
        self.num_agents = N
        self.width = width or min(N, 100)
        self.height = height or min(N, 100)

        self.grid = MultiGrid(self.width, self.height, True)
        self.schedule = RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            rand = random.random()
            infection = rand >= (N-N**.5)/N
            print(i, rand, (N-N**.5)/N)

            a = Person(i, self, level_of_infection=int(infection))
            print(a, a.level_of_infection)
            self.schedule.add(a)

            # adding the agent to a random position in the neighborhood
            (x, y) = random.random() * self.width, random.random() * self.height
            self.grid.place_agent(a, (int(x), int(y)))

    def step(self):
        """Advance the model by one step."""

        self.schedule.step()

    def get_neighbors(self, person, radius=1):
        """ get neighbors of person """
        neighbor_objects = self.grid.get_cell_list_contents([person.pos])
        return [*filter(lambda x: type(x) is Person and x is not person, 
                        neighbor_objects)]

    def move_agent(self, *args, **kwargs):
        return self.grid.move_agent(*args, **kwargs)
