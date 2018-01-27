# PathFinding

Finding length of shortest path between top left and bottom right corner of a maze, using physical intuition of wave propagation (essentially breadth-first search). We are allowed to take out exactly one wall.

The input maze needs to be a matrix of 0's and 1's where 0 is free space and 1 is a wall.
E.g. maze = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
corresponds to the following 6-by-6 maze:

000000
111110
000000
011111
011111
000000

where the only existing path between start to finish is in the shape of the number "2" and its length is 21. If we consider taking out a wall, however, the shortest path length becomes 11.
