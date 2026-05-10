# Assignment No. 2
# A* Algorithm for 8 Puzzle Problem

import heapq

# Goal State
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, -1]]

# Heuristic Function
# Counts number of misplaced tiles
def heuristic(state):
    count = 0

    for i in range(3):
        for j in range(3):

            # Ignore blank tile
            if state[i][j] != -1 and state[i][j] != goal_state[i][j]:
                count += 1

    return count


# Find Blank Tile Position
def find_blank(state):

    for i in range(3):
        for j in range(3):

            if state[i][j] == -1:
                return i, j


# Generate Neighbor States
def get_neighbors(state):

    neighbors = []

    # Blank tile position
    x, y = find_blank(state)

    # Possible moves:
    # Right, Left, Down, Up
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy

        # Check boundaries
        if 0 <= nx < 3 and 0 <= ny < 3:

            # Create deep copy
            new_state = [row[:] for row in state]

            # Swap blank tile
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors


# Convert List to Tuple
# Used for storing in set
def to_tuple(state):

    return tuple(tuple(row) for row in state)


# Print Puzzle State
def print_state(state):

    for row in state:
        print(row)

    print()


# A* Search Algorithm
def astar(start):

    # Priority Queue
    open_list = []

    # Push initial state
    # (f, g, state, path)
    heapq.heappush(
        open_list,
        (heuristic(start), 0, start, [])
    )

    # Visited states
    closed_set = set()

    while open_list:

        # Get state with smallest f value
        f, g, current, path = heapq.heappop(open_list)

        # Goal Check
        if current == goal_state:

            print("\nSolution Found!\n")

            steps = path + [current]

            for i, step in enumerate(steps):

                print("Step", i)
                print_state(step)

            print("Total Moves =", len(steps) - 1)

            return

        # Mark current state visited
        closed_set.add(to_tuple(current))

        # Generate neighbors
        for neighbor in get_neighbors(current):

            # Skip visited states
            if to_tuple(neighbor) in closed_set:
                continue

            # Cost from start
            new_g = g + 1

            # f = g + h
            new_f = new_g + heuristic(neighbor)

            # Add to priority queue
            heapq.heappush(
                open_list,
                (new_f, new_g, neighbor, path + [current])
            )

    print("No Solution Found")


# MAIN PROGRAM

start_state = []

print("Enter Start State (use -1 for blank):")

for i in range(3):

    row = list(map(int, input().split()))
    start_state.append(row)

