#!/usr/bin/env python3

# stdlib imports
import matplotlib.pyplot as plt
import numpy as np
from argparse import ArgumentParser

# local imports
from CoronaModel import Neighborhood
from graphics import make_canvas, ModularServer

def simulate(width, height, N):
    """ setup and run simulation """
    canvas = make_canvas(width, height)
    server = ModularServer(Neighborhood, [canvas], 'title',
                           {'N': N,
                            'width': width,
                            'height': height})

    server.port = 8000
    server.launch()


def main(args):
    '''main'''
    simulate(args.width, args.height, args.numpeople)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-n', '--numpeople', type=int, default=10,
                        help='number of agents in the simulation')
    parser.add_argument('--width', type=int, default=10)
    parser.add_argument('--height', type=int, default=10)

    args = parser.parse_args()
    main(args)
