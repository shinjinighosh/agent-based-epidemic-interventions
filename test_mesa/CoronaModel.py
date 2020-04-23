from mesa import Agent, Model
from mesa.time import RandomActivation

class CoronaAgent(Agent):
    """An agent with initial level of infection."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.level_of_infection = 0

    def step(self):
        # The agent's step will go here.
        pass

class CoronaModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = CoronaAgent(i, self)
            self.schedule.add(a)

    def step(self):
        '''Advance the model by one step.'''
        self.schedule.step()
