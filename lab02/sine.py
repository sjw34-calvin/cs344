"""
This module implements local search on a simple sine function variant.
The function is a linear function  with a single, discontinuous max value
(see the sine function variant in graphs.py).

@author: sjw34-calvin (sameer mall)
@version 6feb2013
"""
from tools.aima.search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import time
import math


class SinVariant(Problem):
    """
    State: x value for the sine function variant f(x)
    Move: a new x value delta steps from the current x (in both directions)
    """

    def __init__(self, initial, maximum=30.0, delta=1):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta

    def actions(self, state):
        return [state + self.delta, state - self.delta]

    def result(self, stateIgnored, x):
        return x

    def value(self, x):
        return math.fabs(x * math.sin(x))


if __name__ == '__main__':
    # Formulate a problem with a 2D hill function and a single maximum value.
    total_initial_val = 0
    total_hill_val = 0
    total_anneal_val = 0

    for i in range(5):
        maximum = 30
        initial = randrange(0, maximum)
        p = SinVariant(initial, maximum, delta=0.001)
        print('Initial                      x: ' + str(p.initial)
              + '\t\tvalue: ' + str(p.value(initial))
              )
        total_initial_val = total_initial_val + p.value(initial)

        #start = time.time()
        # Solve the problem using hill-climbing.
        hill_solution = hill_climbing(p)
        #end = time.time()
        #print(end - start)
        print('Hill-climbing solution       x: ' + str(hill_solution)
              + '\tvalue: ' + str(p.value(hill_solution))
              )
        total_hill_val = total_hill_val + p.value(hill_solution)

        # Solve the problem using simulated annealing.
        #anneal = time.time()
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        #aneal_end = time.time()
       # print(aneal_end - anneal)
        print('Simulated annealing solution x: ' + str(annealing_solution)
              + '\tvalue: ' + str(p.value(annealing_solution))
              )
        total_anneal_val = total_anneal_val + p.value(annealing_solution)

        print("\n")

    print("Total initial value is: " + str(total_initial_val))
    print("Total hill value is: " + str(total_hill_val))
    print("Total anneal value is: " + str(total_anneal_val))
    print("\n")

    print("Average initial value is: " + str(total_initial_val / 5))
    print("Average hill value is: " + str(total_hill_val / 5))
    print("Average anneal value is: " + str(total_anneal_val / 5))