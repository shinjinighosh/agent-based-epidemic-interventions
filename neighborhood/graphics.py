#!/usr.bin/env python3

from mesa import visualization
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


def agent_repr(agent):
    portrayal = {'Shape': 'circle' if agent.good() else 'circle',
                 'Color': ['blue', 'red', 'green', 'grey'][agent.status],
                 'Filled': "true",
                 'Layer': 0,
                 'r': 0.5}
    return portrayal


def make_canvas(w, h, w_=512, h_=512):
    return CanvasGrid(agent_repr, w, h, w_, h_)
