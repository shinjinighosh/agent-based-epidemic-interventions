#!/usr/bin/env python3

from mesa import Agent, Model
from mesa.time import RandomActivation
import random
from mesa.space import MultiGrid

class CoronaAgent(Agent):
    """An agent with initial level of infection."""
    def __init__(self, unique_id, model, level_of_infection = 0):
        super().__init__(unique_id, model)
        self.level_of_infection = level_of_infection

    def step(self):
        self.move()
        if self.level_of_infection == 0:
            return
        else:
            self.give_infection()
        # other_agent = self.random.choice(self.model.schedule.agents)
        # other_agent.level_of_infection += random.random() * self.level_of_infection
        # self.level_of_infection += random.random() * self.level_of_infection
        # print(self.unique_id, "%.3f" % self.level_of_infection, end=';\t')

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
    
    def give_infection(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            other_agent = self.random.choice(cellmates)
            other_agent.level_of_infection += random.random() * self.level_of_infection
            # self.level_of_infection += random.random() * self.level_of_infection

class CoronaModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, width = 10, height = 10):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        self.grid = MultiGrid(width, height, True)
        random_choice = random.choice(range(N))
        # Create agents
        for i in range(self.num_agents):
            a = CoronaAgent(i, self, level_of_infection = int(random_choice == i))
            self.schedule.add(a)

            # adding the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
