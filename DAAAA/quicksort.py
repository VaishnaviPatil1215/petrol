
import random
import time

# Deterministic Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


# Randomized Quick Sort
def random_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = random.choice(arr)
    arr.remove(pivot)

    left = [x for x in arr if x <= pivot]
    right = [x for x in arr if x > pivot]

    return random_quick_sort(left) + [pivot] + random_quick_sort(right)


# Main Program
arr = [45, 12, 89, 23, 5, 67, 34, 10]

start = time.time()
print("Deterministic Sorted:", quick_sort(arr.copy()))
print("Deterministic Time:", time.time() - start)

start = time.time()
print("Randomized Sorted:", random_quick_sort(arr.copy()))
print("Randomized Time:", time.time() - start)















'''sample output

Deterministic Sorted: [5, 10, 12, 23, 34, 45, 67, 89]
Deterministic Time: 0.00001

Randomized Sorted: [5, 10, 12, 23, 34, 45, 67, 89]
Randomized Time: 0.00002



Experiment: Analysis of Quick Sort using Deterministic and Randomized Variants
Let's understand this program from absolute basics, assuming you are learning Quick Sort for the first time. We'll go through every block, every line, why it is used, how it works, and examples.
1. First understand the concept
Before understanding the code, let's understand what Quick Sort is.

What is Quick Sort?

Quick Sort is a sorting algorithm used to arrange elements in ascending or descending order.

It follows the Divide and Conquer technique.

Divide and Conquer means:
1. Divide the given problem into smaller problems.
2. Solve those smaller problems.
3. Combine the results to get the final answer.
Quick Sort works using three main steps:
- Pivot: Select one element from the array as a pivot.
- Partition: Divide the remaining elements into two groups:
  - Left: Elements smaller than or equal to the pivot.
  - Right: Elements greater than the pivot.
- Recursion: Apply the same process to the left and right groups until the array is sorted.
Example of Quick Sort
Suppose we have this array:
[45, 12, 89, 23, 5]



Step 1: Select a pivot

For deterministic Quick Sort, we select the first element.

Pivot = 45

Step 2: Divide the elements
- Left elements (smaller than or equal to 45): [12, 23, 5]
- Right elements (greater than 45): [89]
Now:
[12, 23, 5] + [45] + [89]


Step 3: Repeat the process

Sort the left part [12, 23, 5].

Choose 12 as the pivot.
- Left = [5]
- Right = [23]
Now:
[5] + [12] + [23]


The right part [89] already has one element, so it is sorted.

Final sorted array:
[5, 12, 23, 45, 89]


This is how Quick Sort works.

2. Block-by-block code explanation
Block 1: Importing libraries
Code:
import randomimport time



Line 1: import random
- random is a built-in Python module.
- It is used to generate random values or select random elements.
- In our program, it is used in Randomized Quick Sort to select a random pivot.
Example:
import randomarr = [10, 20, 30, 40]print(random.choice(arr))



Possible output:
30


The output can change every time because the element is selected randomly.

Why do we use it?

In Randomized Quick Sort, we don't always select the first element as a pivot. We select any random element from the array.

Line 2: import time
- time is another built-in Python module.
- It is used to measure the execution time of the program.
- We use it to compare how much time Deterministic and Randomized Quick Sort take to sort the same array.
Example:
import timestart = time.time()print("Hello")end = time.time()print(end - start)



Here:
- start stores the starting time.
- end stores the ending time.
- end - start gives the total execution time in seconds.
Why do we use it?

Our experiment is about the analysis of Quick Sort. Therefore, we need to measure and compare the execution time of both algorithms.
Block 2: Deterministic Quick Sort
Code:
def quick_sort(arr):    if len(arr) <= 1:        return arr    pivot = arr[0]    left = [x for x in arr[1:] if x <= pivot]    right = [x for x in arr[1:] if x > pivot]    return quick_sort(left) + [pivot] + quick_sort(right)



This function implements Deterministic Quick Sort.

Let's understand every line.

Line 1: def quick_sort(arr):
- def is a Python keyword used to define a function.
- quick_sort is the name of our function.
- arr is the parameter that receives the array we want to sort.
Example:
quick_sort([45, 12, 89, 23])



Here, the array [45, 12, 89, 23] is passed to the function.

Why do we use a function?

We use a function because Quick Sort needs to call itself repeatedly to sort smaller parts of the array.

Line 2: if len(arr) <= 1:

Let's break this down:
- len(arr) returns the number of elements in the array.
- <= means less than or equal to.
- The condition checks whether the array has zero or one element.
Examples:
len([10])       # 1len([])         # 0len([10, 20])   # 2



Why do we use this condition?

This is called the Base Case of recursion.

An array containing zero or one element is already sorted. There is no need to divide it further.

Line 3: return arr
- return sends the result back to the function that called it.
- If the array has zero or one element, we simply return it.
Example:
quick_sort([10])



Output:
[10]


This stops the recursive calls.

Line 4: pivot = arr[0]
- A pivot is an element used to divide the array into two parts.
- arr[0] accesses the first element of the array.
- We store that element in a variable called pivot.
Example:
arr = [45, 12, 89, 23]pivot = arr[0]print(pivot)



Output:
45


Why do we use it?

In Deterministic Quick Sort, we always select the first element as the pivot.

This makes pivot selection fixed and predictable.

Line 5: left = [x for x in arr[1:] if x <= pivot]

This line creates a list containing all elements smaller than or equal to the pivot.

Let's understand its parts:
- arr[1:] means all elements except the first element.
- x represents each element being checked.
- if x <= pivot checks whether the element is smaller than or equal to the pivot.
- If the condition is true, that element is added to the left list.
This is called List Comprehension in Python.

Example:
arr = [45, 12, 89, 23, 5]pivot = 45left = [x for x in arr[1:] if x <= pivot]print(left)



Output:
[12, 23, 5]


Why do we use it?

We need to separate smaller elements from larger elements so that the pivot can be placed in its correct sorted position.

Line 6: right = [x for x in arr[1:] if x > pivot]

This line creates a list containing all elements greater than the pivot.

Let's understand:
- arr[1:] selects all elements except the pivot.
- x represents each element.
- if x > pivot checks whether an element is greater than the pivot.
- If true, the element is added to the right list.
Example:
arr = [45, 12, 89, 23, 5]pivot = 45right = [x for x in arr[1:] if x > pivot]print(right)



Output:
[89]


Why do we use it?

We separate larger elements so that they can be sorted independently on the right side of the pivot.

Line 7–8:
return quick_sort(left) + [pivot] + quick_sort(right)



This is the most important line of the algorithm.

Let's break it into three parts:
1. quick_sort(left) – Recursively sorts the left subarray.
2. [pivot] – Places the pivot between the two sorted subarrays.
3. quick_sort(right) – Recursively sorts the right subarray.
The + operator joins the three lists together.

Example:
left = [12, 5]pivot = 45right = [89]



After recursively sorting the left and right lists:
[5, 12] + [45] + [89]


Result:
[5, 12, 45, 89]


Why do we use recursion?

Because the left and right subarrays may not be sorted. We call the same function again until each subarray contains zero or one element.

This is how Deterministic Quick Sort works.
Block 3: Randomized Quick Sort
Code:
def random_quick_sort(arr):    if len(arr) <= 1:        return arr    pivot = random.choice(arr)    arr.remove(pivot)    left = [x for x in arr if x <= pivot]    right = [x for x in arr if x > pivot]    return random_quick_sort(left) + [pivot] + random_quick_sort(right)



This function implements Randomized Quick Sort.

It is almost similar to Deterministic Quick Sort. The main difference is how the pivot is selected.

Let's understand each line.

Line 1: def random_quick_sort(arr):
- def is used to define a function.
- random_quick_sort is the function name.
- arr is the input array that needs to be sorted.
We create a separate function because we want to implement and analyze the randomized version independently.

Line 2: if len(arr) <= 1:

This checks whether the array contains zero or one element.
- If the array is empty, it is already sorted.
- If the array contains one element, it is already sorted.
Example:
random_quick_sort([10])



Output:
[10]


This is the base case of recursion.

Line 3: return arr

If the array contains zero or one element, we return it without performing any sorting.

This prevents unnecessary recursive calls.

Line 4: pivot = random.choice(arr)

This is the most important line in Randomized Quick Sort.
- random.choice() is a function from the random module.
- It selects one random element from the given list.
- That element is stored in the variable pivot.
Example:
import randomarr = [45, 12, 89, 23, 5]pivot = random.choice(arr)print(pivot)



Possible output:
23


Another time, it might select:
45


Or:
5


Why do we use it?

Unlike Deterministic Quick Sort, which always selects the first element, Randomized Quick Sort selects a random element.

This reduces the chances of repeatedly selecting a bad pivot and getting unbalanced partitions.

Line 5: arr.remove(pivot)
- remove() is a Python list method.
- It removes the first occurrence of the specified element from the list.
- Here, it removes the selected pivot from the array.
Example:
arr = [45, 12, 89, 23, 5]pivot = 23arr.remove(pivot)print(arr)



Output:
[45, 12, 89, 5]


Why do we use it?

We remove the pivot because we want to divide only the remaining elements into left and right subarrays.

The pivot will be added back between the two sorted subarrays in the return statement.

Line 6: left = [x for x in arr if x <= pivot]

This creates a list of all elements smaller than or equal to the selected pivot.

Example:
arr = [45, 12, 89, 5]pivot = 23left = [x for x in arr if x <= pivot]print(left)



Output:
[12, 5]


Why do we use it?

To place all smaller elements on the left side of the pivot.

Line 7: right = [x for x in arr if x > pivot]

This creates a list containing all elements greater than the pivot.

Example:
arr = [45, 12, 89, 5]pivot = 23right = [x for x in arr if x > pivot]print(right)



Output:
[45, 89]


Why do we use it?

To place all larger elements on the right side of the pivot.

Line 8–9:
return random_quick_sort(left) + [pivot] + random_quick_sort(right)



This line combines the sorted left subarray, pivot and sorted right subarray.

Let's understand the three parts:
1. random_quick_sort(left) recursively sorts the left subarray.
2. [pivot] places the selected pivot in between.
3. random_quick_sort(right) recursively sorts the right subarray.
Example:
Left  = [12, 5]
Pivot = 23
Right = [45, 89]


After recursive sorting:
[5, 12] + [23] + [45, 89]


Final result:
[5, 12, 23, 45, 89]


Why do we use recursion here?

Because the left and right subarrays may contain multiple unsorted elements. We repeatedly apply the same process until all subarrays are sorted.
Difference between the two Quick Sort functions
Deterministic Quick Sort	Randomized Quick Sort
Selects the first element as pivot.	Selects a random element as pivot.
Uses arr[0].	Uses random.choice(arr).
Pivot selection is fixed.	Pivot selection changes randomly.
Can perform poorly on certain input arrangements.	Reduces the likelihood of repeatedly getting poor partitions.


Block 4: Main Program
Code:
arr = [45, 12, 89, 23, 5, 67, 34, 10]



This line creates the input array.

An array (called a list in Python) is a collection of elements stored together.

Our input is:
[45, 12, 89, 23, 5, 67, 34, 10]


It contains 8 elements in an unsorted order.

Why do we use this?

We need an input array to test both sorting algorithms and compare their execution times.
Block 5: Measuring Deterministic Quick Sort time
Code:
start = time.time()print("Deterministic Sorted:", quick_sort(arr.copy()))print("Deterministic Time:", time.time() - start)



Let's understand each line.

Line 1: start = time.time()
- time.time() returns the current time in seconds.
- We store this value in the variable start.
It records when the sorting process begins.

Line 2: print("Deterministic Sorted:", quick_sort(arr.copy()))

This line performs sorting and displays the result.

Let's break it down:
- print() displays the output on the screen.
- "Deterministic Sorted:" is the message displayed before the sorted array.
- quick_sort() calls our Deterministic Quick Sort function.
- arr.copy() creates a separate copy of the original array.
Why do we use arr.copy()?

We use it to preserve the original array.

This ensures both sorting algorithms receive the same input.

For example:
arr = [45, 12, 89]new_arr = arr.copy()print(new_arr)



Output:
[45, 12, 89]


The original array remains unchanged.

Line 3: print("Deterministic Time:", time.time() - start)

This calculates and displays the execution time.
- time.time() gets the current time again.
- start contains the starting time.
- Subtracting the starting time from the current time gives the elapsed time.
Formula:
text{Execution Time} = text{End Time} - text{Start Time}


Example:
Start Time = 100.20
End Time   = 100.25

Execution Time = 0.05 seconds


This tells us how long Deterministic Quick Sort took to execute.
Block 6: Measuring Randomized Quick Sort time
Code:
start = time.time()print("Randomized Sorted:", random_quick_sort(arr.copy()))print("Randomized Time:", time.time() - start)



This block is similar to the previous block, but here we measure Randomized Quick Sort.

Line 1: start = time.time()

Records the starting time of Randomized Quick Sort.

Line 2: print("Randomized Sorted:", random_quick_sort(arr.copy()))
- Calls the Randomized Quick Sort function.
- Passes a copy of the original array.
- Sorts the array using a randomly selected pivot.
- Displays the sorted result.
Line 3: print("Randomized Time:", time.time() - start)

Calculates and displays the total execution time of Randomized Quick Sort.

Why do we use two separate time measurements?

We want to compare the performance of both algorithms independently.

Both algorithms receive the same input, so we can compare their execution times.

3. Sample Input and Output
Sample Input:
arr = [45, 12, 89, 23, 5, 67, 34, 10]



Sample Output:
Deterministic Sorted: [5, 10, 12, 23, 34, 45, 67, 89]
Deterministic Time: 0.00002
Randomized Sorted: [5, 10, 12, 23, 34, 45, 67, 89]
Randomized Time: 0.00003


Note: These are illustrative execution times. Your actual output will vary depending on your computer and system load. Both algorithms will produce the same sorted array.

What do we understand from the output?
1. Both algorithms successfully sort the given array.
2. Both produce the same sorted result.
3. Their execution times may be different.
4. Randomized Quick Sort selects different pivots, so its execution time can vary between runs.
4. Time Complexity Analysis
Time complexity tells us how the execution time of an algorithm increases as the input size increases.

Quick Sort has three cases:
Case	Time Complexity	Explanation
Best Case	O(n log n)	Pivot divides the array into nearly equal parts.
Average Case	O(n log n)	Partitions are reasonably balanced on average.
Worst Case	O(n²)	Pivot repeatedly creates highly unbalanced partitions.

Here, n represents the number of elements in the array.
Understanding each case
1. Best Case – O(n log n)

When the pivot divides the array into two nearly equal parts, sorting becomes efficient.

Example:
[10, 20, 30, 40, 50, 60, 70]


If 40 is selected as the pivot:
Left  = [10, 20, 30]
Pivot = 40
Right = [50, 60, 70]


Both parts contain approximately equal elements.

Therefore, the time complexity is O(n log n).

2. Average Case – O(n log n)

In average conditions, the pivot divides the array into reasonably balanced parts.

The algorithm repeatedly divides and sorts these parts.

Therefore, the average time complexity is O(n log n).

3. Worst Case – O(n²)

When the pivot is repeatedly the smallest or largest element, one partition becomes empty and the other contains almost all remaining elements.

Example:
[10, 20, 30, 40, 50]


If the first element is always selected as the pivot:
Pivot = 10
Left  = []
Right = [20, 30, 40, 50]


Again:
Pivot = 20
Left  = []
Right = [30, 40, 50]


This continues until the entire array is sorted.

Therefore, the time complexity becomes O(n²).
Complexity of both variants
Complexity	Deterministic	Randomized
Best Case	O(n log n)	O(n log n)
Average Case	O(n log n)	O(n log n) expected
Worst Case	O(n²)	O(n²)

Important: Randomized Quick Sort has O(n log n) expected time because random pivot selection makes consistently unbalanced partitions less likely. However, its worst case is still O(n²).
5. Space Complexity Analysis
Space complexity tells us how much additional memory an algorithm requires while executing.

For your particular Python implementation:
Case	Auxiliary Space Complexity
Average	O(n)
Worst	O(n²)

Why?
- Both implementations create additional left and right lists.
- They also use recursive function calls.
- In balanced partitions, the additional lists and recursion require approximately O(n) peak space.
- In highly unbalanced partitions, the lists retained during recursive calls can require O(n²) peak space.
The recursion stack alone requires O(log n) space on average and O(n) in the worst case.

Note: These space complexities apply to your list-based implementation, not necessarily to the standard in-place Quick Sort implementation.
6. Example of the complete concept
Let's take one example and understand both algorithms together.

Input:
arr = [30, 10, 50, 20, 40]



A. Deterministic Quick Sort
Rule: Always select the first element as pivot.
Step 1: Select pivot = 30
10, 20
Left
30
Pivot
50, 40
Right

Step 2: Sort left and right parts
- Left [10, 20]: Pivot = 10
- Right [50, 40]: Pivot = 50
Step 3: Combine
[10] + [20] + [30] + [40] + [50]


Final sorted array
[10, 20, 30, 40, 50]



B. Randomized Quick Sort
Rule: Select a random element as pivot.

Suppose the randomly selected pivot is 40.
Step 1: Select pivot = 40
30, 10, 20
Left
40
Pivot
50
Right

Step 2: Sort left and right parts
- Left [30, 10, 20]: A random pivot is selected.
- Right [50]: Already sorted.
Step 3: Combine
[10, 20, 30] + [40] + [50]


Final sorted array
[10, 20, 30, 40, 50]



Notice that both algorithms produce the same sorted array. The difference is only in the way they select their pivots.

7. Important Python terms used in this program
These are useful to remember for your practical examination.
Term	Meaning
import	Imports a module into Python.
random	Module used for random selection.
time	Module used to measure execution time.
def	Defines a function.
len()	Returns the number of elements.
return	Returns a result from a function.
arr[0]	Accesses the first element.
arr[1:]	Selects elements from index 1 onwards.
random.choice()	Selects a random element.
remove()	Removes an element from a list.
arr.copy()	Creates a copy of a list.
print()	Displays output.
Recursion	A function calling itself.
List comprehension	A short way to create a new list.

8. Conclusion
Quick Sort is a Divide and Conquer sorting algorithm.
- Deterministic Quick Sort selects the first element as its pivot.
- Randomized Quick Sort selects a random element as its pivot.
- Both algorithms divide the array into left and right subarrays.
- Both use recursion to sort the subarrays.
- Both have average time complexity O(n log n) and worst-case time complexity O(n²).
- Randomized Quick Sort reduces the probability of consistently getting unbalanced partitions.
9. Viva Questions and Answers
Q1. What is Quick Sort?

Quick Sort is a sorting algorithm that follows the Divide and Conquer technique to sort elements.

Q2. What is a pivot?

A pivot is an element selected to divide an array into two parts.

Q3. What is Deterministic Quick Sort?

It is a Quick Sort variant in which the pivot is selected using a fixed rule, such as selecting the first element.

Q4. What is Randomized Quick Sort?

It is a Quick Sort variant in which the pivot is selected randomly.

Q5. What is recursion?

Recursion is a technique in which a function calls itself to solve smaller parts of a problem.

Q6. What is the base condition?

The base condition is if len(arr) <= 1. It stops recursive calls when the array has zero or one element.

Q7. What is the worst-case time complexity?

O(n²).

Q8. Which variant is generally preferred and why?

Randomized Quick Sort is generally preferred when input arrangements are unpredictable because random pivot selection reduces the likelihood of worst-case partitioning.

Q9. Which technique does Quick Sort use?

Divide and Conquer.

Q10. Why do we calculate execution time?

To analyze and compare the performance of both algorithms.'''