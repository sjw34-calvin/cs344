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
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])


# print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# # elimination_ask() is a dynamic programming version of enumeration_ask().
# print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# # gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
# print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# # See the explanation of the algorithms in AIMA Section 14.4.
# # This answer makes sense because if John and Mary both call there is a high chance that there was a burglary

# i. Compute P(Alarm | Burglary and No Earthquake)
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# This one above gives a probability of 0.94 which is pretty straight forward as can be seen in the table
# This one also gives a very high probability which is accurate because if there is a burglary then the alarm should go off

# ii. Compute P(JohnCalls | Burglary and No Earthquake)
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())
# John will call if the alarm has gone off and the probability of burglary is a big factor in setting off the alarm
# so it makes sense john would call even if there was no earthquake

# iii. Compute P(Burglary | alarm)
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())
# Did the above example in class it is the full joint probability distribution
# This returns a small probability of True: 0.374 because there is a higher chance of it being an earthquake than a burglary
#

# iv. Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# This one makes sense that the probability of burglary is small even if both of them actually call because
# the probability of there being a burglary is small