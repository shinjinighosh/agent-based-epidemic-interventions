from mesa import Agent, Model

class CoronaAgent(Agent):
    """An agent with initial level of infection."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.level_of_infection = 0

class CoronaModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        # Create agents
        for i in range(self.num_agents):
            a = CoronaAgent(i, self)
