# Game-of-Life

The board has the size of M x N cells. A cell can have one of two conditions: 1 - alive, 0 - dead. Each cell can interact with 8 neighbors. The main rules are:

* Alive cell, which has 2 alive neighbors, dies.

* Alive cell, which has 2 or 3 alive neighbors, continues living.

* Alive cell, which has more than 3 alive neighbors, dies.

* Dead cell, which has 3 alive neighbors, reborns.

The task is to write a program, which will be able to:

- randomly generate start state of the board;

- get start state of the board from the file;

- print new state of the board every second.
