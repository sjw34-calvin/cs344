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

# From AIMA code (probability.py) - Fig. 14.2 - cancer example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.2})
    ])

# Compute P(Cancer | positive results on both tests)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# Compute P(Cancer | a positive result on test 1, but a negative result on test 2)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

# Do the results make sense? How much effect does one failed test have on the probability of having cancer?

# Explain your answers:
# The probability of having cancer even if both of your tests generate a positive result is quite low. This is because
# the probability of having cancer in the first place is really low at 0.01
# Having one test fail has a great result on the probability of having cancer. It reduces the probability significantly.
# This shows that the tests actually have a significant impact on determining whether one has cancer or not

# work them out by hand.
# P(Cancer|positive results on both tests)
# alpha <P(C) P(t1 = T|C) P(t2 = T|C), P(-C) P(t1 = T|-C) P(t2 = F|-C)>
# alpha <0.01 * 0.9 * 0.9, 0.99 * 0.2 * 0.2>
# alpha <0.0081, 0.0396>
# <0.17, 0.83>
# These answers match the ones that are output by the program

# P(Cancer| a positive result on test 1, but a negative result on test 2)
# alpha <P(C) P(t1 = T|C) P(t2 = F|C), P(-C) P(t1 = F|-C) P(t2 = F|-C)>
# alpha <0.01 * 0.9 * 0.8, 0.99 * 0.2 * 0.8>
# alpha <9*10^4, 0.1584>
# <0.00565, 0.994>
# This aligns with the answer given by the program

