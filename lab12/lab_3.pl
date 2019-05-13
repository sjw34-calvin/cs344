% Sameer Mall
% Lab 12.3
% 04/26/19

% Create a Prolog program that implements the ridiculous inferences used by Sir Bedevere (Terry Jones)
% to justify the burning of the witch (Connie Booth) in Monte Python's Holy Grail.
% Load your rules and demonstrate that the woman is indeed a witch.

witch(X):- burns(X), woman(X), dressedAsOne(X).
burns(X):- wood(X).
wood(X):- floats(X).
floats(X):- sameWeight(duck, X) ; bread(X) ; apples(X) ; cherries(X).
dressedAsOne(girl).
sameWeight(duck, girl).
woman(girl).
bread(bread).
apples(apples).
cherries(cherries).

% ?- witch(girl).
% returns true