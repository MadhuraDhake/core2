from queue import PriorityQueue

# Graph representation
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 4},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}


def astar(start, goal):

    # Priority Queue
    open_set = PriorityQueue()

    # Add starting node
    open_set.put((0, start))

    # Cost from start node
    g_cost = {start: 0}

    # Parent nodes
    parent = {start: None}

    while not open_set.empty():

        # Get node with minimum cost
        current = open_set.get()[1]

        print("Visiting Node:", current)

        # Goal reached
        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path

        # Check neighbours
        for neighbour in graph[current]:

            # Calculate new cost
            new_cost = g_cost[current] + graph[current][neighbour]

            # If better path found
            if neighbour not in g_cost or new_cost < g_cost[neighbour]:

                g_cost[neighbour] = new_cost

                # f(n) = g(n) + h(n)
                f_cost = new_cost + heuristic[neighbour]

                open_set.put((f_cost, neighbour))

                parent[neighbour] = current

    return None


# Driver Code
start = 'A'
goal = 'G'

path = astar(start, goal)

print("\nShortest Path:")
print(path)


#sc - bc - O(log V)
#sc - wc - O(E log V)
#tc - O(V)
"""
from queue import PriorityQueue

EXPLANATION :

from
from is a Python keyword used to import a specific part from a module.
A module is a file that already contains prewritten Python code and functions.
Instead of importing the entire module, we are importing only the thing we need.

queue
queue is a built-in Python module.
It contains different types of queue data structures.

A queue is a structure where elements are stored in an order.

This module helps in managing data in an organized manner.

import
import is a keyword used to bring external functionality into the current Python program.

Without importing, Python will not recognize classes or functions from other modules.

PriorityQueue
PriorityQueue is a special queue where elements are removed based on priority.

The smallest value gets removed first.

This is extremely important in A* Algorithm because:
A* always selects the node having the minimum total cost.

Internally what happens:

Python loads the queue module.
It finds the PriorityQueue class.
That class becomes available in this program.
Now we can create a priority queue object.

Why are we using PriorityQueue in A*?

Because A* always chooses:
Lowest f(n) = g(n) + h(n)

Where:
g(n) = actual path cost
h(n) = heuristic estimated cost

PriorityQueue automatically keeps elements sorted according to priority.

# Graph representation
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 1, 'E': 5},
    'C': {'F': 2},
    'D': {'G': 4},
    'E': {'G': 1},
    'F': {'G': 2},
    'G': {}
}

EXPLANATION :

# is used for comments in Python.

Comments are ignored by Python interpreter.

They are written only for humans to understand the code.

Graph representation
This comment tells us that below code stores a graph.

What is a graph?

A graph is a collection of:

Nodes (vertices)
Connections between nodes (edges)

Example:
A → B

Here:
A and B are nodes
Arrow is an edge

graph
graph is a variable name.

This variable stores the entire graph structure.

=
= is the assignment operator.

It stores the value on the right side into the variable on the left side.

{ }
Curly braces represent a dictionary in Python.

Dictionary stores data in:
key : value format

Example:
{
"name": "Madhura"
}

'A'
This is a node name.

Node A acts as a key in dictionary.

:
Colon separates key and value.

{'B': 1, 'C': 3}
This dictionary represents neighbours of node A.

Meaning:
A is connected to:
B with cost 1
C with cost 3

What does cost mean?

Cost means distance or weight required to travel.

'A': {'B': 1, 'C': 3}
Meaning:
From A:
Go to B with cost 1
Go to C with cost 3

Similarly:

'B': {'D': 1, 'E': 5}
Meaning:
From B:
Go to D with cost 1
Go to E with cost 5

'C': {'F': 2}
Meaning:
From C:
Go to F with cost 2

'D': {'G': 4}
Meaning:
From D:
Go to G with cost 4

'E': {'G': 1}
Meaning:
From E:
Go to G with cost 1

'F': {'G': 2}
Meaning:
From F:
Go to G with cost 2

'G': {}
G has no neighbours.

Empty dictionary {} means:
No outgoing path from G.

Internally what happens:

Python creates a dictionary.
Each node becomes a key.
Each node stores neighbouring nodes and edge costs.
Entire graph becomes stored in memory.

What are we actually doing here?

We are creating a weighted graph for A* search algorithm.

The algorithm will use this graph to:

Move from one node to another
Calculate costs
Find shortest path
# Heuristic values
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 2,
    'G': 0
}

EXPLANATION :

Comment symbol.

Heuristic values
This comment tells us that heuristic estimates are stored below.

What is heuristic?

Heuristic means:
Estimated distance from current node to goal node.

It is a smart guessing value.

A* uses heuristic to move faster toward goal.

heuristic
Variable storing heuristic values.

=
Assignment operator.

{ }
Dictionary.

'A': 7
Estimated distance from A to goal is 7.

'B': 6
Estimated distance from B to goal is 6.

'C': 4
Estimated distance from C to goal is 4.

'D': 3
Estimated distance from D to goal is 3.

'E': 1
Estimated distance from E to goal is 1.

'F': 2
Estimated distance from F to goal is 2.

'G': 0
Goal node heuristic is always 0.

Why?

Because distance from goal to itself is 0.

Internally what happens:

Python creates another dictionary.
Each node stores heuristic estimate.
A* later accesses these values during search.

What are we actually doing here?

We are helping A* decide which node looks closer to goal.

Without heuristic:
Algorithm behaves like Dijkstra.

With heuristic:
Algorithm becomes faster and smarter.

def astar(start, goal):

EXPLANATION :

def
def is a Python keyword used to define a function.

Function is a reusable block of code.

astar
Function name.

This function performs A* search algorithm.

( )
Parentheses hold parameters.

start
Input parameter representing starting node.

goal
Input parameter representing destination node.

:
Colon indicates start of function body.

Internally what happens:

Python creates a function object.
Function code gets stored.
Function will execute only when called.

What are we actually doing here?

We are creating the main A* algorithm function.

    # Priority Queue
    open_set = PriorityQueue()

EXPLANATION :

Indentation
Spaces before line indicate this code belongs to function.

Python uses indentation to define blocks.

Priority Queue

Comment.

open_set
Variable name.

Open set means:
List of nodes waiting to be explored.

=
Assignment operator.

PriorityQueue()
Creates a priority queue object.

( )
Calling constructor.

Constructor creates new object.

Internally what happens:

Memory is allocated.
Empty priority queue is created.
Queue can now store nodes with priorities.

Why is it needed?

Because A* must always pick node having minimum f-cost first.

    # Add starting node
    open_set.put((0, start))

EXPLANATION :

Add starting node

Comment.

open_set
Priority queue object.

.
Dot operator accesses function inside object.

put
Function used to insert element into queue.

((0, start))
Tuple being inserted.

Tuple format:
(priority, node)

0
Initial priority.

start
Starting node value.

Why priority 0?

Because initially:
g(n) = 0

No movement has happened yet.

Internally what happens:

Tuple inserted into queue.
Queue arranges according to priority.
Start node becomes first node to explore.

What are we actually doing here?

We are starting the search process from initial node.

    # Cost from start node
    g_cost = {start: 0}

EXPLANATION :

Cost from start node

Comment.

g_cost
Dictionary storing actual travel cost from start node.

=
Assignment operator.

{start: 0}
Dictionary initialization.

start
Key.

0
Value.

Meaning:
Cost from start node to itself is 0.

Internally:

Dictionary created.
Start node stored with cost 0.

Why needed?

A* uses g(n) to know actual travelled distance.

    # Parent nodes
    parent = {start: None}

EXPLANATION :

Parent nodes

Comment.

parent
Dictionary storing parent of each node.

This helps reconstruct shortest path later.

=
Assignment operator.

{start: None}
Dictionary.

None
Special Python value meaning:
No value.

Why None?

Start node has no parent.

Internally:

Parent dictionary created.
Start node stored without parent.

What are we actually doing here?

We are preparing to trace path backward after reaching goal.

    while not open_set.empty():

EXPLANATION :

while
Loop keyword.

Loop runs repeatedly while condition is True.

not
Logical operator.

Reverses boolean result.

open_set.empty()
Checks whether queue is empty.

If queue is empty:
Returns True

not True becomes False.

Meaning:
Loop continues until queue becomes empty.

:
Start of loop block.

Internally what happens:

Python checks queue.
If nodes exist:
Loop continues.
If queue empty:
Loop stops.

What are we actually doing here?

We are repeatedly exploring nodes until:

Goal found
OR
No path exists.
        # Get node with minimum cost
        current = open_set.get()[1]

EXPLANATION :

Get node with minimum cost

Comment.

current
Variable storing current node.

=
Assignment operator.

open_set.get()
Removes highest priority element.

In PriorityQueue:
Lowest value means highest priority.

Suppose queue has:
(4,'B')
(7,'C')

Then get() removes:
(4,'B')

[1]
Index operator.

Tuple has:
index 0 → priority
index 1 → node

So:
[1] extracts node only.

Internally:

Queue finds smallest priority.
Removes tuple.
Extracts node name.
Stores in current.

What are we actually doing here?

We are selecting the most promising node for exploration.

        print("Visiting Node:", current)

EXPLANATION :

print
Built-in function for displaying output.

( )
Function call.

"Visiting Node:"
String message.

,
Separator.

current
Current node variable.

Internally:

Python converts values to text.
Displays on screen.

What are we actually doing here?

We are showing traversal process step-by-step.

        # Goal reached
        if current == goal:

EXPLANATION :

Goal reached

Comment.

if
Conditional statement.

Checks condition.

current == goal
Comparison operator.

== checks equality.

If current node equals goal node:
Condition becomes True.

:
Start of if block.

Internally:

Python compares both values.
If same:
Goal reached.

What are we actually doing here?

We are checking whether destination has been found.

            path = []

EXPLANATION :

path
Variable storing shortest path.

=
Assignment operator.

[ ]
Empty list.

List stores ordered collection.

Internally:

Empty list created.
Path nodes will be added later.
            while current is not None:

EXPLANATION :

while
Loop.

current
Current node variable.

is not
Identity comparison operator.

Checks object identity.

None
Special null value.

Meaning:
Loop runs until current becomes None.

Why?

Because start node parent is None.

Internally:

Current node checked.
Loop continues backward through parents.
                path.append(current)

EXPLANATION :

path
List.

.
Dot operator.

append
Function adding item at end of list.

current
Node added into path.

Internally:

Current node inserted into list end.

What are we actually doing here?

We are building path from goal to start.

                current = parent[current]

EXPLANATION :

parent[current]
Gets parent of current node.

=
Assignment operator.

current becomes parent node.

Internally:

Dictionary searched.
Parent node returned.
Current moves backward.

What are we actually doing here?

We are tracing route backward.

            path.reverse()

EXPLANATION :

reverse
List function reversing order.

Why needed?

Path currently is:
Goal → Start

We need:
Start → Goal

Internally:

List elements swapped.
Order reversed.
            return path

EXPLANATION :

return
Keyword used to send value back.

path
Returned shortest path list.

Internally:

Function stops execution.
Path sent back to caller.

What are we actually doing here?

We are returning final shortest path.

        # Check neighbours
        for neighbour in graph[current]:

EXPLANATION :

Check neighbours

Comment.

for
Loop keyword.

neighbour
Loop variable.

in
Membership operator.

graph[current]
Gets neighbour dictionary of current node.

Loop runs for every neighbour.

Internally:

Current node neighbours fetched.
Loop iterates one by one.

What are we actually doing here?

We are exploring all possible next paths.

            # Calculate new cost
            new_cost = g_cost[current] + graph[current][neighbour]

EXPLANATION :

Calculate new cost

Comment.

new_cost
Variable storing updated path cost.

g_cost[current]
Current travel cost.

Addition operator.

graph[current][neighbour]
Edge cost between nodes.

Internally:

Current cost fetched.
Edge cost fetched.
Both added.

Example:
A→B cost = 1
Current cost = 0

New cost = 1

What are we actually doing here?

We are calculating actual path cost to neighbour.

            # If better path found
            if neighbour not in g_cost or new_cost < g_cost[neighbour]:

EXPLANATION :

if
Conditional.

neighbour not in g_cost
Checks whether neighbour visited before.

or
Logical OR operator.

new_cost < g_cost[neighbour]
Checks if new path is shorter.

<
Less-than operator.

Meaning:
Update only if:

Node never visited
OR
Better path found

Internally:
Python evaluates both conditions.

What are we actually doing here?

We are ensuring shortest path is maintained.

                g_cost[neighbour] = new_cost

EXPLANATION :

Updates neighbour cost.

Dictionary key:
neighbour

Value:
new_cost

Internally:
Old cost replaced with better cost.

                # f(n) = g(n) + h(n)
                f_cost = new_cost + heuristic[neighbour]

EXPLANATION :

f(n) = g(n) + h(n)

Comment explaining A* formula.

f_cost
Total estimated cost.

new_cost
Actual travelled cost.

heuristic[neighbour]
Estimated remaining cost.

Addition operator.

Formula:
f(n)=g(n)+h(n)

Internally:

Actual cost calculated.
Heuristic added.
Total priority obtained.

What are we actually doing here?

We are calculating node priority for A*.

                open_set.put((f_cost, neighbour))

EXPLANATION :

Inserts neighbour into priority queue.

Tuple format:
(priority,node)

Queue automatically sorts by f_cost.

Internally:

Tuple inserted.
Queue rearranges nodes.
                parent[neighbour] = current

EXPLANATION :

Stores parent relationship.

Meaning:
Current node leads to neighbour.

Internally:
Dictionary updated.

Why needed?

To reconstruct shortest path later.

    return None

EXPLANATION :

return
Returns value.

None
Means no path found.

Internally:
Function ends.

# Driver Code
start = 'A'
goal = 'G'

EXPLANATION :

Driver Code
Main execution section.

start
Starting node.

goal
Destination node.

=
Assignment operator.

'A' and 'G'
String values.

What are we actually doing here?

We are giving input to algorithm.

path = astar(start, goal)

EXPLANATION :

path
Variable storing returned shortest path.

astar(start, goal)
Function call.

Internally:

Function executes.
A* algorithm runs.
Shortest path returned.
print("\nShortest Path:")
print(path)

EXPLANATION :

print
Displays output.

"\nShortest Path:"
\n means new line.

Makes output cleaner.

print(path)
Displays shortest path list.

Internally:
Python converts list into readable text.

#sc - bc - O(log V)
#sc - wc - O(E log V)
#tc - O(V)

EXPLANATION :

These comments represent complexity analysis.

sc
Space Complexity.

bc
Best Case.

wc
Worst Case.

tc
Time Complexity.

O(log V)
Logarithmic complexity.

O(E log V)
Complexity involving edges and vertices.

O(V)
Linear complexity with vertices.

V
Number of vertices.

E
Number of edges.

What are we actually doing in this entire code?

This program implements A* Search Algorithm.

Main goal:
Find shortest path from start node to goal node intelligently.

Step-by-step actual working:

Create graph
Store heuristic values
Insert starting node into priority queue
Pick node with minimum f-cost
Explore neighbours
Calculate:
g(n) = actual cost
h(n) = estimated cost
f(n) = g(n) + h(n)
Update better paths
Continue until goal reached
Reconstruct shortest path using parent dictionary
Print shortest path

Final shortest path produced by this code:
A → B → D → G
input:
start = 'A'
goal = 'G'
output:
Visiting Node: A
Visiting Node: B
Visiting Node: C
Visiting Node: D
Visiting Node: E
Visiting Node: G

Shortest Path:
['A', 'B', 'E', 'G']"""