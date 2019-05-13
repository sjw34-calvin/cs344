% Sameer Mall
% Lab 13.1
% 05/03/19

% a. Do these exercises from LPN!.
% 		i. Exercise 3.2
%		Do you know these wooden Russian dolls (Matryoshka dolls) where the smaller ones are contained in bigger ones?

directlyIn(katarina, olga).
directlyIn(olga, natasha).
directlyIn(irina, natasha).

in(X, Y) :- directlyIn(X, Y).
in(X, Y) :- directlyIn(X, Z), in(Z, Y).


% 		ii. Exercise 4.5
% Suppose we are given a knowledge base with the following facts:

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

% base case
listtran([],[]).
listtran([G | X], [E | Y]) :- tran(G, E), listtran(X, Y).

% ?- listtran([eins,neun,zwei],X).
% X  =  [one,nine,two].

% ?- listtran(X,[one,seven,six,two]).
% X  =  [eins,sieben,sechs,zwei].

% b. Does Prolog implement a version of generalized modus ponens (i.e., modus ponens with
% variables and instatiation)? If so, demonstrate how it’s done; if not,
% explain why not. If it doesn’t, can you implement one? Why or why not?

% Yes, Prolog does implement a version of generalized modus ponens using first order logic. This allows Prolog to use
% variables. An example is provided below:

man(socrates).
mortal(X) :- man(X).

% ?- mortal(socrates).
% -> "true"

