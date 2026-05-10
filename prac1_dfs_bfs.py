# DFS Function
def dfs(visited, graph, node):

    # Check if node is not visited
    if node not in visited:

        # Print current node
        print(node, end=" ")

        # Mark node as visited
        visited.add(node)

        # Visit all neighbours recursively
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# BFS Function
def bfs(visited, graph, node, queue):

    # Mark starting node visited
    visited.add(node)

    # Insert node into queue
    queue.append(node)

    # Continue until queue becomes empty
    while queue:

        # Remove first element from queue
        s = queue.pop(0)

        # Print current node
        print(s, end=" ")

        # Visit all neighbours
        for neighbour in graph[s]:

            # If neighbour not visited
            if neighbour not in visited:

                # Mark visited
                visited.add(neighbour)

                # Add into queue
                queue.append(neighbour)


# Main Function
def main():

    # Set for DFS visited nodes
    visited1 = set()

    # Set for BFS visited nodes
    visited2 = set()

    # Queue for BFS
    queue = []

    # Input number of nodes
    n = int(input("Enter number of nodes : "))

    # Empty graph dictionary
    graph = dict()

    # Input graph
    for i in range(1, n + 1):

        # Number of edges
        edges = int(input("Enter number of edges for node {} : ".format(i)))

        # Create empty adjacency list
        graph[i] = list()

        # Input neighbours
        for j in range(1, edges + 1):

            node = int(input("Enter edge {} for node {} : ".format(j, i)))

            graph[i].append(node)

    # DFS Traversal
    print("The following is DFS")

    dfs(visited1, graph, 1)

    print()

    # BFS Traversal
    print("The following is BFS")

    bfs(visited2, graph, 1, queue)


# Driver Code
if __name__ == "__main__":
    main()

