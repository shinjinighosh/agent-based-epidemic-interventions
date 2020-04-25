#!/usr.bin/env python3

from mesa import visualization
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer, VisualizationElement


def agent_repr(agent):
    portrayal = {'Shape': 'circle' if agent.good() else 'circle',
                 'Color': ['blue', 'red', 'green', 'grey'][agent.status],
                 'Filled': "true",
                 'Layer': 0,
                 'r': 0.5}
    return portrayal


class SimpleCanvas(VisualizationElement):
    local_includes = ["static/simple_continuous_canvas.js"]
    portrayal_method = None
    canvas_height = 500
    canvas_width = 500

    def __init__(self, portrayal_method, w=500, h=500, *args, **kwargs):
        '''
        Instantiate a new SimpleCanvas
        '''
        self.portrayal_method = portrayal_method
        self.canvas_height = h
        self.canvas_width = w
        new_element = ("new Simple_Continuous_Module({}, {})".
                       format(self.canvas_width, self.canvas_height))
        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
        space_state = []
        for obj in model.schedule.agents:
            portrayal = self.portrayal_method(obj)
            x, y = obj.pos
            x = ((x - model.space.x_min) /
                 (model.space.x_max - model.space.x_min))
            y = ((y - model.space.y_min) /
                 (model.space.y_max - model.space.y_min))
            portrayal["x"] = x
            portrayal["y"] = y
            space_state.append(portrayal)
        return space_state
        

def make_canvas(w=512, h=512, w_=512, h_=512):
    return SimpleCanvas(agent_repr, w, h, w_, h_)
 
