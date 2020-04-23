#!/usr/bin/env python3

from mesa import Agent, Model
from mesa.time import RandomActivation
import random

class CoronaAgent(Agent):
    """An agent with initial level of infection."""
    def __init__(self, unique_id, model, level_of_infection = 0):
        super().__init__(unique_id, model)
        self.level_of_infection = level_of_infection

    def step(self):
        if self.level_of_infection == 0:
            return
        other_agent = self.random.choice(self.model.schedule.agents)
        other_agent.level_of_infection += random.random() * self.level_of_infection
        # self.level_of_infection += random.random() * self.level_of_infection
        # print(self.unique_id, "%.3f" % self.level_of_infection, end=';\t')

class CoronaModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        random_choice = random.choice(range(N))
        # Create agents
        for i in range(self.num_agents):
            a = CoronaAgent(i, self, level_of_infection = int(random_choice == i))
            self.schedule.add(a)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
