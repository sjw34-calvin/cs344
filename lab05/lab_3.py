'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: Sameer Mall
@professor: kvanderlinden
@version Jan 2, 2013
'''

from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])


# a. Implement this network shown and use it to compute the following probabilities:
#
#     P(Raise | sunny)
print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())
# output = False: 0.99, True: 0.01
# Computed by hand:
# P(R | s) = < 0.01, 0.99> These are independent events so the probability is the same as just the probability
# of getting a raise

#     P(Raise | happy ∧ sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happiness).show_approx())
# output = False: 0.986, True: 0.0142
# Computed by hand:
# P(R | h and s)
# = alpha P(R, h, s)
# = alpha P(h | R and s) * P(s) * P(R)
# = alpha <P(h | R and s) * P(s) * p(R), P(h |not R and s) * P(s) * p(not R)>
# = alpha < 1.0 * 0.7 * 0.01, 0.7 * 0.7 * 0.99 >
# = < 0.0142, 0.986 >
# These probabilities makes sense because sunny and raise are independent events
# when you factor in it being sunny and happy which are both positive things the probability increases a lot

# b.
# i. P(Raise | happy)
print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())
# output: False: 0.982, True: 0.0185
# ii P(Raise | happy and not sunny)
print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())
# output: False: 0.917, True: 0.0833
# Do these results make sense to you? Why or why not? We leave working these problems out by hand as an optional exercise.

# These results make sense because raise and sunny are independent events so it being sunny does not really affect you
# getting a raise or not





