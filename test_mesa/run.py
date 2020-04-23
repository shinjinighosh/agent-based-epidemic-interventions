#!/usr/bin/env python3

from CoronaModel import CoronaModel

test_model = CoronaModel(10)

for i in range(10):
    print('\nstep', i, end='\t')
    test_model.step()
