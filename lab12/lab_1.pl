% Sameer Mall
% Lab 12.1
% 04/26/19


% a. From LPN!
% i. Exercise 1.4 - Represent the following in Prolog

% 1. butch is a killer
killer(butch).

% 2. Mia and Marsellus are married.
married(mia, marcellus).

% 3. Zed is dead.
dead(zed).

% 4. Marsellus kills everyone who gives Mia a footmassage.
kills(marsellus, X) :- givesFootMassage(X, mia).

% 5. Mia loves everyone who is a good dancer.
loves(mia, X) :- goodDancer(X).

% 6. Jules eats anything that is nutritious or tasty.
eats(jules, X) :- nutritious(X).
eats(jules, X) :- tasty(X).

% I built the representations the way I did because the first 3 are simply facts
% and the last 3 are rules/conditions so I represented them accordingly.

% ii. Exercise 1.5 - Prolog Response

% Suppose we are working with the following
% knowledge base:
wizard(ron).
wizard(X) :- hasBroom(X), hasWand(X).

hasWand(harry).
quidditchPlayer(harry).
hasBroom(X) :- quidditchPlayer(X).

% How does prolog respond to the following queries?
% Explain how Prolog comes up with its answers.
% 1.
wizard(ron).
% -> true
% This is one of the facts explicitly recorded in our KB.

% 2.
witch(ron).
%-> undefined procedure
% This query is about a property (witch) that it has no information about
% so it concludes that the query cannot be deduced from the information.

% 3.
wizard(hermione).
%-> false
% This is not a fact in our KB so this information cannot be deduced from the
% information in our KB.

% 4.
witch(hermione).
% -> undefined procedure
% This query is about a property (witch) that it has no information about
% so it concludes that the query cannot be deduced from the information.

% 5.
wizard(harry).
% -> true
% This isn't an explicitly stated fact but can be deduced from another rule
% in our KB.

% 6.
wizard(Y).
% -> Y = ron ; Y = harry.
% Both Ron and Harry meet the conditions for the wizard rule.

% 7.
% witch(Y).
% -> undefined procedure
% This query is about a property (witch) that it has no information about
% so it concludes that the query cannot be deduced from the information.

b.
​
% This can be represented in Prolog in the following format:
​
q :- p.
p.

% ? - q. -> returns true
​
% This is modus ponens
% The Prolog can be given the premises as facts, and if you ask it
% about the conclusion, it will respond "true."

c.
% Horn clause is a clause with at most one positive literal. It allows us to use variables which we can't use in
% propositional logic. Horn clauses can only imply one thing whereas, propositional logic can imply conjunction and
% disjunction.

d.
% Prolog does support this distinction. We can "TELL" the knowledge base facts
% (fundamental assertions abou the problem domain)and rules (inferences about facts
% in the domain). We can then "ASK" (query) questions about the domain.
% i.e.
man(socrates).
mortal(X) :- man(X).

% ?- mortal(socrates).
% -> "true"


