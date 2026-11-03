
# 0-1 Knapsack using Dynamic Programming

def knapsack(W, wt, val, n):

    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):

            if wt[i - 1] <= w:
                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Main program
n = int(input("Enter number of items: "))

val = []
wt = []

for i in range(n):
    val.append(int(input("Enter value of item: ")))
    wt.append(int(input("Enter weight of item: ")))

W = int(input("Enter knapsack capacity: "))

print("Maximum value:", knapsack(W, wt, val, n))



''' sample input:
Enter number of items: 3
Enter value of item: 60
Enter weight of item: 10
Enter value of item: 100
Enter weight of item: 20
Enter value of item: 120
Enter weight of item: 30
Enter knapsack capacity: 50

sample output:
Maximum value: 220

Complexity Summary
Complexity	Result	Reason
Time	O(n × W)	Two nested loops
Space	O(n × W)	2D DP table
Time and Space Complexity – 0-1 Knapsack Using Dynamic Programming
1. Time Complexity: O(n × W)
- The program uses two nested for loops.
- Outer loop executes n times (number of items).
- Inner loop executes W times (knapsack capacity).
- Each iteration performs constant-time operations.
Therefore:
O(n \times W)

2. Space Complexity: O(n × W)
- The program creates a 2D DP table.
- It contains (n+1) × (W+1) cells.
- Therefore, the memory required depends on the number of items and knapsack capacity.
O(n \times W)

Complexity Summary
Complexity	Result	Reason
Time	O(n × W)	Two nested loops
Space	O(n × W)	2D DP table

Where:
- n = Number of items.
- W = Knapsack capacity.
Note: The time complexity is pseudo-polynomial because it depends on the numerical value of the capacity W, not just the input size.

0-1 Knapsack Problem Using Dynamic Programming – Complete Explanation
Let's understand this practical from the very beginning, assuming you are learning the 0-1 Knapsack Problem and Dynamic Programming for the first time.

We will understand:
1. What is the 0-1 Knapsack Problem?
2. Why do we use it?
3. What is Dynamic Programming?
4. Complete code explanation, block by block and line by line.
5. Dry run with an example.
6. Sample input and output.
7. Time and space complexity.
8. Another real-life example of the concept.

1. What is the 0-1 Knapsack Problem?
Imagine you are going on a trip and you have a bag (knapsack) that can carry a maximum weight of 50 kg.

You have different items. Each item has:
- A weight.
- A value (or profit).
Your task is to select items in such a way that:
- The total weight should not exceed the bag's capacity.
- The total value should be maximum.
- You can either select an entire item or leave it.
- You cannot select a fraction of an item.
This problem is called the 0-1 Knapsack Problem.
Why is it called 0-1 Knapsack?
- 0 means the item is not selected.
- 1 means the item is selected.
For example, if you have a laptop, you can either put the entire laptop in your bag or leave it. You cannot put only half of the laptop.







medium.com


Example
Suppose we have the following items:
Item	Weight	Value
Item 1	10	60
Item 2	20	100
Item 3	30	120

Knapsack capacity = 50 kg.

We need to find which items give us the maximum value without exceeding 50 kg.

Possible combinations:
Selected items	Total weight	Total value
Item 1	10	60
Item 2	20	100
Item 3	30	120
Item 1 + 2	30	160
Item 1 + 3	40	180
Item 2 + 3	50	220

The best choice is Item 2 + Item 3.
- Total weight = 20 + 30 = 50
- Total value = 100 + 120 = 220
Therefore, the maximum value is 220.

2. What is Dynamic Programming?
Dynamic Programming (DP) is an algorithmic technique used to solve complex problems by breaking them into smaller subproblems.

Instead of solving the same subproblem again and again, we store its result and reuse it whenever required.

In simple words: Solve smaller problems first, store their answers, and use those answers to solve bigger problems.
Why do we use Dynamic Programming in Knapsack?
Suppose we have multiple items. We need to check different combinations to find the maximum value.

Checking every possible combination repeatedly takes more time.

Dynamic Programming makes this process efficient by storing previously calculated results in a table.

In our program, we use a 2D table called dp.
- Rows represent the number of items considered.
- Columns represent the available knapsack capacity.
- Each cell stores the maximum value possible for that particular situation.

3. Complete Python Code
First, let's look at the complete program. Read it once, and then we will break it into smaller blocks.
# 0-1 Knapsack using Dynamic Programmingdef knapsack(W, wt, val, n):    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]    for i in range(1, n + 1):        for w in range(1, W + 1):            if wt[i - 1] <= w:                dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]],                               dp[i - 1][w])            else:                dp[i][w] = dp[i - 1][w]    return dp[n][W]# Main programn = int(input("Enter number of items: "))val = []wt = []for i in range(n):    val.append(int(input("Enter value of item: ")))    wt.append(int(input("Enter weight of item: ")))W = int(input("Enter knapsack capacity: "))print("Maximum value:", knapsack(W, wt, val, n))



4. Code Explanation – Block by Block
Block 1: Defining the function
def knapsack(W, wt, val, n):



Let's understand every word.
- def – A Python keyword used to define a function.
- knapsack – Name of our function.
- W – Maximum capacity of the knapsack.
- wt – List containing the weights of all items.
- val – List containing the values of all items.
- n – Total number of items.
Why do we use a function?

A function allows us to write the main logic separately and call it whenever required.

For example, suppose:
W = 50wt = [10, 20, 30]val = [60, 100, 120]n = 3



When we call:
knapsack(W, wt, val, n)



The values are passed to the function.
Parameter	Received value
W	50
wt	[10, 20, 30]
val	[60, 100, 120]
n	3

Now the function has all the information needed to solve the problem.
Block 2: Creating the DP table
dp = [[0 for x in range(W + 1)] for x in range(n + 1)]



Important line
This is the most important line because we create a 2D DP table to store the calculated results.

First, understand what a 2D list is.

A normal list looks like:
a = [1, 2, 3]



A 2D list looks like a table:
a = [    [0, 0, 0],    [0, 0, 0],    [0, 0, 0]]



It contains rows and columns.

Now let's understand our actual statement:
dp = [[0 for x in range(W + 1)] for x in range(n + 1)]



There are two parts:

Part 1:
[0 for x in range(W + 1)]



This creates one row containing zeros.

If W = 50, then range(W + 1) creates 51 positions because Python starts counting from 0.

Therefore, one row contains 51 zeros.

Part 2:
for x in range(n + 1)



This creates multiple rows.

If n = 3, then range(n + 1) creates 4 rows.

Why are we using n + 1 and W + 1?

Because we need:
- One extra row for the situation where no items are considered.
- One extra column for the situation where the capacity is zero.
So, for our example:
- Number of items = 3
- Capacity = 50
Our DP table will have:
- 4 rows (0 to 3).
- 51 columns (0 to 50).
What does this table store?

Each cell dp[i][w] represents:

The maximum value we can obtain using the first i items with a knapsack capacity of w.

Initially, every cell is 0 because we have not calculated any values yet.

For example:
       Capacity
       0  1  2  3  ... 50
Item 0 0  0  0  0  ...  0
Item 1 0  0  0  0  ...  0
Item 2 0  0  0  0  ...  0
Item 3 0  0  0  0  ...  0


Block 3: Outer loop – Selecting items one by one
for i in range(1, n + 1):



This loop runs through all the items one by one.
- i represents the current item number being considered.
- range(1, n + 1) starts from 1 because row 0 represents no items.
For example, if n = 3:
i = 1
i = 2
i = 3


This means:
- First iteration: Consider Item 1.
- Second iteration: Consider Item 2.
- Third iteration: Consider Item 3.
Why do we need this loop?

We need to calculate the maximum possible value after considering each item.

We start with the first item and gradually include more items.
Block 4: Inner loop – Checking capacity
for w in range(1, W + 1):



This loop checks different knapsack capacities.
- w represents the current capacity being considered.
- It starts from 1 and goes up to W.
For example, if W = 5, the values of w will be:
w = 1
w = 2
w = 3
w = 4
w = 5


Why do we need another loop?

The outer loop selects the items one by one.

The inner loop checks what maximum value can be obtained at each possible capacity.

For example:
- What is the maximum value with capacity 10?
- What is the maximum value with capacity 20?
- What is the maximum value with capacity 30?
And so on.

Important: Both loops work together to fill the DP table.
Block 5: Checking whether an item can fit
if wt[i - 1] <= w:



This condition checks whether the current item can fit inside the available capacity.

Let's understand the expression:
- wt is the list of item weights.
- i - 1 is used because Python list indexing starts from 0.
- w is the current capacity.
For example:
wt = [10, 20, 30]



If i = 1:
wt[i - 1]wt[1 - 1]wt[0]



The result is 10.

So the condition becomes:
if 10 <= w:



If the available capacity is 20, the condition is true because the item weighs only 10.

Why do we use i - 1?

Our DP table starts counting items from row 1, but Python lists start indexing from 0.
DP row (i)	Python index (i-1)	Item weight
1	0	10
2	1	20
3	2	30

If the item fits, we have two choices:
1. Include the item.
2. Exclude the item.
We need to calculate both choices and select the better one.
Block 6: Finding the maximum value
dp[i][w] = max(val[i - 1] + dp[i - 1][w - wt[i - 1]],               dp[i - 1][w])



Most important logic of the program
This statement implements the main concept of the 0-1 Knapsack Problem.

We use the Python max() function to choose the maximum value between two possibilities.

Let's divide it into two parts.

Part 1: Including the current item
val[i - 1] + dp[i - 1][w - wt[i - 1]]



This calculates the total value if we select the current item.

It contains two things:
1. val[i - 1] – Value of the current item.
2. dp[i - 1][w - wt[i - 1]] – Maximum value obtained using previous items with the remaining capacity.
Let's take an example.

Suppose:
val = [60, 100, 120]wt = [10, 20, 30]



Currently:
- We are considering Item 2.
- Its weight is 20.
- Its value is 100.
- Available capacity is 50.
If we include Item 2:

Remaining capacity:
50 - 20 = 30


Now we add:
Value of current item + Maximum value for remaining capacity


Therefore:
100 + dp[1][30]


If dp[1][30] = 60, the result becomes:
100 + 60 = 160


This means we get a total value of 160 by including Item 2 along with the best selection from previous items.

Why do we use i - 1 in the DP table?

Because when including the current item, we can only use previously considered items to fill the remaining capacity.

This prevents selecting the same item multiple times.

Part 2: Excluding the current item
dp[i - 1][w]



This means we do not select the current item.

We simply take the maximum value already calculated using previous items at the same capacity.

For example:
dp[1][50] = 60


This means if we exclude Item 2, the best value using previous items is 60.

Finally, we compare both choices:
max(160, 60)



Result:
160


So we select the option that gives us the maximum value.

In simple words:
- First expression = Include the item.
- Second expression = Exclude the item.
- max() = Select whichever gives more value.
This is the main logic behind Dynamic Programming in this program.
Block 7: When the item cannot fit
else:    dp[i][w] = dp[i - 1][w]



This block executes when the condition is false.

That means:
wt[i - 1] > w



In simple words, the current item's weight is greater than the available capacity.

Therefore, we cannot select that item.

We have only one option: exclude it.

So we copy the previous result:
dp[i][w] = dp[i - 1][w]



Example:

Suppose:
- Current item weight = 30 kg.
- Available capacity = 20 kg.
Since 30 is greater than 20, the item cannot fit.

Therefore, we use the maximum value obtained from previous items without including the current item.
Block 8: Returning the final answer
return dp[n][W]



After both loops finish, our DP table is completely filled.

We need the answer from the last row and last column.
- n represents all the available items.
- W represents the complete knapsack capacity.
Therefore:
dp[n][W]



gives the maximum value obtainable using all items within the given capacity.

For our example:
dp[3][50] = 220



So the function returns:
220



5. Main Program Explanation
Now that we have understood the function, let's understand how the user enters the data and how the function gets called.
Block 1: Taking the number of items
n = int(input("Enter number of items: "))



- input() accepts information from the user.
- int() converts the entered value into an integer.
- n stores the total number of items.
Example:
Enter number of items: 3


Now:
n = 3



Block 2: Creating empty lists
val = []wt = []



We create two empty lists.
- val stores the values of items.
- wt stores the weights of items.
Why separate lists?

Because we need to store the weight and value of each item separately.

After entering our example:
val = [60, 100, 120]wt = [10, 20, 30]



The corresponding positions represent the same item.

For example:
val[0] = 60
wt[0] = 10


This means Item 1 has value 60 and weight 10.
Block 3: Taking item details using a loop
for i in range(n):    val.append(int(input("Enter value of item: ")))    wt.append(int(input("Enter weight of item: ")))



Let's understand each line.

Line 1:
for i in range(n):



This loop executes once for every item.

If n = 3, it executes three times.

Line 2:
val.append(int(input("Enter value of item: ")))



- input() takes the item's value.
- int() converts it into an integer.
- append() adds that value to the val list.
For example:
val.append(60)



Now:
val = [60]



Line 3:
wt.append(int(input("Enter weight of item: ")))



This works similarly, but stores the weight in the wt list.

For example:
wt.append(10)



Now:
wt = [10]



This process repeats for all items.
Block 4: Taking knapsack capacity
W = int(input("Enter knapsack capacity: "))



This statement asks the user to enter the maximum capacity of the bag.

Example:
Enter knapsack capacity: 50


Now:
W = 50



Block 5: Calling the function and displaying the answer
print("Maximum value:", knapsack(W, wt, val, n))



This statement calls our previously defined function.

It passes four arguments:
- W – Knapsack capacity.
- wt – Weight list.
- val – Value list.
- n – Number of items.
The function performs all calculations and returns the maximum value.

Finally, print() displays the result.

For example:
Maximum value: 220



6. Dry Run of the Program
Let's understand how the program actually works internally.

Consider the following input:
Item	Weight	Value
1	10	60
2	20	100
3	30	120

Knapsack capacity = 50.

Our DP table will have 4 rows and 51 columns.

Instead of displaying all 51 columns, let's understand the important capacity values: 0, 10, 20, 30, 40 and 50.

The following table shows the values after processing each item.
Items considered	0	10	20	30	40	50
0 items	0	0	0	0	0	0
Item 1	0	60	60	60	60	60
Items 1, 2	0	60	100	160	160	160
Items 1, 2, 3	0	60	100	160	180	220

Let's understand how these values are obtained.

Step 1: Considering Item 1
- Weight = 10
- Value = 60
If capacity is less than 10, the item cannot fit.

If capacity is 10 or more, we can select it and get value 60.

Therefore, at capacity 10, 20, 30, 40 and 50, the maximum value is 60.

Step 2: Considering Item 2
- Weight = 20
- Value = 100
At capacity 20, we can select Item 2 and get 100.

At capacity 30, we can select Item 1 and Item 2:
Weight = 10 + 20 = 30
Value = 60 + 100 = 160


At capacity 50, selecting both still gives 160.

Step 3: Considering Item 3
- Weight = 30
- Value = 120
At capacity 30, selecting Item 3 gives 120, but the previous best value was 160. So we keep 160.

At capacity 40, we can select Item 1 and Item 3:
Weight = 10 + 30 = 40
Value = 60 + 120 = 180


At capacity 50, we can select Item 2 and Item 3:
Weight = 20 + 30 = 50
Value = 100 + 120 = 220


This gives the maximum value.
Final Answer: 220
7. Sample Input and Output
Sample Input
Enter number of items: 3
Enter value of item: 60
Enter weight of item: 10
Enter value of item: 100
Enter weight of item: 20
Enter value of item: 120
Enter weight of item: 30
Enter knapsack capacity: 50


Sample Output
Maximum value: 220


Understanding the output
We have three items:
- Item 1: Weight = 10, Value = 60
- Item 2: Weight = 20, Value = 100
- Item 3: Weight = 30, Value = 120
The program selects Item 2 and Item 3.

Total weight:
20 + 30 = 50


Total value:
100 + 120 = 220


Since the total weight is exactly equal to the capacity, the selection is valid.

Therefore, the maximum value is 220.

8. Time and Space Complexity
Complexity tells us how much time and memory an algorithm requires as the input size increases.
Time Complexity: O(n × W)
In our program, we have two nested loops:
for i in range(1, n + 1):    for w in range(1, W + 1):



- Outer loop executes n times.
- Inner loop executes W times.
Therefore:
\[
T(n) = O(n \times W)
\]

Example:

If:
- Number of items = 3
- Capacity = 50
The main DP calculation performs:
\[
3 \times 50 = 150
\]

iterations.
Space Complexity: O(n × W)
We create a 2D DP table:
dp = [[0 for x in range(W + 1)] for x in range(n + 1)]



The table contains:
\[
(n+1)\times(W+1)
\]

cells.

Therefore:
\[
S(n) = O(n \times W)
\]

Why?

Because we store the calculated results for every item and every possible capacity.
Complexity Summary
Type	Complexity	Reason
Time	O(n × W)	Two nested loops
Space	O(n × W)	2D DP table

Note: This is called pseudo-polynomial time because the complexity depends on the numerical capacity W, not just the number of input items.

9. Example of the Concept Used in Real Life
Let's take a different example to understand where the 0-1 Knapsack Problem can be used.

Situation: A delivery person has a bag with a maximum capacity of 10 kg.

There are four packages available.
Package	Weight	Value
A	2 kg	₹30
B	3 kg	₹40
C	4 kg	₹50
D	5 kg	₹60

The delivery person wants to carry packages that provide the maximum total value without exceeding 10 kg.

Let's check some combinations.
Selected packages	Total weight	Total value
A + B	5 kg	₹70
A + C	6 kg	₹80
A + D	7 kg	₹90
B + C	7 kg	₹90
B + D	8 kg	₹100
C + D	9 kg	₹110
A + B + C	9 kg	₹120
A + B + D	10 kg	₹130

The best combination is A + B + D.
- Total weight = 2 + 3 + 5 = 10 kg.
- Total value = 30 + 40 + 60 = ₹130.
Maximum value = ₹130
This is exactly how the 0-1 Knapsack algorithm works. It checks whether to include or exclude each package and finds the combination that gives the maximum value within the available capacity.
Applications of the 0-1 Knapsack Problem
1. Cargo loading: Selecting packages to maximize the value of goods loaded into a vehicle.
2. Budget allocation: Selecting projects within a fixed budget to maximize returns.
3. Resource management: Selecting tasks within limited resources.
4. Investment selection: Choosing investments within a fixed budget.
5. Memory management: Selecting files to store within limited storage capacity.

10. Important Points to Remember for Your Practical Exam
Question	Answer
Which problem are we solving?	0-1 Knapsack Problem
Which technique is used?	Dynamic Programming
What does 0 mean?	Item is not selected
What does 1 mean?	Item is selected
Can we select half an item?	No
Why do we use a DP table?	To store previously calculated results
Why do we use max()?	To choose the better option between including and excluding an item
What does dp[i][w] represent?	Maximum value using first i items with capacity w
What does return dp[n][W] do?	Returns the final maximum value
Time Complexity	O(n × W)
Space Complexity	O(n × W)

The most important formula
Remember this formula because it represents the entire logic of the program.
dp[i][w] =
\max
\begin{cases}
val[i-1]+dp[i-1][w-wt[i-1]]\\
dp[i-1][w]
\end{cases}
When the item does not fit:

dp[i][w]=dp[i-1][w]

In simple words:
- If the item fits, check both possibilities: include it or exclude it.
- If the item does not fit, exclude it.
- Store the maximum result in the DP table.
- Finally, return the last cell of the table.
One final thing to understand: Dynamic Programming is not randomly selecting items. It systematically calculates and stores the best possible answer for smaller capacities and fewer items, then uses those answers to find the overall maximum value. That's the actual idea behind this practical.'''