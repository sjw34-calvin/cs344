% Sameer Mall
% Lab 12.2
% 04/26/19

% a)
%	i) Exercise 2.1:  questions 1, 2, 8, 9, 14 - Give the necessary instantiations.
% 		Which of the following pairs unify?
% 		1) bread  =  bread -> true
% 		2) ’Bread’  =  bread -> false
% 		8) food(X)  =  food(bread) -> X = bread
% 		9) food(bread,X)  =  food(Y,sausage) -> X = sausage, Y = bread.
%		14) meal(food(bread),X)  =  meal(X,drink(beer)) -> false

% 	ii) Exercise 2.2
% 		We are working with the following database.

house_elf(dobby).
witch(hermione).
witch(’McGonagall’).
witch(rita_skeeter).
magic(X):-  house_elf(X).
% magic(X):-  wizard(X).
magic(X):-  witch(X).

% Which of the following queries are satisfied? Where relevant, give all the variable instantiations that lead to success.

% 1. ?-  magic(house_elf). -> false
% 2. ?-  wizard(harry). -> undefined procedure
% 3. ?-  magic(wizard). -> false
% 4. ?-  magic(’McGonagall’). -> true
% 5. ?-  magic(Hermione). ->
% 		Hermione = dobby;
%		After the one above it will go to the wizard line but since it is not in our KB it skips it and moves on to the 3 witch statements
%		Hermione = Hermione;
% 		Hermione = ’McGonagall’;
%		Hermione = rita_skeeter;
% Initially, the given program did not work because wizard is an undefined procedure in the KB so I had to comment it out
% to make it work.

% Draw the search tree for the query magic(Hermione).
% _variable is a special type of anonymous variable
%          --------------------------------------------------------------
%          |                     ?- magic(Hermione)                     |
%          --------------------------------------------------------------
%                      /              |                     \
%     Hermione = _G34 /               | Hermione = _G34      \ Hermione = _G34
%                    /                |                       \
%     ----------------------     ------------------        ---------------------------------------
%     | ?- house_elf(_G34) |	 | ?- wizard(_G34) |       |    	     ?- witch(_G34)          |
%     ----------------------     ------------------        ---------------------------------------
%               |						|						/   | 						\
%  _G34 = dobby |						|    _G34 = hermione   /    | _G34 = 'McGonagall' 	 \ _G34 = rita_skeeter
%				|						|					  /     |						  \
%			 ------					    X				   ------   ------                   -------
%            |	   |									   |    |   |    |					 |     |
%            -------                                       ------   ------ 				     -------
%

% b) Inference in propositional logic does make use of unification. This is useful because unification allows us to combine two general
%	 but overlapping rules. Modus ponens is an example of inference rules using unification.
% https://people.cs.pitt.edu/~milos/courses/cs2740/Lectures/class9.pdf
%
% c) Prolog does use resolution as its inference engine.
%

