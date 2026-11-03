
# Recursive Fibonacci
def fibonacci_recursive(n):
    if n <= 1:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Non-Recursive (Iterative) Fibonacci
def fibonacci_non_recursive(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


# Main Program
n = int(input("Enter the number of terms: "))

print("\nFibonacci Series using Recursion:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")

print("\n\nFibonacci Series using Non-Recursion:")
fibonacci_non_recursive(n)

'''
sample input

Enter the number of terms: 7

sample output
Fibonacci Series using Recursion:
0 1 1 2 3 5 8

Fibonacci Series using Non-Recursion:
0 1 1 2 3 5 8

Method	Time Complexity	Space Complexity
Recursive	O(2ⁿ)	O(n)
Non-Recursive	O(n)	O(1)

Explanation:
1. Recursive approach:
   - A function calls itself to calculate the previous two Fibonacci numbers.
   - It creates multiple repeated function calls.
   - Therefore, time complexity is O(2ⁿ).
   - Recursive calls require a stack, so space complexity is O(n).
2. Non-recursive approach:
   - Uses a for loop instead of calling the function repeatedly.
   - Stores only two previous Fibonacci numbers (a and b).
   - Therefore, time complexity is O(n) and space complexity is O(1).
What is Fibonacci Series?
The Fibonacci series is a sequence in which each number is the sum of the previous two numbers.

Formula:
F(n)=F(n-1)+F(n-2)


Initial values:
F(0)=0,\quad F(1)=1

Example:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Conclusion: The non-recursive method is more efficient than the basic recursive method because it avoids repeated calculations and uses constant extra space.


1. What is the Fibonacci Series?
The Fibonacci series is a sequence of numbers in which each number is obtained by adding the previous two numbers.

The series starts with:
- First number = 0
- Second number = 1
After that, every number is calculated by adding the previous two numbers.

Formula:
\[
F(n)=F(n-1)+F(n-2)
\]

For example:
Position	Calculation	Fibonacci number
0	Initial value	0
1	Initial value	1
2	0 + 1	1
3	1 + 1	2
4	1 + 2	3
5	2 + 3	5
6	3 + 5	8
7	5 + 8	13

Therefore, the Fibonacci series is:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
Why do we use Fibonacci?
Fibonacci is useful for understanding:
- Recursion and function calls.
- Dynamic programming and optimization.
- Algorithm time and space complexity.
- Mathematical patterns in nature.
It is also used in certain searching algorithms, such as Fibonacci Search.

2. What are Recursive and Non-Recursive Approaches?
We can calculate Fibonacci numbers in two ways.
A. Recursive approach
Recursion means a function calls itself to solve a smaller version of the same problem.

For example, to calculate Fibonacci number at position 5:
\[
F(5)=F(4)+F(3)
\]

And:
\[
F(4)=F(3)+F(2)
\]

The function keeps calling itself until it reaches a stopping condition.
B. Non-recursive approach (Iterative)
Non-recursive means solving a problem without calling the same function repeatedly.

Here, we use a for loop and two variables to calculate the next Fibonacci number.

For example:
- Start with a = 0, b = 1.
- Add them to get the next number.
- Update the values.
- Repeat until the required number of terms is generated.

3. Complete Python Code
We have two functions:
1. fibonacci_recursive() – calculates Fibonacci using recursion.
2. fibonacci_non_recursive() – calculates Fibonacci using a loop.
The main program calls both functions and displays their results.
# Recursive Fibonaccidef fibonacci_recursive(n):    if n <= 1:        return n    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)# Non-Recursive (Iterative) Fibonaccidef fibonacci_non_recursive(n):    a = 0    b = 1    for i in range(n):        print(a, end=" ")        a, b = b, a + b# Main Programn = int(input("Enter the number of terms: "))print("\nFibonacci Series using Recursion:")for i in range(n):    print(fibonacci_recursive(i), end=" ")print("\n\nFibonacci Series using Non-Recursion:")fibonacci_non_recursive(n)




4. Block-by-Block Code Explanation
Block 1: Recursive Fibonacci Function
# Recursive Fibonaccidef fibonacci_recursive(n):    if n <= 1:        return n    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)



Let's understand each line.
Line 1: # Recursive Fibonacci
- # is used to write a comment in Python.
- Comments explain what a particular section of code does.
- Python ignores comments during execution.
We write this comment to identify that the following function uses recursion.
Line 2: def fibonacci_recursive(n):
- def is a Python keyword used to define a function.
- fibonacci_recursive is the name of our function.
- n is a parameter that represents the position of the Fibonacci number we want to calculate.
- The colon : indicates the beginning of the function body.
Example:
fibonacci_recursive(5)



Here, 5 is passed as the argument, and the function calculates the Fibonacci number at position 5.

The answer will be 5.
Line 3: if n <= 1:
This is called the base condition (base case) of recursion.
- if checks a condition.
- n <= 1 checks whether n is less than or equal to 1.
Why do we use this?

Every recursive function needs a stopping condition. Otherwise, the function will continue calling itself indefinitely.

In Fibonacci:
- If n = 0, return 0.
- If n = 1, return 1.
These are the first two Fibonacci numbers, so we already know their values.

Example:
fibonacci_recursive(0)  # Returns 0fibonacci_recursive(1)  # Returns 1



The function stops making further recursive calls when this condition becomes true.
Line 4: return n
- return sends the result back to the function that called it.
- Here, we directly return n because the first two Fibonacci numbers are 0 and 1.
For example:

If n = 0, it returns 0.

If n = 1, it returns 1.

Important: return also ends the current function execution.
Line 5: return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
This is the main logic of the Fibonacci program.

We use the Fibonacci formula:
\[
F(n)=F(n-1)+F(n-2)
\]

Let's understand the statement:
- fibonacci_recursive(n - 1) calls the same function with the previous position.
- fibonacci_recursive(n - 2) calls the same function with the position before that.
- + adds the results of both function calls.
- return sends their sum back.
Example:

Suppose:
fibonacci_recursive(4)



According to the formula:
\[
F(4)=F(3)+F(2)
\]

Now:
\[
F(3)=F(2)+F(1)=1+1=2
\]

\[
F(2)=F(1)+F(0)=1+0=1
\]

Therefore:
\[
F(4)=2+1=3
\]

Result = 3
How does recursion actually work?
Let's take fibonacci_recursive(4).
Function call breakdown
F(4)

F(3) + F(2)

F(3)

F(2) + F(1)

2

F(2)

F(1) + F(0)

1

F(1) = 1

F(2)

F(1) + F(0)

1

F(1) = 1

F(0) = 0



F(4) = 3
Notice that F(2) is calculated more than once. This repeated calculation makes basic recursion inefficient.

What you should remember: Recursion uses repeated function calls, and the base condition stops those calls.

Block 2: Non-Recursive (Iterative) Fibonacci Function
# Non-Recursive (Iterative) Fibonaccidef fibonacci_non_recursive(n):    a = 0    b = 1    for i in range(n):        print(a, end=" ")        a, b = b, a + b



This function calculates Fibonacci without recursion. Instead, it uses a loop.
Line 1: # Non-Recursive (Iterative) Fibonacci
This is a comment explaining that the following function uses an iterative approach.

Iterative means repeating instructions using loops.
Line 2: def fibonacci_non_recursive(n):
- def defines a function.
- fibonacci_non_recursive is the function name.
- n represents the number of Fibonacci terms to print.
For example:
fibonacci_non_recursive(5)



This prints the first five Fibonacci numbers.
Line 3: a = 0
We initialize the first variable a with 0.

Why?

Because the first Fibonacci number is 0.
Line 4: b = 1
We initialize the second variable b with 1.

Why?

Because the second Fibonacci number is 1.

At the beginning:
Variable	Value
a	0
b	1

These two variables store the previous two Fibonacci numbers.
Line 5: for i in range(n):
This is a for loop.
- for is used to repeat a block of code.
- i is the loop variable.
- range(n) generates numbers from 0 to n-1.
- The loop executes n times.
Example:

If n = 5:
range(5)



Produces:

0, 1, 2, 3, 4

Therefore, the loop executes 5 times.

Why do we use a loop?

Because we need to calculate and print the required number of Fibonacci terms without calling the function recursively.
Line 6: print(a, end=" ")
This statement prints the current value of a.
- print() displays the value.
- a is the current Fibonacci number.
- end=" " ensures that the next number is printed on the same line with a space instead of moving to a new line.
For example:
print(0, end=" ")print(1, end=" ")print(1, end=" ")



Output:
0 1 1


Why print a?

Because a stores the current Fibonacci number that we want to display.
Line 7: a, b = b, a + b
Most important line in iterative approach
This statement updates both variables to calculate the next Fibonacci number.

It uses Python's multiple assignment (tuple unpacking).

The logic is:
- New a gets the old value of b.
- New b gets the sum of old a and old b.
In other words:
a = bb = a + b



But writing it this way would be incorrect because the old value of a would be lost before calculating b.

Python's simultaneous assignment solves this problem by evaluating the right-hand side first.

Example:

Initially:
a = 0
b = 1


After executing:
a, b = b, a + b



We get:
a = 1
b = 1


Next iteration:
a = 1
b = 2


Next iteration:
a = 2
b = 3


This is how the Fibonacci sequence is generated.
Complete dry run of the iterative function
Suppose n = 6.
Iteration	Printed a	Old a	Old b	New a	New b
1	0	0	1	1	1
2	1	1	1	1	2
3	1	1	2	2	3
4	2	2	3	3	5
5	3	3	5	5	8
6	5	5	8	8	13

Final output:

0 1 1 2 3 5

Notice that we only need two variables to calculate the entire series!

Block 3: Main Program
# Main Programn = int(input("Enter the number of terms: "))



Line 1: # Main Program
This comment indicates that the main execution of our program starts here.
Line 2: n = int(input("Enter the number of terms: "))
Let's break this statement into smaller parts.

1. input()
- Used to accept input from the user.
- Whatever the user enters is initially treated as a string.
2. "Enter the number of terms: "

This is the message displayed to the user.

3. int()

Converts the input into an integer because we need a number to control our loop.

4. n =

Stores the entered number inside the variable n.

Example:

If the user enters:
7


Then:
n = 7



The program will calculate and display seven Fibonacci numbers.

Block 4: Calling the Recursive Function
print("\nFibonacci Series using Recursion:")for i in range(n):    print(fibonacci_recursive(i), end=" ")



Line 1: print("\nFibonacci Series using Recursion:")
- Prints the heading.
- \n represents a newline character.
- It moves the cursor to the next line before printing the heading.
Line 2: for i in range(n):
This loop runs from 0 to n-1.

Why do we use it?

Because we want to display the entire Fibonacci series, not just one Fibonacci number.

For example, if n = 5, the loop calls:
fibonacci_recursive(0)fibonacci_recursive(1)fibonacci_recursive(2)fibonacci_recursive(3)fibonacci_recursive(4)



Line 3: print(fibonacci_recursive(i), end=" ")
This line performs two operations:
1. Calls the recursive function with the current value of i.
2. Prints the returned Fibonacci number.
For example:

When i = 0, it prints 0.

When i = 1, it prints 1.

When i = 2, it prints 1.

When i = 3, it prints 2.

When i = 4, it prints 3.

Therefore, for n = 5, the output is:
0 1 1 2 3


Important: The loop is outside the recursive function because we want to calculate each Fibonacci position and print the complete series.

Block 5: Calling the Non-Recursive Function
print("\n\nFibonacci Series using Non-Recursion:")fibonacci_non_recursive(n)



Line 1: print("\n\nFibonacci Series using Non-Recursion:")
- Prints the heading for the non-recursive Fibonacci series.
- \n\n creates two newline characters, leaving a blank line before the heading.
Line 2: fibonacci_non_recursive(n)
This calls the non-recursive function.

The value of n is passed to the function.

For example:
fibonacci_non_recursive(7)



The function initializes a = 0 and b = 1, executes the loop seven times, and prints:
0 1 1 2 3 5 8


Unlike the recursive function, this function directly prints the series instead of returning each number.

5. Sample Input and Output
Sample Input:
Enter the number of terms: 7


Sample Output:
Fibonacci Series using Recursion:
0 1 1 2 3 5 8

Fibonacci Series using Non-Recursion:
0 1 1 2 3 5 8


How did we get this output?
The user entered 7, which means we need to print the first seven Fibonacci numbers.

Starting with:
- First number = 0
- Second number = 1
Calculations:
Term	Calculation	Result
1	Initial	0
2	Initial	1
3	0 + 1	1
4	1 + 1	2
5	1 + 2	3
6	2 + 3	5
7	3 + 5	8

Both methods generate the same output, but their internal working is different.

6. Time and Space Complexity Analysis
Complexity tells us how much time and memory an algorithm requires as the input size increases.
A. Recursive Fibonacci
Less efficient
Time Complexity: O(2ⁿ)

Why?
- Every function call generates two more function calls (except the base cases).
- The same Fibonacci values are calculated repeatedly.
- This increases the total number of function calls exponentially.
For example, while calculating F(5), F(3) and F(2) get calculated multiple times.

The recurrence relation is:
\[
T(n)=T(n-1)+T(n-2)+O(1)
\]

Its tighter asymptotic bound is \(\Theta(\phi^n)\), where \(\phi\) is the golden ratio. It is commonly expressed using the simpler upper bound O(2ⁿ).

Space Complexity: O(n)

Why?
- Every recursive function call is stored in the call stack.
- The maximum depth of recursive calls is proportional to n.
- Therefore, the space complexity is O(n).
B. Non-Recursive Fibonacci
More efficient
Time Complexity: O(n)

Why?
- The for loop executes n times.
- Every iteration performs a constant number of operations.
- Therefore, time complexity is O(n).
Space Complexity: O(1)

Why?
- We only use two variables: a and b.
- We do not create additional arrays or recursive function calls.
- Memory usage remains constant regardless of n.
C. Complexity Comparison
Parameter	Recursive	Non-Recursive
Technique	Function calls	For loop
Time	O(2ⁿ)	O(n)
Space	O(n)	O(1)
Repeated calculations	Yes	No
Efficiency	Less efficient	More efficient

Important for practical exam: The non-recursive method is more efficient because it avoids repeated calculations and requires constant extra space.

7. Real-Life Example of Fibonacci Series
Example: Rabbit Population

Imagine a pair of rabbits is introduced into an environment.

For a simplified mathematical model, assume:
- Each mature pair produces one new pair every month.
- Rabbits do not die.
- A new pair takes one month to mature.
The number of rabbit pairs follows the Fibonacci pattern.
Month	Number of rabbit pairs
1	1
2	1
3	2
4	3
5	5
6	8
7	13








knowanimals.com


The population follows the Fibonacci sequence because the number of pairs in the current month depends on the pairs from the previous two months.

This is a simplified mathematical example, not a prediction of actual rabbit populations.
Other applications of Fibonacci
1. Nature: Patterns in sunflower seed arrangements and pinecones.
2. Computer Science: Fibonacci Search algorithm.
3. Mathematics: Number sequences and mathematical patterns.
4. Algorithm Analysis: Understanding recursion and dynamic programming.

8. Important Viva Questions
Q1. What is Fibonacci series?

A sequence in which each number is the sum of the previous two numbers, starting with 0 and 1.

Q2. What is recursion?

Recursion is a technique in which a function calls itself until a base condition is reached.

Q3. What is the base condition in this program?
if n <= 1:    return n



It stops recursive calls when n becomes 0 or 1.

Q4. What is an iterative approach?

An approach that uses loops to repeat instructions instead of calling a function recursively.

Q5. Why is non-recursive Fibonacci better?

It avoids repeated calculations and requires less memory.

Q6. Why do we use two variables, a and b?

To store the previous two Fibonacci numbers and calculate the next number.

Q7. What happens if we remove the base condition?

The recursive function will not have a proper stopping condition and will eventually cause a recursion error.

Q8. Which method uses a stack?

The recursive method uses the function call stack to store pending function calls.

Q9. What is the output for n = 5?
0 1 1 2 3


Q10. What is the difference between print() and return?
- print() displays a value on the screen.
- return sends a value back to the function caller.

9. Final Practical Revision
Remember these points before your practical examination:
- Fibonacci formula: \(F(n)=F(n-1)+F(n-2)\)
- Starting values: 0 and 1.
- Recursive approach: Function calls itself.
- Base condition: if n <= 1.
- Non-recursive approach: Uses a for loop.
- a, b = b, a + b updates the two Fibonacci numbers.
- Recursive time complexity: O(2ⁿ) (commonly stated upper bound).
- Recursive space complexity: O(n).
- Non-recursive time complexity: O(n).
- Non-recursive space complexity: O(1).
Most important thing to understand: Both approaches produce the same Fibonacci series. The difference is that recursion solves the problem using repeated function calls, whereas iteration solves it using a loop and two variables.'''