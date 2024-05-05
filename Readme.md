Asymptotic Notation
----------------------

1. Omega Notation (Best Case; Minimum time or space taken)
    - Lower Bound of an Algorimthm
2. Theta Notation (Avg Case)
    - Middle of Upper and Lower Bound of an Algorimthm
3. Big O Notation (Worst Case; Maximum time or space taken)
    - Upper Bound of an Algorimthm
    - `We always interested to finding max time taken by algorithms` 
    - `kyoki hum chahte hai ki max hi sabse kam ho aur esi ko kam karne ki koshish karte hai.`


Rules to find Big O
---------------------

Sorting Algorithms
-------------------

Bubble Sort (Sinking or Exchange Sort)
-----------
```code
for i in range(len(arr)){
    
}
```

2d array
-------------
```py
array = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

array = [ [1,2,3],[4,5,6],[7,8,9] ]

array = [row[col,col,col],row[col,col,col],row[col,col,col]]


arr[row][col]

arr[0][1] = 2
arr[3][1] = 7
```


In Python, both generators and simple functions serve different purposes and have distinct characteristics. Here are the main differences between them:

Execution:

A simple function executes its entire code block every time it's called. When you call a function, it runs from start to finish, and any local variables are re-initialized.
A generator function, on the other hand, generates a sequence of values lazily using the yield keyword. Each time a value is yielded, the function's state is saved, allowing it to resume execution from where it left off the next time it's called. This makes generators suitable for iterating over large sequences without needing to store the entire sequence in memory at once.
Memory Usage:

Simple functions may create and manipulate large data structures, potentially consuming a lot of memory, especially if they return large data sets.
Generators are memory-efficient because they generate values on-the-fly, one at a time, and only store the state of the generator function, not the entire sequence of generated values. This makes them particularly useful when dealing with large or infinite sequences.
Iteration:

With simple functions, you typically use a return statement to return a computed value or a collection of values. You can then iterate over the returned value(s) using loops or other iterable methods.
Generators use the yield statement to produce a sequence of values one at a time. You can iterate over these values using a loop or by passing the generator   object to functions like next() or using constructs like for ... in ....
State:

Simple functions do not maintain any internal state between calls. Each time you call the function, it starts execution from the beginning.
Generators maintain their internal state between calls. They remember where they left off when yielding a value and resume execution from that point the next time they're called. This allows generators to produce a sequence of values incrementally.
In summary, simple functions are used to execute a block of code and return a value(s), while generators are used to lazily generate sequences of values, making them more memory-efficient, especially for large or infinite sequences.





## Space and Time Complexity

time complexity : O(1) < O(log N) < O(N) < O(N log N) < O(2^N)


## Some logical notes:

AND (&): The result is 1 only if all corresponding bits in the inputs are 1.
Shortcut: "All bits must be 1 to get 1."

1 & 1 & 1 &.... -> 1
0 & 1 & 1 ... -> 0  when it gets 0, not check any further input bit

OR (|): The result is 1 if any corresponding bit in the inputs is 1.
Shortcut: "Any bit being 1 results in 1."

0 & 0 & 0 & 0 & 1 -> 1
1 & 0 & 0 & 0... -> 1 when it gets 1, not check any further input bit

XOR (^): The result is 1 if the number of corresponding bits that are 1 is odd.
Shortcut: "Odd number of 1s result in 1."

NOT (~): It simply flips each bit of the input.
Shortcut: "Flips all the bits."




## some notes on array with time complexity?


O(N), Only one traversal is needed, i.e, i from 0 to n and j from n-1 to 0 with at most 2*N steps. The above approach will also work for the M x N matrix (not only for N x N). Complexity would be O(M + N)



