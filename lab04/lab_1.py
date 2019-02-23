'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: sameer mall
@version Feb 23, 2019
'''

from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

# summary of hand work:
# P(Cavity|Catch) = (P(Cavity and Catch)) / P(Catch)
# = (0.108 + 0.072) / (0.108 + 0.016 +0.072+.144) = 0.5294117647

C = JointProbDist(['Coin1', 'Coin2'])
T, F = True, False
C[T, T] = 0.25
C[T, F] = 0.25
C[F, T] = 0.25
C[F, F] = 0.25

# Compute P(Coin2 | coin1 = heads)
PC = enumerate_joint_ask('Coin2', {'Coin1': T}, C)
print(PC.show_approx())

