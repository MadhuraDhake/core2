import heapq

def prim(graph,start):
    visited=set()
    min_heap=[(0,start)]
    total_cost=0

    while min_heap:

        weight,node=heapq.heappop(min_heap)

        if node not in visited:

            visited.add(node)

            total_cost+=weight

            print("Visited:",node,"Weight:",weight)

            for neighbor,w in graph[node]:

                if neighbor not in visited:

                    heapq.heappush(min_heap,(w,neighbor))

    print("Total Cost of MST:",total_cost)


graph={
    'A':[('B',2),('C',1)],
    'B':[('A',2),('D',4),('E',2)],
    'C':[('A',1),('F',2)],
    'D':[('B',4)],
    'E':[('B',2),('F',3)],
    'F':[('C',2),('E',3)]
}

prim(graph,'A')
"""
EXPLANATION :

import heapq
import is a keyword in Python.
It is used to bring an external module into the current program.
A module is a file that contains pre-written functions and tools.
Instead of writing everything manually, Python allows us to use already available modules.
heapq is the name of the module.
heapq stands for "Heap Queue".
This module provides heap data structure functions.

WHAT IS A HEAP :

A heap is a special tree-based data structure.
In a Min Heap:
The smallest element always stays at the top.
Prim’s Algorithm always needs the minimum weight edge.
So Min Heap helps in quickly finding the smallest edge.

WHY WE USE heapq HERE :

Prim’s Algorithm repeatedly selects the minimum weight edge.
Instead of searching manually every time,
heap automatically keeps smallest weight at top.
This makes the algorithm faster and efficient.

INTERNAL WORKING :

Python loads all functions from heapq module into memory.

Functions like:

heapq.heappush()
heapq.heappop()

become available for use.

def prim(graph,start):

EXPLANATION :

def prim(graph,start):
def is a keyword.
It stands for "define".
It is used to create a function.
prim is the function name.
The function is named after Prim’s Algorithm.
(graph,start) are parameters.
graph
stores the graph data structure.
start
stores the starting node from where MST construction begins.
: colon marks the beginning of function block.

WHAT THIS FUNCTION DOES :

This function implements Prim’s Minimum Spanning Tree Algorithm.
It connects all vertices using minimum possible total cost.

INTERNAL WORKING :

When function is called:

prim(graph,'A')

Python stores:

graph → graph dictionary
start → 'A'
Then execution starts line by line inside function.
    visited=set()

EXPLANATION :

visited=set()
visited is a variable.
= is assignment operator.
set() creates an empty set.

WHAT IS A SET :

Set is a collection datatype in Python.
It stores unique values only.
Duplicate values are not allowed.

WHY WE USE VISITED SET :

Prim’s Algorithm should not revisit nodes again and again.
So visited set keeps track of already processed vertices.

INTERNAL WORKING :

Initially:

visited={}

Actually empty set internally:

set()

As nodes get visited:

{'A'}
{'A','C'}
{'A','C','B'}
    min_heap=[(0,start)]

EXPLANATION :

min_heap=[(0,start)]
min_heap
is a variable storing heap elements.
=
assigns value.
[]
represents a list.
(0,start)
is a tuple.

WHAT THIS TUPLE MEANS :

(weight,node)

So:

(0,'A')

means:

Current weight = 0
Starting node = A

WHY WE START WITH 0 :

Starting node does not need any edge to reach itself.
So initial cost is 0.

WHY MIN HEAP IS USED :

Heap automatically gives smallest weight edge first.

INTERNAL WORKING :

Initially heap contains:

[(0,'A')]

Later more edges are inserted.

    total_cost=0

EXPLANATION :

total_cost=0
total_cost
stores total MST cost.
Initially cost is 0.

WHY THIS IS NEEDED :

Prim’s Algorithm keeps adding edge weights.
Final sum becomes MST cost.

INTERNAL WORKING :

Initially:

0

After adding edges:

1
3
5
7
11
    while min_heap:

EXPLANATION :

while min_heap:
while
is a loop keyword.
Loop continues until condition becomes False.
min_heap
itself acts as condition.

WHAT THIS CONDITION MEANS :

If heap contains elements:
loop runs.
If heap becomes empty:
loop stops.

WHY THIS IS NEEDED :

Algorithm continues processing until all reachable nodes are explored.

INTERNAL WORKING :

Heap contents keep changing:

[(0,'A')]
[(1,'C'),(2,'B')]
[(2,'B'),(2,'F')]

Loop runs until:

[]
        weight,node=heapq.heappop(min_heap)

EXPLANATION :

weight,node=heapq.heappop(min_heap)
heapq.heappop()
removes and returns smallest element from heap.
min_heap
is passed into function.

Returned tuple gets unpacked into:

weight
node

EXAMPLE :

Heap:

[(1,'C'),(2,'B')]

After pop:

weight=1
node='C'

WHY THIS IS IMPORTANT :

Prim’s Algorithm always selects minimum weight edge.

INTERNAL WORKING :

Heap internally rearranges itself after removal.
Smallest value always stays at top.
        if node not in visited:

EXPLANATION :

if node not in visited:
if
is conditional statement.
not in
checks absence.

WHAT THIS CHECKS :

"Is this node unvisited?"

WHY THIS IS NEEDED :

Already visited nodes should not be processed again.
Prevents cycles.

INTERNAL WORKING :

If:

visited={'A','C'}
node='B'

Then:

'B' not in visited

becomes:

True
            visited.add(node)

EXPLANATION :

visited.add(node)
.add()
is set method.
Adds node into visited set.

WHY THIS IS NEEDED :

Marks current node as processed.

INTERNAL WORKING :

Before:

{'A','C'}

After adding B:

{'A','C','B'}
            total_cost+=weight

EXPLANATION :

total_cost+=weight
+=
is shorthand assignment operator.

This means:

total_cost=total_cost+weight

WHAT THIS DOES :

Adds current edge weight into MST total cost.

EXAMPLE :

Before:

total_cost=3
weight=2

After:

total_cost=5
            print("Visited:",node,"Weight:",weight)

EXPLANATION :

print("Visited:",node,"Weight:",weight)
print()
displays output on screen.
"Visited:"
is string.
node
displays current node.
"Weight:"
displays label.
weight
displays edge weight.

OUTPUT EXAMPLE :

Visited: C Weight: 1
            for neighbor,w in graph[node]:

EXPLANATION :

for neighbor,w in graph[node]:
for
loop iterates repeatedly.
neighbor,w
unpack tuple values.
graph[node]
accesses adjacency list of current node.

EXAMPLE :

If:

node='A'

Then:

graph['A']

returns:

[('B',2),('C',1)]

Loop runs as:

neighbor='B'
w=2

then:

neighbor='C'
w=1

WHY THIS IS NEEDED :

To explore connected neighboring vertices.
                if neighbor not in visited:

EXPLANATION :

if neighbor not in visited:
Checks whether neighbor is already visited.

WHY :

Only unvisited nodes should be added into heap.

INTERNAL WORKING :

If:

visited={'A'}
neighbor='B'

Condition becomes:

True
                    heapq.heappush(min_heap,(w,neighbor))

EXPLANATION :

heapq.heappush(min_heap,(w,neighbor))
heappush()
inserts element into heap.

(w,neighbor)
stores:

(weight,node)

EXAMPLE :

(2,'B')

WHY THIS IS NEEDED :

Future nodes must be available for selection.
Heap automatically keeps smallest weight at top.

INTERNAL WORKING :

Before:

[(2,'B')]

After adding:

[(1,'C'),(2,'B')]
    print("Total Cost of MST:",total_cost)

EXPLANATION :

print("Total Cost of MST:",total_cost)
Displays final minimum spanning tree cost.

OUTPUT :

Total Cost of MST: 11
graph={
    'A':[('B',2),('C',1)],
    'B':[('A',2),('D',4),('E',2)],
    'C':[('A',1),('F',2)],
    'D':[('B',4)],
    'E':[('B',2),('F',3)],
    'F':[('C',2),('E',3)]
}

EXPLANATION :

graph
is dictionary storing graph structure.
{} represent dictionary.
'A'
is key.
[('B',2),('C',1)]
means:
A connected to B with weight 2
A connected to C with weight 1

WHAT THIS GRAPH REPRESENTS :

A --2-- B
|       |
1       2
|       |
C --2-- F
        |
        3
        |
        E

WHY GRAPH IS NEEDED :

Prim’s Algorithm works on weighted graphs.
prim(graph,'A')

EXPLANATION :

prim(graph,'A')
Function call statement.
graph
passes graph data.
'A'
passes starting node.

INTERNAL WORKING STEP-BY-STEP :

STEP 1:

Start from A

STEP 2:

Choose minimum edge A-C = 1

STEP 3:

Choose minimum edge A-B = 2

STEP 4:

Choose minimum edge B-E = 2

STEP 5:

Choose minimum edge C-F = 2

STEP 6:

Choose minimum edge B-D = 4

FINAL MST COST :

11

WHAT ACTUALLY WE ARE DOING IN THIS CODE :

We are implementing Prim’s Minimum Spanning Tree Algorithm.
The goal is:
Connect all vertices
Use minimum total edge cost
Avoid cycles
The algorithm:
Starts from one node
Chooses smallest edge
Expands graph gradually
Continues until all nodes are connected

OUTPUT :

Visited: A Weight: 0
Visited: C Weight: 1
Visited: B Weight: 2
Visited: E Weight: 2
Visited: F Weight: 2
Visited: D Weight: 4

Total Cost of MST: 11"""