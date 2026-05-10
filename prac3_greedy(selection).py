def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr

arr=[64,25,12,22,11]

print("Original Array :",arr)

selection_sort(arr)

print("Sorted Array :",arr)

#Time Complexity:O(n^2)
#Space Complexity:O(1)
"""
EXPLANATION :
def selection_sort(arr):


def is a keyword in Python.


def stands for "define".


It is used to create a function.


A function is a reusable block of code.


Instead of writing the same code again and again, we place it inside a function and call it whenever needed.


selection_sort is the name of the function.


This name is given by the programmer.


The function name should describe what the function does.


Here the function performs Selection Sort, so the name is selection_sort.


(arr) is called a parameter.


arr will store the list given to the function.


A parameter acts like a container that receives values from outside the function.


: is called a colon.


In Python, colon indicates the beginning of a block of code.


Everything written inside the function must be properly indented after the colon.


So this entire line means:
"Create a function named selection_sort that takes a list called arr as input."


INTERNAL WORKING :


When the function is called, Python creates memory for the function.


The list passed by the user gets stored inside arr.


Then Python starts executing the code written inside the function line by line.


    n=len(arr)


n is a variable.


Variables are used to store data temporarily in memory.


= is the assignment operator.


It assigns the value from the right side to the left side.


len() is a built-in Python function.


len stands for "length".


It counts how many elements are present inside the list.


arr is the list passed into the function.


Suppose:
arr=[64,25,12,22,11]


Then:
len(arr)
becomes:
5


So:
n=5


WHY THIS LINE IS NEEDED :


The algorithm must know how many elements are present.


This helps the loops know how many times they should run.


INTERNAL WORKING :


Python checks the list.


Counts all elements one by one.


Returns the count.


That count gets stored inside n.


    for i in range(n):


for is a loop keyword in Python.


A loop is used to repeat code multiple times automatically.


i is a loop variable.


It changes value during every iteration.


in is a keyword used to access elements from a sequence.


range(n) generates numbers starting from 0 up to n-1.


If:
n=5
then:
range(5)
generates:
0,1,2,3,4


: starts the loop block.


WHAT THIS LOOP DOES :


This is the outer loop of Selection Sort.


It controls each pass of sorting.


In every pass, the algorithm places one smallest element in its correct position.


INTERNAL WORKING :
PASS 1:


i=0


PASS 2:


i=1


PASS 3:


i=2


And so on.
        min_index=i


min_index is a variable.


It stores the index of the smallest element.


= assigns value.


Initially, the algorithm assumes:
"Current element itself is the smallest."


So:
min_index=i


EXAMPLE :
If:
i=0
Then:
min_index=0
WHY THIS IS NEEDED :


Selection Sort first assumes an element is minimum.


Then it checks the remaining elements.


If a smaller element is found, min_index changes.


INTERNAL WORKING :


Python stores the current position number inside min_index.


        for j in range(i+1,n):


This is the inner loop.


j is another loop variable.


range(i+1,n) means:
Start from the next element after i
and continue till n-1.


EXAMPLE :
If:
i=0n=5
Then:
range(1,5)
becomes:
1,2,3,4
WHY THIS LOOP IS NEEDED :


The algorithm compares the current element with all remaining elements.


It searches for the smallest value in the unsorted part of the list.


INTERNAL WORKING :


Python repeatedly changes j.


Each time it checks another element.


            if arr[j]<arr[min_index]:


if is a conditional statement.


It checks whether a condition is True or False.


arr[j]
means the element at index j.


<
is the less-than comparison operator.


arr[min_index]
means the current smallest element.


WHAT THIS CONDITION CHECKS :


"Is the new element smaller than the current minimum element?"


EXAMPLE :
Suppose:
arr=[64,25,12,22,11]
Current:
min_index=0
Then:
arr[min_index]=64
Now:
j=1arr[j]=25
Condition:
25<64
This becomes True.
INTERNAL WORKING :


Python fetches both values from memory.


Compares them.


If condition is True, the next line executes.


                min_index=j


If a smaller element is found:
update min_index.


EXAMPLE :
Previously:
min_index=0
Now:
j=1
So:
min_index=1
WHY THIS IS NEEDED :


The algorithm must always remember the position of the smallest element found so far.


INTERNAL WORKING :


Python replaces the old value stored in min_index with the new index.


        arr[i],arr[min_index]=arr[min_index],arr[i]


This line performs swapping.


Swapping means exchanging positions of two values.


LEFT SIDE:
arr[i],arr[min_index]
RIGHT SIDE:
arr[min_index],arr[i]
WHAT HAPPENS :


The smallest element moves to the correct position.


Current element moves to old minimum position.


EXAMPLE :
Before swap:
[64,25,12,22,11]
After first pass:
[11,25,12,22,64]
WHY THIS IS NEEDED :


Selection Sort places one smallest element correctly in every pass.


INTERNAL WORKING :


Python temporarily stores values internally.


Then exchanges them safely in one line.


    return arr


return is a keyword.


It sends data back from the function.


arr is the sorted list.


WHY THIS IS NEEDED :


After sorting is complete, the function should provide the final sorted list.


INTERNAL WORKING :


Function execution stops here.


Sorted array is returned to the place where function was called.


arr=[64,25,12,22,11]
EXPLANATION :


arr is a variable storing a list.


[] are square brackets.


They represent a list in Python.


Elements inside list are separated using commas ,.


The list contains unsorted numbers.


INTERNAL WORKING :


Python allocates memory for the list.


Stores all numbers sequentially.


print("Original Array :",arr)
EXPLANATION :


print() is a built-in Python function.


It displays output on the screen.


"Original Array :"
is a string.


,
separates multiple items inside print.


arr
prints the list.


OUTPUT :
Original Array : [64,25,12,22,11]
selection_sort(arr)
EXPLANATION :


This line calls the function.


Control goes inside the function.


Sorting starts.


The original list gets modified.


INTERNAL WORKING STEP-BY-STEP :
PASS 1:


Find smallest element


11 found


Swap with 64


Array becomes:
[11,25,12,22,64]
PASS 2:


Find smallest from remaining


12 found


Swap with 25


Array becomes:
[11,12,25,22,64]
PASS 3:


Find smallest from remaining


22 found


Swap with 25


Array becomes:
[11,12,22,25,64]
PASS 4:


25 already correct


PASS 5:


64 already correct


Final sorted array:
[11,12,22,25,64]
print("Sorted Array :",arr)
EXPLANATION :


Prints the sorted list after function execution.


OUTPUT :
Sorted Array : [11,12,22,25,64]
#Time Complexity:O(n^2)
EXPLANATION :


# is used for comments in Python.


Comments are ignored during execution.


O(n^2) means:
if elements increase,
comparisons increase quadratically.


WHY :


Nested loops are used.


Outer loop runs n times.


Inner loop also runs many times.


So:
n × n = n^2
#Space Complexity:O(1)
EXPLANATION :


Space Complexity means extra memory used.


O(1) means constant space.


WHY :


No extra array is created.


Sorting happens inside the same list.


WHAT ACTUALLY WE ARE DOING IN THIS CODE :


We are sorting numbers in ascending order using Selection Sort.


The algorithm repeatedly:


Finds the smallest element


Places it at the correct position




After every pass, one element gets fixed permanently.


Finally the entire array becomes sorted.


INPUT :
[64,25,12,22,11]
OUTPUT :
Original Array : [64,25,12,22,11]Sorted Array : [11,12,22,25,64]"""