# Run A* Algorithm
astar(start_state)
'''
What Actually Are We Doing In This Code?

In this program, we are solving the 8 Puzzle Problem using the A* Search Algorithm.

The 8 Puzzle Problem contains:

8 numbered tiles
1 blank space represented using -1

The goal is to move the tiles step-by-step until we reach the final goal arrangement.

Goal State:

1 2 3
4 5 6
7 8 -1

The program:

Takes the starting puzzle from the user
Finds all possible moves
Uses A* Algorithm to find the best path
Uses a heuristic function to decide which move is better
Prints all steps from start state to goal state

A* Algorithm works using:

f(n)=g(n)+h(n)

Where:

g(n) = actual cost from start node
h(n) = estimated cost to reach goal
f(n) = total estimated cost

The algorithm always selects the state having minimum f(n) value.

# Assignment No. 2
# A* Algorithm for 8 Puzzle Problem

import heapq

EXPLANATION :

#

The # symbol is used for comments in Python.
Comments are ignored by the Python interpreter.
They are written to explain the code to humans.
They improve readability and understanding.

Assignment No. 2

This is simply a comment written to identify the assignment number.

A* Algorithm for 8 Puzzle Problem

This comment tells us what the program is about.
The program uses the A* search algorithm to solve the 8 puzzle problem.

import

import is a Python keyword.
It is used to bring external modules or libraries into the program.
Python has many built-in modules containing ready-made functions.

heapq

heapq is a built-in Python module.
It is used to create a Priority Queue using a Heap data structure.
A heap automatically keeps the smallest element at the top.
In A* Algorithm, we always need the state with minimum cost.
Therefore heapq is necessary.

Internally what happens:

Python loads the heapq module into memory.
All heap-related functions become available.
We can now use:
heapq.heappush()
heapq.heappop()

These functions help in inserting and removing elements efficiently.

# Goal State
goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, -1]]

EXPLANATION :

goal_state

This is a variable name.
It stores the final desired puzzle arrangement.

=

This is the assignment operator.
It assigns the value on the right side to the variable on the left side.

[[1, 2, 3], [4, 5, 6], [7, 8, -1]]

This is a 2-dimensional list.
A 2D list is a list containing other lists.
It represents rows and columns like a matrix.

Structure internally:

[
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, -1]
]

-1

Represents the blank tile.
Blank means empty position.

Why goal state is needed:

The algorithm continuously compares current state with goal state.
When both become equal, the solution is found.

Internally what happens:

Python creates nested lists in memory.
goal_state stores the memory reference of that list.
# Heuristic Function
# Counts number of misplaced tiles
def heuristic(state):

EXPLANATION :

def

def is a Python keyword.
It is used to define a function.

Function meaning:

A function is a reusable block of code.
It performs a specific task.

heuristic

This is the function name.
It calculates heuristic value.

Heuristic meaning:

A heuristic estimates how close we are to the goal.
Here we count misplaced tiles.

(state)

state is a parameter.
Parameters receive values when function is called.

Example:

heuristic(start_state)

Then:

start_state gets stored inside state.

:

Colon indicates start of function body.

Internally what happens:

Python stores this function definition in memory.
Function code does not execute immediately.
It executes only when called.
    count = 0

EXPLANATION :

count

Variable used to store number of misplaced tiles.

=

Assignment operator.

0

Initial value.

Why needed:

We need a counter.
Every wrong tile increases count by 1.

Internally:

Python allocates memory for integer 0.
count points to that memory.
    for i in range(3):

EXPLANATION :

for

Loop keyword.
Used for repetition.

i

Loop variable.
Stores current row index.

in

Checks values coming from iterable object.

range(3)

Generates:
0, 1, 2

Why 3:

Puzzle has 3 rows.

Internally:

Loop runs 3 times.
i becomes:
0
1
2
        for j in range(3):

EXPLANATION :

This is a nested loop.

j

Stores column index.

Purpose:

Outer loop handles rows.
Inner loop handles columns.

Together:

Every cell of puzzle is visited.

Internally:

For every value of i,
j again runs from 0 to 2.

So total iterations:

3×3=9

All 9 positions are checked.

            if state[i][j] != -1 and state[i][j] != goal_state[i][j]:

EXPLANATION :

if

Conditional statement.
Executes code only if condition is True.

state[i][j]

Accesses current tile.

Example:

state[1][2]
Row 1, column 2.

!=

Not equal operator.

-1

Blank tile.

and

Logical operator.
Both conditions must be True.

Condition meaning:

Tile should not be blank
Tile should not match goal state

If both are true:

Tile is misplaced.

Internally:

Python checks first condition.
Then second condition.
If both True:
Entire condition becomes True.
                count += 1

EXPLANATION :

+=

Compound assignment operator.

Equivalent to:

count = count + 1

Purpose:

Increase misplaced tile count.

Internally:

Old value read
1 added
New value stored back
    return count

EXPLANATION :

return

Sends value back to function caller.

count

Final heuristic value.

Example:

If 3 tiles misplaced:
return 3

Internally:

Function execution stops.
Value sent back.
# Find Blank Tile Position
def find_blank(state):

EXPLANATION :

Purpose:

Find position of blank tile (-1).

Why needed:

Blank tile is moved during puzzle solving.
We must know its location.
    for i in range(3):
        for j in range(3):

EXPLANATION :

These loops scan entire puzzle.

i

Row index

j

Column index

All positions checked one-by-one.

            if state[i][j] == -1:

EXPLANATION :

==

Equality operator.

Checks:

Is current tile blank?

If yes:

Condition becomes True.
                return i, j

EXPLANATION :

Returns blank tile coordinates.

Example:

If blank at row 2 column 1:
return 2, 1

Internally:

Tuple is created.
# Generate Neighbor States
def get_neighbors(state):

EXPLANATION :

Neighbor states:

States reachable in one move.

Purpose:

Generate all possible next puzzle configurations.
    neighbors = []

EXPLANATION :

Creates empty list.

Purpose:

Store all neighboring states.
    x, y = find_blank(state)

EXPLANATION :

Function call:

Finds blank tile position.

x

Row

y

Column

Example:

If function returns (2,1)
Then:
x = 2
y = 1
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

EXPLANATION :

Possible movement directions.

Structure:

(0,1)   → Right
(0,-1)  → Left
(1,0)   → Down
(-1,0)  → Up

Why tuples used:

Tuples store fixed coordinate changes.
    for dx, dy in moves:

EXPLANATION :

Loop through every move.

dx

Row movement

dy

Column movement

Example:

(0,1)
Means move right.
        nx = x + dx
        ny = y + dy

EXPLANATION :

Calculates new blank position.

nx

New row

ny

New column

Example:

Current position (2,1)
Move (0,1)

Then:

nx = 2
ny = 2
        if 0 <= nx < 3 and 0 <= ny < 3:

EXPLANATION :

Boundary checking.

Purpose:

Prevent invalid positions.

Checks:

Row inside grid
Column inside grid

Without this:

Program may crash.
            new_state = [row[:] for row in state]

EXPLANATION :

Creates deep copy of puzzle.

Why needed:

Original puzzle should not change.

row[:]

Copies each row separately.

Internally:

New independent list created.
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

EXPLANATION :

Swaps tiles.

Purpose:

Move blank tile.

Python swapping internally:

Temporary tuple created
Values exchanged

\

Line continuation character.
            neighbors.append(new_state)

EXPLANATION :

append()

Adds element to list.

Adds newly generated puzzle state.

    return neighbors

EXPLANATION :

Returns all neighboring states.

# Convert List to Tuple
def to_tuple(state):

EXPLANATION :

Purpose:

Convert list into tuple.

Why:

Lists cannot be stored in sets.
Tuples can.
    return tuple(tuple(row) for row in state)

EXPLANATION :

Converts:

Inner lists → tuples
Outer list → tuple

Example:

[[1,2],[3,4]]

becomes:

((1,2),(3,4))
# Print Puzzle State
def print_state(state):

EXPLANATION :

Function to display puzzle neatly.

    for row in state:
        print(row)

EXPLANATION :

Prints each row separately.

    print()

EXPLANATION :

Prints empty line.

Purpose:

Improve readability.
# A* Search Algorithm
def astar(start):

EXPLANATION :

Main solving function.

Purpose:

Find shortest path to goal.

start

Starting puzzle.
    open_list = []

EXPLANATION :

Priority queue storage.

Stores states waiting for exploration.

    heapq.heappush(
        open_list,
        (heuristic(start), 0, start, [])
    )

EXPLANATION :

Adds initial state.

Structure:

(f, g, current_state, path)

heuristic(start)

h(n)

0

g(n)

start

Current state

[]

Empty path initially.
    closed_set = set()

EXPLANATION :

Stores visited states.

Purpose:

Avoid revisiting same states.
    while open_list:

EXPLANATION :

Loop runs while queue not empty.

If queue empty:

No solution exists.
        f, g, current, path = heapq.heappop(open_list)

EXPLANATION :

Removes smallest priority state.

heappop()

Removes minimum element.

Because heap automatically sorts.

        if current == goal_state:

EXPLANATION :

Goal checking.

If current puzzle equals goal:

Solution found.
            print("\nSolution Found!\n")

EXPLANATION :

\n

New line character.

Improves formatting.

            steps = path + [current]

EXPLANATION :

Combines previous path and final state.

            for i, step in enumerate(steps):

EXPLANATION :

enumerate()

Gives index and value together.

i

Step number

step

Puzzle state
                print("Step", i)
                print_state(step)

EXPLANATION :

Displays step number and puzzle.

            print("Total Moves =", len(steps) - 1)

EXPLANATION :

len()

Counts total states.

-1

Because initial state is not a move.
            return

EXPLANATION :

Stops function after solution found.

        closed_set.add(to_tuple(current))

EXPLANATION :

Adds current state to visited set.

        for neighbor in get_neighbors(current):

EXPLANATION :

Generates all possible next states.

            if to_tuple(neighbor) in closed_set:
                continue

EXPLANATION :

Checks:

Already visited?

continue

Skip remaining loop code.
            new_g = g + 1

EXPLANATION :

Move cost increased.

Every move costs 1.

            new_f = new_g + heuristic(neighbor)

EXPLANATION :

Calculates total cost.

f(n)=g(n)+h(n)

            heapq.heappush(
                open_list,
                (new_f, new_g, neighbor, path + [current])
            )

EXPLANATION :

Adds neighbor into priority queue.

Queue automatically arranges by smallest f.

    print("No Solution Found")

EXPLANATION :

Executes if no path exists.

# MAIN PROGRAM

start_state = []

EXPLANATION :

Creates empty list for user input.

print("Enter Start State (use -1 for blank):")

EXPLANATION :

Displays instruction to user.

for i in range(3):

    row = list(map(int, input().split()))
    start_state.append(row)

EXPLANATION :

input()

Takes user input.

.split()

Splits values by spaces.

map(int, ...)

Converts strings to integers.

list()

Converts map object into list.

append()

Adds row into puzzle.

Example input:

1 2 3

becomes:

[1, 2, 3]
# Run A* Algorithm
astar(start_state)

EXPLANATION :

Calls A* function.

start_state

Passed as argument.

Program execution starts solving puzzle from here.

INPUT:
1 2 3
4 5 6
7 -1 8

OUTPUT:

Solution Found!

Step 0
[1, 2, 3]
[4, 5, 6]
[7, -1, 8]

Step 1
[1, 2, 3]
[4, 5, 6]
[7, 8, -1]

Total Moves = 1'''