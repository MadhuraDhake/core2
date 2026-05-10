# Number of vertices
V = 4

# Number of colors
m = 3

# Graph using adjacency matrix
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

# Store color assigned to each vertex
colors = [0] * V


# Check whether current color can be assigned
def isSafe(vertex, color):

    for i in range(V):

        # If adjacent vertex has same color
        if graph[vertex][i] == 1 and colors[i] == color:
            return False

    return True


# Backtracking function
def solve(vertex):

    # All vertices colored
    if vertex == V:
        return True

    # Try all colors
    for color in range(1, m + 1):

        if isSafe(vertex, color):

            # Assign color
            colors[vertex] = color

            print(f"Color {color} assigned to Vertex {vertex}")

            # Recursive call
            if solve(vertex + 1):
                return True

            # Backtracking
            print(f"Backtracking from Vertex {vertex}")

            colors[vertex] = 0

    return False


# Start coloring from vertex 0
if solve(0):

    print("\nSolution Found")

    for i in range(V):
        print(f"Vertex {i} ---> Color {colors[i]}")

else:
    print("No Solution Exists")

    # tc and sc = O(v)
    #worst case = O(m^v)
    """
    V = 4

EXPLANATION :

V

Variable name used to store the number of vertices present in the graph.

=

Assignment operator.
Used to store the value from the right side into the variable on the left side.

4

Integer value.
Represents total number of vertices in the graph.

What are we actually doing here?

We are defining the size of the graph.
The graph contains 4 vertices:
Vertex 0
Vertex 1
Vertex 2
Vertex 3

Internally what happens?

Python creates memory for variable V.
Value 4 gets stored inside it.
m = 3

EXPLANATION :

m

Variable used to store the number of colors available.

=

Assignment operator.

3

Integer value.
Means 3 colors are available for coloring the graph.

What are we actually doing here?

We are telling the program that only 3 colors can be used.

Internally what happens?

Python stores value 3 in variable m.

Later the program will try:

Color 1
Color 2
Color 3
graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

EXPLANATION :

graph

Variable name used to store the graph structure.

=

Assignment operator.

[ ]

Square brackets represent lists in Python.
Since multiple lists are inside another list, this becomes a 2D list or matrix.

This matrix is called an adjacency matrix.

Meaning of values:

1 → connection exists between two vertices.
0 → no connection exists.

First row:

[0, 1, 1, 1]

Meaning:

Vertex 0 connected to Vertex 1
Vertex 0 connected to Vertex 2
Vertex 0 connected to Vertex 3

Second row:

[1, 0, 1, 0]

Meaning:

Vertex 1 connected to Vertex 0
Vertex 1 connected to Vertex 2

Third row:

[1, 1, 0, 1]

Meaning:

Vertex 2 connected to Vertex 0
Vertex 2 connected to Vertex 1
Vertex 2 connected to Vertex 3

Fourth row:

[1, 0, 1, 0]

Meaning:

Vertex 3 connected to Vertex 0
Vertex 3 connected to Vertex 2

What are we actually doing here?

We are creating the graph structure.
The program will use this matrix to check adjacency between vertices.

Internally what happens?

Python creates nested lists in memory.
Each value can be accessed using indexes like:
graph[0][1]

Meaning:

Row 0
Column 1

Value is 1.

So Vertex 0 and Vertex 1 are connected.

colors = [0] * V

EXPLANATION :

colors

Variable used to store color assigned to every vertex.

=

Assignment operator.

[0]

Creates a list containing one element 0.

*

Repetition operator for lists.

V

Number of times list should repeat.

Since V = 4, this becomes:

[0, 0, 0, 0]

Meaning:

No vertex is colored initially.

What are we actually doing here?

We are preparing storage for color assignments.

Internally what happens?

Python creates a list with 4 positions.

Current state:

Vertex	Color
0	0
1	0
2	0
3	0
def isSafe(vertex, color):

EXPLANATION :

def

Keyword used to define a function in Python.

isSafe

Function name.
Indicates this function checks whether assigning a color is safe.

( )

Parentheses contain parameters.

vertex

Parameter storing current vertex number.

color

Parameter storing current color to check.

:

Marks start of function body.

What are we actually doing here?

We are creating a function that checks:

"Can this vertex use this color without conflict?"

Internally what happens?

Python stores function definition in memory.
Function executes only when called.
for i in range(V):

EXPLANATION :

for

Loop keyword.
Used for repetition.

i

Loop variable.

in

Keyword used for iteration.

range(V)

Generates values from 0 to V-1.

Since V = 4:

0, 1, 2, 3

:

Starts loop body.

What are we actually doing here?

We are checking all vertices one by one.

Internally what happens?

Iteration 1:

i = 0

Iteration 2:

i = 1

Iteration 3:

i = 2

Iteration 4:

i = 3
if graph[vertex][i] == 1 and colors[i] == color:
    return False

EXPLANATION :

if

Conditional statement.

graph[vertex][i]

Accesses adjacency matrix value.

Example:

graph[1][0]

Checks whether Vertex 1 and Vertex 0 are connected.

== 1

Checks whether connection exists.

and

Logical operator.
Both conditions must be true.

colors[i]

Color assigned to vertex i.

== color

Checks whether adjacent vertex already has same color.

return False

Function immediately stops.
Returns False.

Meaning:

Current color assignment is invalid.

What are we actually doing here?

Preventing adjacent vertices from having same color.

Internally step-by-step:

Suppose:

colors = [1,0,0,0]

Trying:

isSafe(1,1)

Program checks:

graph[1][0] == 1

True.

Then:

colors[0] == 1

True.

So:

return False

Because adjacent vertices cannot share same color.

return True

EXPLANATION :

return

Sends value back to function caller.

True

Boolean value meaning success.

What are we actually doing here?

Approving the color assignment because no conflict was found.

Internally what happens?

Function finishes execution.
Control returns to caller function.
def solve(vertex):

EXPLANATION :

def

Function definition keyword.

solve

Function name.
Used to solve graph coloring problem.

vertex

Parameter representing current vertex.

:

Starts function body.

What are we actually doing here?

We are creating a recursive backtracking function.

Purpose:

Try colors
Check safety
Move to next vertex
Backtrack if needed
if vertex == V:
    return True

EXPLANATION :

if

Conditional statement.

vertex == V

Checks whether all vertices are colored.

Example:

If:

V = 4

Vertices are:

0,1,2,3

When recursion reaches:

vertex = 4

It means all vertices are already processed.

return True

Solution found successfully.

What are we actually doing here?

Stopping recursion after successful coloring.
for color in range(1, m + 1):

EXPLANATION :

for

Loop keyword.

color

Loop variable storing current color.

range(1, m + 1)

Generates colors from 1 to m.

Since:

m = 3

Values become:

1,2,3

Why m + 1?

Python excludes last value in range.

So:

range(1,4)

Produces:

1,2,3

What are we actually doing here?

Trying every possible color for current vertex.
if isSafe(vertex, color):

EXPLANATION :

isSafe(vertex, color)

Function call.
Checks whether current color can be assigned safely.

If safe:

Condition becomes True.
Program enters block.

What are we actually doing here?

Verifying color validity before assignment.
colors[vertex] = color

EXPLANATION :

colors[vertex]

Accesses current vertex position.

=

Assignment operator.

color

Current color value.

Example:

colors[0] = 1

Meaning:

Vertex 0 gets Color 1.

Internally:

Before:

[0,0,0,0]

After:

[1,0,0,0]
print(f"Color {color} assigned to Vertex {vertex}")

EXPLANATION :

print()

Displays output on screen.

f""

f-string formatting.

{color}

Replaced with actual color value.

{vertex}

Replaced with actual vertex value.

Example output:

Color 1 assigned to Vertex 0

What are we actually doing here?

Showing current assignment step to user.
if solve(vertex + 1):
    return True

EXPLANATION :

solve(vertex + 1)

Recursive function call.
Moves to next vertex.

Example:

If current vertex is:

0

Next call becomes:

solve(1)

return True

If recursive call succeeds, stop further processing.

What are we actually doing here?

Continuing coloring process recursively.

Internally step-by-step:

Current vertex colored
Move to next vertex
Try colors again
Continue until all vertices colored
print(f"Backtracking from Vertex {vertex}")

EXPLANATION :

print()

Displays output.

f""

Formatted string.

Example output:

Backtracking from Vertex 2

What are we actually doing here?

Informing that current choice failed.
Program will undo current color assignment.
colors[vertex] = 0

EXPLANATION :

colors[vertex]

Access current vertex color.

= 0

Removes assigned color.

Example:

Before:

[1,2,3,0]

After:

[1,2,0,0]

What are we actually doing here?

Undoing wrong choice.
Trying another possible color.

This process is called backtracking.

return False

EXPLANATION :

return

Sends value back.

False

Boolean value meaning failure.

What are we actually doing here?

Indicating no valid color worked for current vertex.
if solve(0):

EXPLANATION :

solve(0)

Starts recursive graph coloring from Vertex 0.

if

Checks whether solution exists.

If solution found:

Condition becomes True.

What are we actually doing here?

Starting entire graph coloring process.
print("\nSolution Found")

EXPLANATION :

print()

Displays output.

\n

Newline character.
Moves output to next line.

Displays:

Solution Found
for i in range(V):
    print(f"Vertex {i} ---> Color {colors[i]}")

EXPLANATION :

for

Loop keyword.

i

Loop variable.

range(V)

Generates vertex numbers.

print()

Displays output.

colors[i]

Accesses assigned color.

Example output:

Vertex 0 ---> Color 1

What are we actually doing here?

Printing final coloring result.
else:
    print("No Solution Exists")

EXPLANATION :

else

Executes when if solve(0) becomes False.

print()

Displays output.

Meaning:

Graph cannot be colored using given number of colors.

Output:

No Solution Exists

INPUT :

No manual input from user.

Predefined values:

V = 4
m = 3

Graph:

0 -- 1
|  / |
| /  |
2 -- 3

OUTPUT :

Color 1 assigned to Vertex 0
Color 2 assigned to Vertex 1
Color 3 assigned to Vertex 2
Color 2 assigned to Vertex 3

Solution Found
Vertex 0 ---> Color 1
Vertex 1 ---> Color 2
Vertex 2 ---> Color 3
Vertex 3 ---> Color 2

What is Graph Coloring?

Graph Coloring is a problem in graph theory where we assign colors to vertices (nodes) of a graph in such a way that:

No two adjacent vertices should have the same color.

Adjacent vertices means:

Vertices directly connected by an edge.
What are we actually doing in this problem?

We are trying to color all vertices of a graph using a limited number of colors while following one important rule:

Connected vertices cannot have the same color.

The program checks:

Is it possible to color the graph?
If yes, what color should each vertex get?
Why is this problem used?

Graph coloring is used in real-life situations where:

Two connected things cannot share the same resource.

Examples:

Situation	Meaning of Colors
Exam timetable	Different exam time slots
Map coloring	Different region colors
WiFi channels	Different frequencies
Register allocation in compiler	Different CPU registers
Task scheduling	Different time slots
Example of Graph Coloring

Suppose we have this graph:

A ----- B
|       |
|       |
C ----- D

Connections:

A connected to B and C
B connected to A and D
C connected to A and D
D connected to B and C

Now suppose we use:

Red
Blue

Possible coloring:

Vertex	Color
A	Red
B	Blue
C	Blue
D	Red

This works because:

Connected vertices have different colors.
What happens if adjacent vertices have same color?

Example:

Vertex	Color
A	Red
B	Red

If A and B are connected:

This becomes invalid.

Because graph coloring rule says:

Adjacent vertices cannot share same color.
What is the goal of this code?

This code tries to:

Start from first vertex
Try a color
Check if color is safe
If safe:
assign color
move to next vertex
If not safe:
try another color
If all colors fail:
backtrack
remove previous color
try different combination
What is Backtracking here?

Backtracking means:

Try something
If it fails later
Undo it
Try another option

Example:

Suppose:

Vertex 0 = Color 1
Vertex 1 = Color 2
Vertex 2 = Color 2

Now if Vertex 2 conflicts:

Remove its color
Try another color

This undo process is called backtracking.

What are vertices in this problem?

Vertices are nodes of graph.

In your code:

V = 4

Vertices are:

0
1
2
3
What are edges?

Edges are connections between vertices.

Example:

0 ----- 1

Means:

Vertex 0 connected to Vertex 1
What is the graph in your code?

Your graph:

graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

Visual form:

      1
     / \
    0---2
     \ /
      3

Connections:

0 connected to 1,2,3
1 connected to 0,2
2 connected to 0,1,3
3 connected to 0,2
Why do we need isSafe()?

Before assigning a color, we must check:

Is any adjacent vertex already using this color?

If yes:

Color is unsafe.

If no:

Color is safe.
Why recursion is used?

Because:

We solve one vertex at a time.
After coloring one vertex, we move to next vertex.
Same process repeats again and again.

Recursion helps automate this repeated process.

Why multiple colors are tried?

Because:

One color may create conflict.
Another color may work.

So program tries:

Color 1
Color 2
Color 3

for every vertex.

What is the final output of this code?

The code gives valid color assignment.

Example:

Vertex 0 ---> Color 1
Vertex 1 ---> Color 2
Vertex 2 ---> Color 3
Vertex 3 ---> Color 2

Meaning:

Vertex	Color
0	1
1	2
2	3
3	2

And no connected vertices share same color.

Step-by-step working of your code

Initial state:

Vertex 0 = uncolored
Vertex 1 = uncolored
Vertex 2 = uncolored
Vertex 3 = uncolored

Step 1:
Try Vertex 0

Color 1 is safe

Assign:

Vertex 0 = Color 1

Step 2:
Move to Vertex 1

Color 1 not safe because Vertex 0 already has Color 1
Try Color 2
Safe

Assign:

Vertex 1 = Color 2

Step 3:
Move to Vertex 2

Color 1 not safe
Color 2 not safe
Color 3 safe

Assign:

Vertex 2 = Color 3

Step 4:
Move to Vertex 3

Color 1 not safe
Color 2 safe

Assign:

Vertex 3 = Color 2

All vertices colored successfully.

Solution found.
    """