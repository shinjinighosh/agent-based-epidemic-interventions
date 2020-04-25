#!/usr/bin/env python3

# stdlib
import random

# mesa stuff
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid

# local imports
import simstats


class Person(Agent):
    """An agent with initial level of infection."""

    sex = None
    age = None
    pos = None

    status = 0  # healthy, infected, immune, dead
    infectivity = None
    level_of_infection = None
    days = 0

    def __init__(self, unique_id, model, infectivity=0, level_of_infection=0):
        super().__init__(unique_id, model)

        self.neighborhood = model

        self.infectivity = infectivity
        self.level_of_infection = level_of_infection
        self.update()
        print(self, level_of_infection, self.level_of_infection)

    def __str__(self):
        self.update()
        s = '\tPerson'
        s += str(self.unique_id) + '; status: ' + [
            'healthy',
            'infected',
            'immune',
            'dead'
        ][self.status]

        return s

    def good(self):
        """ is good? """
        return self.status in {0, 2}

    def step(self):
        """ move forward a timestep """
        self.move()
        self.interact()
        # other_agent = self.random.choice(self.model.schedule.agents)
        # other_agent.level_of_infection += random.random() * self.level_of_infection
        # self.level_of_infection += random.random() * self.level_of_infection
        # print(self.unique_id, "%.3f" % self.level_of_infection, end=';\t')

    def move(self):
        if self.status == 3: return # because dead people do not move
        if self.status == 1: self.days += 1

        possible_steps = self.neighborhood.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=True,
        )
        new_position = self.random.choice(possible_steps)
        self.neighborhood.move_agent(self, new_position)

    def interact(self, other=None):
        """interact with people close to this person"""
        # neighbors = self.model.grid.get_cell_list_contents([self.pos])
        neighbors = self.neighborhood.get_neighbors(self)

        if other: neighbors = [other]
        for other in neighbors:
            # other = random.choice(neighbors)
            print(self.unique_id, 'interacts with', other.unique_id)
            other.level_of_infection += random.random() * self.level_of_infection

            self.update()
            other.update()

    def update(self):
        """ update status and params """

        if self.status in [2, 3]: return # because infected or dead people stay as they are

        self.status = 0 if self.level_of_infection == 0 else 1

        today = simstats.recover_or_die(self)  # returns 0, 1 or 2
        self.status += today

        if self.good(): self.level_of_infection = 0

        return self.status
