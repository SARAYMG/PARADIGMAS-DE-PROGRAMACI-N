/* Facts */
male(jack).
male(oliver).
male(ali).
male(james).
male(simon).
male(harry).
male(dan).
male(erick).
female(helen).
female(sophie).
female(jess).
female(lily).
female(jeny).
 
parent_of(jack,jess).
parent_of(jack,lily).
parent_of(helen, jess).
parent_of(helen, lily).
parent_of(oliver,james).
parent_of(sophie, james).
parent_of(jess, simon).
parent_of(ali, simon).
parent_of(lily, harry).
parent_of(james, harry).
parent_of(jeny, dan).
parent_of(jeny, erick).
parent_of(dan, ali).
parent_of(lily,jess).

 
/* Rules */
father_of(X,Y):- male(X),
    parent_of(X,Y).
 
mother_of(X,Y):- female(X),
    parent_of(X,Y).
 
grandfather_of(X,Y):- male(X),
    parent_of(X,Z),
    parent_of(Z,Y).
 
grandmother_of(X,Y):- female(X),
    parent_of(X,Z),
    parent_of(Z,Y).
 
sister_of(X,Y):- %(X,Y or Y,X)%
    female(X),
    father_of(F, Y), father_of(F,X),X \= Y.
 
sister_of(X,Y):- female(X),
    mother_of(M, Y), mother_of(M,X),X \= Y.
 
aunt_of(X,Y):- female(X),
    parent_of(Z,Y), sister_of(Z,X),!.

/* Reglas Propuestas */
aunty_of(X,Y):-
    parent_of(Z,Y),
    sister_of(X,Z).
 
brother_of(X,Y):- %(X,Y or Y,X)%
    male(X),
    father_of(F, Y), father_of(F,X),X \= Y.
 
brother_of(X,Y):- male(X),
    mother_of(M, Y), mother_of(M,X),X \= Y.
 
uncle_of(X,Y):-
    parent_of(Z,Y), brother_of(Z,X).

ancestor_of(X,Y):- parent_of(X,Y).
ancestor_of(X,Y):- parent_of(X,Z),
    ancestor_of(Z,Y).

/* Reglas Propuestas */
sibling_of(X,Y):-
    parent_of(Z,X),
    parent_of(Z,Y),  X\=Y.

/* Reglas Propuestas */
nephew_of(X,Y):-
    male(X),
    sibling_of(Z,Y),
    parent_of(Z,X).