#tc- O(v+e)
#sc- O(v)
"""
# DFS Function
def dfs(visited, graph, node):

EXPLANATION :

# DFS Function

# is used for writing a comment in Python.
Comments are ignored by the Python interpreter.
They are written to explain the code to humans.
Here, the comment tells us that the next code is related to the DFS function.

def

def is a keyword in Python.
It is used to define a function.
A function is a reusable block of code.
Instead of writing the same logic again and again, we create a function and call it whenever needed.

dfs

dfs is the function name.
DFS stands for Depth First Search.
Depth First Search is a graph traversal algorithm.
It first visits one node completely till the deepest level and then comes back.

( and )

Parentheses are used to pass parameters to the function.
Parameters are variables that receive values when the function is called.

visited

visited stores all nodes that have already been visited.
This is important because graphs may contain cycles.
Without checking visited nodes, the program may enter infinite recursion.

graph

graph stores the graph structure.
It is represented using a dictionary.
Each node stores a list of its neighbouring nodes.

Example:

graph = {
    1: [2,3],
    2: [1,4],
    3: [1],
    4: [2]
}

node

node represents the current node being processed.
DFS starts from one node and explores deeply.

:

Colon indicates the start of the function body.
All indented lines below belong to this function.

What are we doing in this block?

We are creating a DFS function.
This function will traverse the graph using the Depth First Search technique.
It will:
check visited nodes
print nodes
recursively visit neighbours

Internal Working:

Function receives current node.
It checks whether node is already visited.
If not visited:
print node
mark visited
recursively visit neighbours
Recursion continues until all reachable nodes are visited.
    # Check if node is not visited
    if node not in visited:

EXPLANATION :

if

if is a conditional statement.
It checks whether a condition is true or false.

node not in visited

node is the current node.
not in is a membership operator.
It checks whether the node is absent inside the visited set.

Example:

visited = {1,2,3}

If:

node = 4

Then:

4 not in visited

becomes True.

Why is this needed?

Graphs can contain cycles.
Example:
1 → 2 → 3 → 1
Without visited checking, DFS will run forever.
So we must avoid revisiting already visited nodes.

:

Colon starts the if-block.

What are we doing here?

We are checking whether the current node has already been visited.
If not visited, then only continue traversal.

Internal Working:

Python searches inside the set.
If node absent:
condition becomes True
Control enters the if-block.
        # Print current node
        print(node, end=" ")

EXPLANATION :

print()

print() is a built-in Python function.
It displays output on the screen.

node

Current node value gets printed.

end=" "

Normally print moves cursor to next line.
Example:
print(1)
print(2)

Output:

1
2

But:

print(1, end=" ")
print(2)

Output:

1 2
" " means a space is printed after every node.

Why needed?

To display traversal in one line.

What are we doing here?

We are printing the current node being visited in DFS traversal order.

Internal Working:

Current node value fetched.
Printed on console.
Cursor remains on same line.
        # Mark node as visited
        visited.add(node)

EXPLANATION :

visited

Set storing visited nodes.

.add()

add() is a set method.
It inserts a value into the set.

node

Current node added to visited set.

Why needed?

Prevents revisiting same node.
Avoids infinite loops.
Ensures efficient traversal.

Example:

Before:

visited = {1,2}

After:

visited.add(3)

Result:

visited = {1,2,3}

What are we doing here?

We are marking current node as visited.

Internal Working:

Python checks whether node already exists.
If not:
node inserted into set.
        # Visit all neighbours recursively
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

EXPLANATION :

for

Loop keyword.
Used for iteration.

neighbour

Variable storing neighbouring node one by one.

in

Membership/iteration keyword.

graph[node]

Access adjacency list of current node.

Example:

graph = {
    1:[2,3]
}

Then:

graph[1]

gives:

[2,3]

Meaning node 1 connects to nodes 2 and 3.

dfs(visited, graph, neighbour)

Recursive function call.
Function calls itself.

Why recursion?

DFS naturally works recursively.
It goes deep into graph before backtracking.

What are we doing here?

We are visiting every neighbouring node recursively.

Internal Working:

Suppose:

1 → 2 → 4

DFS steps:

Visit 1
Go to 2
Go to 4
No more neighbours
Return back to 2
Return back to 1

This returning process is called backtracking.

# BFS Function
def bfs(visited, graph, node, queue):

EXPLANATION :

bfs

Function name.
BFS means Breadth First Search.

Difference from DFS:

DFS goes depth-wise.
BFS goes level-wise.

Example:

    1
   / \
  2   3
 / \
4   5

DFS:

1 2 4 5 3

BFS:

1 2 3 4 5

queue

Queue data structure used in BFS.
Queue follows FIFO:
First In First Out

Why queue?

BFS processes nodes level by level.

What are we doing?

Creating BFS traversal function.
    # Mark starting node visited
    visited.add(node)

EXPLANATION :

Starting node added into visited set immediately.
Prevents revisiting.

What are we doing?

Marking BFS starting node as visited.
    # Insert node into queue
    queue.append(node)

EXPLANATION :

queue

List used as queue.

.append()

Inserts element at end of list.

Example:

queue = []
queue.append(1)

Result:

[1]

Why needed?

BFS begins from starting node.
Queue stores nodes waiting for processing.

What are we doing?

Adding first node into queue.
    # Continue until queue becomes empty
    while queue:

EXPLANATION :

while

Loop runs repeatedly while condition true.

queue

Non-empty list evaluates to True.
Empty list evaluates to False.

Meaning:

Continue BFS until queue becomes empty.

What are we doing?

Repeatedly processing nodes.

Internal Working:

Remove front node.
Visit neighbours.
Add unvisited neighbours.
Repeat until queue empty.
        # Remove first element from queue
        s = queue.pop(0)

EXPLANATION :

pop(0)

Removes first element from list.

Example:

queue = [1,2,3]
queue.pop(0)

Returns:

1

Remaining:

[2,3]

s

Stores removed node.

Why needed?

BFS processes nodes in FIFO order.

What are we doing?

Taking front node from queue for processing.
        # Print current node
        print(s, end=" ")

EXPLANATION :

Prints current BFS node.
end=" " keeps output on same line.

What are we doing?

Displaying BFS traversal order.
        # Visit all neighbours
        for neighbour in graph[s]:

EXPLANATION :

Iterating through neighbours of current node.

Example:

graph[1] = [2,3]

Loop visits:

2
3

What are we doing?

Exploring adjacent nodes.
            # If neighbour not visited
            if neighbour not in visited:

EXPLANATION :

Checks whether neighbour already processed.

Why needed?

Prevents duplicate visits and cycles.

What are we doing?

Filtering unvisited neighbours.
                # Mark visited
                visited.add(neighbour)

EXPLANATION :

Marks neighbour visited immediately.

Why immediate marking?

Prevents same node from entering queue multiple times.
                # Add into queue
                queue.append(neighbour)

EXPLANATION :

Adds neighbour into queue.
It will be processed later level-by-level.

What are we doing?

Scheduling neighbour for future traversal.
# Main Function
def main():

EXPLANATION :

main()

Main controlling function.
Organizes complete program flow.

What are we doing?

Creating main function to:
take input
create graph
call DFS
call BFS
    # Set for DFS visited nodes
    visited1 = set()

EXPLANATION :

set()

Creates empty set.

Why set?

Fast searching.
No duplicate values.

What are we doing?

Creating DFS visited set.
    # Set for BFS visited nodes
    visited2 = set()

EXPLANATION :

Separate visited set for BFS.
DFS already modifies visited1.

Why separate?

BFS should start fresh traversal.
    # Queue for BFS
    queue = []

EXPLANATION :

[]

Creates empty list.

Used as queue in BFS.

    # Input number of nodes
    n = int(input("Enter number of nodes : "))

EXPLANATION :

input()

Takes user input as string.

int()

Converts string into integer.

Example:

"5" → 5

n

Stores number of nodes.

What are we doing?

Taking graph size input.
    # Empty graph dictionary
    graph = dict()

EXPLANATION :

dict()

Creates empty dictionary.

Graph representation:

{
    node : [neighbours]
}

What are we doing?

Creating adjacency list graph.
    # Input graph
    for i in range(1, n + 1):

EXPLANATION :

range(1, n+1)

Generates numbers from 1 to n.

Example:

range(1,5)

gives:

1 2 3 4

What are we doing?

Taking graph data node-by-node.
        # Number of edges
        edges = int(input("Enter number of edges for node {} : ".format(i)))

EXPLANATION :

edges

Stores neighbour count.

.format(i)

Inserts node number inside string.

Example:

"Node {}".format(1)

Result:

Node 1

What are we doing?

Asking neighbour count for each node.
        # Create empty adjacency list
        graph[i] = list()

EXPLANATION :

graph[i]

Creates key for node.

list()

Empty neighbour list.

Example:

graph[1] = []
        # Input neighbours
        for j in range(1, edges + 1):

EXPLANATION :

Loop runs for every edge.

What are we doing?

Taking neighbour input.
            node = int(input("Enter edge {} for node {} : ".format(j, i)))

EXPLANATION :

Takes neighbour node input.

Example:

Enter edge 1 for node 1 : 2

Means:

node 1 connected to 2
            graph[i].append(node)

EXPLANATION :

.append()

Adds neighbour into adjacency list.

Example:

Before:

graph[1] = []

After:

graph[1].append(2)

Result:

graph[1] = [2]
    # DFS Traversal
    print("The following is DFS")

EXPLANATION :

Prints DFS heading.
    dfs(visited1, graph, 1)

EXPLANATION :

Starts DFS traversal from node 1.

Function receives:

visited set
graph
starting node
    print()

EXPLANATION :

Prints empty line.

Why needed?

Separates DFS and BFS output neatly.
    # BFS Traversal
    print("The following is BFS")

EXPLANATION :

Prints BFS heading.
    bfs(visited2, graph, 1, queue)

EXPLANATION :

Starts BFS traversal from node 1.
# Driver Code
if __name__ == "__main__":
    main()

EXPLANATION :

__name__

Special built-in Python variable.

When file runs directly:

__name__ = "__main__"

When imported:

it stores module name.

Meaning here:

Execute main() only if file runs directly.

What are we doing?

Starting program execution safely.
#tc- O(v+e)
#sc- O(v)

EXPLANATION :

tc

Time Complexity

O(v+e)

v = vertices
e = edges

Reason:

Every node visited once.
Every edge processed once.

sc

Space Complexity

O(v)

Reason:

Visited set stores nodes.
Queue/recursion stack also stores nodes.

Overall What Are We Doing In This Entire Code?

This program performs graph traversal using:

DFS (Depth First Search)
BFS (Breadth First Search)

Steps:

User creates graph.
Graph stored using adjacency list.
DFS explores graph deeply using recursion.
BFS explores graph level-wise using queue.
Traversal order printed on screen.

INPUT:
Enter number of nodes : 4

Enter number of edges for node 1 : 2
Enter edge 1 for node 1 : 2
Enter edge 2 for node 1 : 3

Enter number of edges for node 2 : 2
Enter edge 1 for node 2 : 1
Enter edge 2 for node 2 : 4

Enter number of edges for node 3 : 1
Enter edge 1 for node 3 : 1

Enter number of edges for node 4 : 1
Enter edge 1 for node 4 : 2

EXPLANATION :

This is the sample input given to the program.

Enter number of nodes : 4

Total nodes in graph = 4
Nodes are:
1
2
3
4

Now graph input starts node-by-node.

Enter number of edges for node 1 : 2

Node 1 has 2 neighbours.

Enter edge 1 for node 1 : 2

First neighbour of node 1 is node 2.

Enter edge 2 for node 1 : 3

Second neighbour of node 1 is node 3.

So currently:

graph[1] = [2,3]

Meaning:

1 → 2
1 → 3

Enter number of edges for node 2 : 2

Node 2 has 2 neighbours.

Enter edge 1 for node 2 : 1

Node 2 connected to node 1.

Enter edge 2 for node 2 : 4

Node 2 connected to node 4.

Now:

graph[2] = [1,4]

Meaning:

2 → 1
2 → 4

Enter number of edges for node 3 : 1

Node 3 has 1 neighbour.

Enter edge 1 for node 3 : 1

Node 3 connected to node 1.

Now:

graph[3] = [1]

Enter number of edges for node 4 : 1

Node 4 has 1 neighbour.

Enter edge 1 for node 4 : 2

Node 4 connected to node 2.

Now:

graph[4] = [2]

Final graph becomes:

graph = {
    1:[2,3],
    2:[1,4],
    3:[1],
    4:[2]
}

Graph representation:

    1
   / \
  2   3
  |
  4
The following is DFS
1 2 4 3

The following is BFS
1 2 3 4

EXPLANATION :

This is the output produced by the program.

DFS Traversal:

1 2 4 3

DFS means Depth First Search.

DFS always goes deeply first.

Step-by-step internal working:

Step 1:

Start from node 1
Print 1

Visited:

{1}

Step 2:

Go to first neighbour of 1
First neighbour = 2
Print 2

Visited:

{1,2}

Step 3:

Go to first neighbour of 2
First neighbour = 1
Already visited
Ignore it

Step 4:

Go to next neighbour of 2
Neighbour = 4
Print 4

Visited:

{1,2,4}

Step 5:

Node 4 neighbour = 2
Already visited
Return back

This returning process is called backtracking.

Step 6:

Return to node 1
Next neighbour = 3
Print 3

Visited:

{1,2,3,4}

DFS completed.

Final DFS Output:

1 2 4 3

BFS Traversal:

1 2 3 4

BFS means Breadth First Search.

BFS visits nodes level-by-level.

It uses queue.

Internal Working Step-by-Step:

Initial:

Queue:

[1]

Visited:

{1}

Step 1:

Remove 1 from queue
Print 1

Queue becomes:

[]

Add neighbours:

2
3

Queue:

[2,3]

Visited:

{1,2,3}

Step 2:

Remove 2
Print 2

Queue:

[3]

Neighbour:

1 already visited
4 unvisited

Add 4.

Queue:

[3,4]

Visited:

{1,2,3,4}

Step 3:

Remove 3
Print 3

Queue:

[4]

Neighbour:

1 already visited

Step 4:

Remove 4
Print 4

Queue:

[]

Traversal completed.

Final BFS Output:

1 2 3 4"""