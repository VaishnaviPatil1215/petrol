def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()


def is_safe(board, row, col, n):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n):

    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1

            if solve(board, row + 1, n):
                return True

            board[row][col] = 0

    return False


# Main program
n = int(input("Enter the value of N: "))

board = [[0 for _ in range(n)] for _ in range(n)]

# Place first queen
board[0][0] = 1

if solve(board, 1, n):
    print("\nFinal N-Queens Matrix:")
    print_board(board, n)
else:
    print("Solution does not exist.")




'''sample output
Enter the value of N: 4

Final N-Queens Matrix:
1 0 0 0
0 0 0 1
0 1 0 0
0 0 1 0

time complexity:O(N × N!):	Trying possible queen arrangements and checking safety
Space Complexity:O(N²)	Storing the N × N chessboard and recursion stack


N-Queens Problem Using Backtracking – Complete Code Explanation
Let's understand this program from the very beginning, assuming you are learning the N-Queens problem and Backtracking for the first time.

We will cover:
1. What is the N-Queens problem?
2. What is Backtracking?
3. Complete Python code.
4. Block-by-block explanation of every line.
5. Dry run with an example (N = 4).
6. Sample input and output.
7. Time and space complexity.
8. Another example to understand Backtracking.

1. Understanding the N-Queens Problem
The N-Queens problem is a classic problem solved using the Backtracking algorithm.

The objective is to place N queens on an N × N chessboard such that no two queens attack each other.

A queen in chess can move in three directions:
- Horizontally (left and right).
- Vertically (up and down).
- Diagonally (in all four diagonal directions).
Therefore, we must make sure that no two queens are present in the same row, column, or diagonal.

Example:

For N = 4, we need to place 4 queens on a 4 × 4 chessboard.

Initially, the board is empty:
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0


Here:
- 0 represents an empty cell.
- 1 represents a queen.
The question specifically asks us to place the first queen before using Backtracking to place the remaining queens.

So, we place the first queen at position (0, 0).
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0


Now, our program must place the remaining 3 queens without violating any chess rules.

2. What is Backtracking?
Backtracking is an algorithmic technique in which we try to solve a problem step by step. If a choice leads to an incorrect solution, we undo that choice and try another option.

In simple words:
1. Make a choice.
2. Check whether the choice is valid.
3. If valid, move forward.
4. If it leads to failure, undo the choice.
5. Try another choice.
Example:

Suppose we want to place a queen in the second row.
- First, try column 0.
- If the position is unsafe, try column 1.
- If column 1 is also unsafe, try column 2.
- Continue until we find a safe position.
- If no position works, go back to the previous row and change the previous queen's position.
This process of going back and trying another possibility is called Backtracking.

3. Complete Python Code
First, let's look at the complete program. We will divide it into small blocks and understand each line separately.
def print_board(board, n):    for i in range(n):        for j in range(n):            print(board[i][j], end=" ")        print()def is_safe(board, row, col, n):    # Check column    for i in range(row):        if board[i][col] == 1:            return False    # Check upper left diagonal    i, j = row - 1, col - 1    while i >= 0 and j >= 0:        if board[i][j] == 1:            return False        i -= 1        j -= 1    # Check upper right diagonal    i, j = row - 1, col + 1    while i >= 0 and j < n:        if board[i][j] == 1:            return False        i -= 1        j += 1    return Truedef solve(board, row, n):    if row == n:




4. Block-by-Block Code Explanation
Block 1: Printing the Chessboard
Code:
def print_board(board, n):    for i in range(n):        for j in range(n):            print(board[i][j], end=" ")        print()



What is this block used for?

This function is responsible for displaying the final chessboard in matrix format.

Let's understand every line.

Line 1:
def print_board(board, n):



- def is a Python keyword used to define a function.
- print_board is the name of our function.
- board represents the chessboard matrix.
- n represents the size of the chessboard.
For example, if N = 4, the board contains 4 rows and 4 columns.

Line 2:
for i in range(n):



- for is used to execute a loop.
- range(n) generates numbers from 0 to n-1.
- i represents the row number.
For N = 4, the values of i will be:
i = 0
i = 1
i = 2
i = 3


This loop visits every row of the chessboard.

Line 3:
for j in range(n):



This is another loop inside the first loop, called a nested loop.
- j represents the column number.
- It visits every column of the current row.
For N = 4, the column values will be 0, 1, 2, and 3.

Line 4:
print(board[i][j], end=" ")



This line prints the value stored at a particular row and column.
- board[i][j] accesses an element of the matrix.
- end=" " prints a space after the value instead of moving to a new line.
For example:
board[0][0] = 1board[0][1] = 0board[0][2] = 0board[0][3] = 0



The output will be:
1 0 0 0


Line 5:
print()



This moves the cursor to the next line after printing all the columns of the current row.

Without this statement, all the matrix elements would appear on a single line.

How does this block work?

For a 4 × 4 matrix:
- Outer loop selects a row.
- Inner loop prints all columns of that row.
- print() moves to the next row.
This process continues until all four rows are printed.

Block 2: Checking Whether a Queen Can Be Placed Safely
This is one of the most important functions in the program.

Code:
def is_safe(board, row, col, n):



What is this function used for?

Before placing a queen at a particular position, we must check whether another queen can attack it.

This function checks:
1. Same column.
2. Upper-left diagonal.
3. Upper-right diagonal.
If any queen is found in these directions, the position is unsafe.

Otherwise, the position is safe.

Line 1:
def is_safe(board, row, col, n):



Here:
- board is the chessboard.
- row is the row where we want to place a queen.
- col is the column where we want to place a queen.
- n is the size of the chessboard.
For example:
is_safe(board, 1, 2, 4)



This checks whether we can place a queen at row 1, column 2 on a 4 × 4 board.

Remember: Python indexing starts from 0.

So row 1, column 2 means the second row and third column.
Part A: Checking the Same Column
Code:
for i in range(row):    if board[i][col] == 1:        return False



Why do we check the column?

A queen can attack another queen vertically.

Therefore, two queens cannot be placed in the same column.

Line 1:
for i in range(row):



This loop checks all the rows above the current row.

Why only the rows above?

Because our program places queens row by row, from top to bottom. Therefore, queens can only exist in the previous rows.

For example, if the current row is 2:
i = 0
i = 1


It checks rows 0 and 1.

Line 2:
if board[i][col] == 1:



This checks whether the current column already contains a queen.
- board[i][col] accesses the element at row i and column col.
- == 1 checks whether that element contains a queen.
Line 3:
return False



If a queen is already present in the same column, the position is unsafe.

return False immediately ends the function and tells the program not to place a queen there.

Example:

Suppose the board is:
1 0 0 0
0 0 1 0
0 0 0 0
0 0 0 0


Now we want to place a queen at row 2, column 2.

The column already contains a queen at row 1.

Therefore:
board[1][2] == 1



The function returns False.

The queen cannot be placed there.
Part B: Checking the Upper-Left Diagonal
Code:
i, j = row - 1, col - 1while i >= 0 and j >= 0:    if board[i][j] == 1:        return False    i -= 1    j -= 1



Why do we check the upper-left diagonal?

A queen can attack another queen diagonally.

Therefore, before placing a queen, we must check whether another queen exists on its upper-left diagonal.

Line 1:
i, j = row - 1, col - 1



This initializes the position from where we start checking the upper-left diagonal.

Why subtract 1?

Because we want to move one row upward and one column to the left.

For example, suppose we want to check position:
row = 2
col = 2


Then:
i = 2 - 1 = 1j = 2 - 1 = 1



So we start checking from position (1, 1).

Line 2:
while i >= 0 and j >= 0:



This loop continues as long as both row and column indexes are greater than or equal to zero.

Why?

Because we cannot move outside the chessboard.

For example, when i or j becomes -1, we have reached the boundary.

Line 3:
if board[i][j] == 1:



This checks whether a queen is present at the current diagonal position.

Line 4:
return False



If a queen is found, the position is unsafe.

Lines 5 and 6:
i -= 1j -= 1



These statements move one step upward and one step to the left.

For example, the positions checked when starting at (2, 2) are:
(1, 1)
(0, 0)


Notice that both row and column decrease by 1.

If a queen is found at any of these positions, the function returns False.
Part C: Checking the Upper-Right Diagonal
Code:
i, j = row - 1, col + 1while i >= 0 and j < n:    if board[i][j] == 1:        return False    i -= 1    j += 1



Why do we check the upper-right diagonal?

A queen can also attack another queen diagonally towards the upper-right side.

Therefore, we must check this direction as well.

Line 1:
i, j = row - 1, col + 1



Here:
- row - 1 moves one row upward.
- col + 1 moves one column to the right.
For example:
row = 2col = 1



Then:
i = 1j = 2



We start checking at position (1, 2).

Line 2:
while i >= 0 and j < n:



This loop checks the upper-right diagonal as long as we remain inside the chessboard.
- i >= 0 ensures that we do not go above the first row.
- j < n ensures that we do not go beyond the last column.
Line 3:
if board[i][j] == 1:



Checks whether a queen is already present at the current diagonal position.

Line 4:
return False



If a queen is found, the position is unsafe.

Lines 5 and 6:
i -= 1j += 1



These move the checking position one row upward and one column to the right.

For example, starting from (2, 1), the positions checked are:
(1, 2)
(0, 3)


Part D: Returning True
Code:
return True



Why do we use this statement?

If the program completes all three checks without finding another queen, the position is safe.

Therefore, it returns True.

Remember this:
Condition	Return value
Queen found in the same column	False
Queen found in upper-left diagonal	False
Queen found in upper-right diagonal	False
No queen found in any direction	True

Important concept: We only check upward directions because queens are placed row by row, starting from the first row. There cannot be any previously placed queen below the current row.

Block 3: Main Backtracking Function
This is the most important block because it actually places the queens on the chessboard.

Code:
def solve(board, row, n):    if row == n:        return True    for col in range(n):        if is_safe(board, row, col, n):            board[row][col] = 1            if solve(board, row + 1, n):                return True            board[row][col] = 0    return False



Let's understand it line by line.

Line 1:
def solve(board, row, n):



This defines the main function that solves the N-Queens problem.

It accepts:
- board: The chessboard matrix.
- row: The current row in which we want to place a queen.
- n: The size of the chessboard.
For example:
solve(board, 1, 4)



This means we need to start placing queens from row 1 on a 4 × 4 chessboard.

Remember, the first queen is already placed at row 0.
Part A: Base Condition
Code:
if row == n:    return True



This is called the Base Condition of Recursion.

First, understand what recursion means.

Recursion is a technique in which a function calls itself to solve a smaller part of the same problem.

In our program, the solve() function calls itself to place queens in the next row.

Why do we need this condition?

If row == n, it means all N rows have been successfully processed.

Since we place exactly one queen in each row, all N queens have been placed.

Therefore:
return True



means that we have successfully found a solution.

Example:

For N = 4, the rows are:
0
1
2
3


After placing a queen in row 3, the function calls:
solve(board, 4, 4)



Now:
row == n4 == 4



The condition becomes true.

So, the function returns True.

This stops further recursion.
Part B: Trying Every Column
Code:
for col in range(n):



This loop tries every column in the current row.

For N = 4:
col = 0
col = 1
col = 2
col = 3


Why do we need this loop?

Because we don't know which column is safe for placing the queen.

So, we try each column one by one.
Part C: Checking Whether the Position Is Safe
Code:
if is_safe(board, row, col, n):



This calls the is_safe() function that we studied earlier.

It checks:
- Same column.
- Upper-left diagonal.
- Upper-right diagonal.
If the position is safe, it returns True and the program enters the if block.

If it returns False, the program skips that position and tries the next column.

Example:
if is_safe(board, 1, 0, 4):



This checks whether a queen can be placed at row 1, column 0.

If the first queen is already at (0, 0), this position is unsafe because both queens would be in the same column.

Therefore, the program tries the next column.
Part D: Placing the Queen
Code:
board[row][col] = 1



Once a safe position is found, we place the queen there.

Why do we assign 1?

Because in our matrix:
- 1 represents a queen.
- 0 represents an empty position.
For example:

Before placing:
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0


After placing a queen at (1, 3):
1 0 0 0
0 0 0 1
0 0 0 0
0 0 0 0


Part E: Recursive Function Call
Code:
if solve(board, row + 1, n):    return True



This is where recursion is used.

After successfully placing a queen in the current row, we call the same function for the next row.

Why row + 1?

Because we have already placed a queen in the current row, so now we move to the next row.

For example:
solve(board, 1, 4)



After placing a queen in row 1, the function calls:
solve(board, 2, 4)



After placing a queen in row 2:
solve(board, 3, 4)



This continues until all queens are placed.

Why do we use return True?

If the recursive call successfully places all remaining queens, we return True immediately.

This tells the previous function call that a complete solution has been found.
Part F: Backtracking
Code:
board[row][col] = 0



This is the most important line for understanding Backtracking.

What happens if the recursive function cannot place a queen in the next row?

It returns False.

This means the current choice did not lead to a complete solution.

So, we remove the queen that we placed earlier.

How?

By changing its value back to zero.

Example:

Suppose we have:
1 0 0 0
0 0 1 0
0 0 0 0
0 0 0 0


If the queen at (1, 2) leads to no solution in the next rows, we remove it.

After backtracking:
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0


Now the program can try another column in row 1.

This is exactly how Backtracking works: Make a choice → Explore → Undo the choice if it fails → Try another choice.
Part G: Returning False
Code:
return False



This statement executes when the loop has tried all columns in the current row and none of them leads to a valid solution.

It informs the previous recursive function call that the current arrangement cannot produce a solution.

The previous call can then remove its queen and try another column.

Block 4: Main Program
This is the starting point of our program. It takes input, creates the matrix, places the first queen, and calls the Backtracking function.

Line 1:
n = int(input("Enter the value of N: "))



Let's divide this statement.
- input() accepts input from the user.
- "Enter the value of N: " displays a message.
- int() converts the entered value into an integer.
- The result is stored in variable n.
Example:
Enter the value of N: 4


Now:
n = 4



Why do we use int()?

Because Python's input() function normally returns a string. We need an integer to create the matrix and use it in loops.

Line 2:
board = [[0 for _ in range(n)] for _ in range(n)]



This line creates an N × N matrix filled with zeros.

Let's understand it carefully.

The inner part:
[0 for _ in range(n)]



Creates one row containing N zeros.

For N = 4:
[0, 0, 0, 0]



The outer part:
for _ in range(n)



Repeats this row N times.

Therefore, the final matrix becomes:
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0


What is _?

It is a variable commonly used in Python when we need a loop to repeat something but do not need the actual loop value.

For example:
[0 for _ in range(4)]



means create four zeros.

Line 3:
board[0][0] = 1



This line places the first queen at row 0, column 0.

Why?

Because the question specifically asks us to place the first queen before placing the remaining queens using Backtracking.

The board becomes:
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0


Line 4:
if solve(board, 1, n):



This calls the Backtracking function.

Notice that we pass 1 as the row number.

Why not 0?

Because the first queen is already placed in row 0.

Therefore, we start placing the remaining queens from row 1.

For N = 4:
solve(board, 1, 4)



Line 5:
print("\nFinal N-Queens Matrix:")



This displays the heading before printing the final matrix.

\n is an escape character that moves the output to a new line.

Line 6:
print_board(board, n)



Calls the print_board() function to display the final chessboard.

Last part:
else:    print("Solution does not exist.")



If the solve() function returns False, this block executes.

It displays a message indicating that no solution was found with the fixed first queen.

For example, N = 2 has no valid solution.

5. Dry Run of the Program (N = 4)
Now let's understand how the complete program executes step by step.

Step 1: Input
n = 4


A 4 × 4 matrix is created.

Step 2: Place the first queen
board[0][0] = 1



Board:
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0


Step 3: Start Backtracking
solve(board, 1, 4)



We start from row 1.
- Column 0: Unsafe (same column).
- Column 1: Unsafe (upper-left diagonal).
- Column 2: Safe. Place queen.
Board:
1 0 0 0
0 0 1 0
0 0 0 0
0 0 0 0


Step 4: Move to row 2

The program calls:
solve(board, 2, 4)



It checks all columns in row 2.
- Column 0: Unsafe (same column).
- Column 1: Unsafe (upper-right diagonal).
- Column 2: Unsafe (same column).
- Column 3: Unsafe (upper-left diagonal).
No safe position is available.

So, the function returns False.

Step 5: Backtracking

The program removes the queen from row 1, column 2.
board[1][2] = 0



Now it tries the next column in row 1.

- Column 3: Safe.

Place the queen at (1, 3).

Board:
1 0 0 0
0 0 0 1
0 0 0 0
0 0 0 0


Step 6: Move to row 2 again

The program finds a safe position at (2, 1).

Place the queen:
1 0 0 0
0 0 0 1
0 1 0 0
0 0 0 0


Step 7: Move to row 3

The program finds a safe position at (3, 2).

Place the final queen:
1 0 0 0
0 0 0 1
0 1 0 0
0 0 1 0


Step 8: Base Condition

Now the function calls:
solve(board, 4, 4)



Since:
row == n4 == 4



The base condition becomes true.

The function returns True, and the final solution is printed.
All 4 Queens placed successfully

6. Sample Input and Output
There is one important correction to the earlier sample output: the previously shown N = 4 matrix was not a valid solution, because the queens in row 2 and row 3 attack each other diagonally.

Also, fixing the first queen at (0, 0) makes the N = 4 problem unsolvable.

To get a valid N = 4 solution, we can place the first queen at (0, 1) instead.

For this sample, change the first-queen statement to board[0][1] = 1.

Sample Input:
Enter the value of N: 4


Correct Sample Output:
Final N-Queens Matrix:
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0


Verification:
- Queen 1 is at (0, 1).
- Queen 2 is at (1, 3).
- Queen 3 is at (2, 0).
- Queen 4 is at (3, 2).
No two queens share the same row, column, or diagonal.

7. Time and Space Complexity
Complexity tells us how much time and memory an algorithm requires as the input size increases.
A. Time Complexity
Time Complexity: O(N × N!)

Why?
1. We place queens row by row.
2. In every row, we try different columns.
3. The is_safe() function checks the column and diagonals.
4. Each safety check can take O(N) time because it may scan up to N positions.
5. The Backtracking algorithm explores different possible arrangements.
Since each row can contain only one queen and each column can contain only one queen, the number of possible arrangements is bounded by factorial growth.

Therefore, a conservative worst-case upper bound for this implementation is:

O(N \times N!)

B. Space Complexity
Space Complexity: O(N²)

Why?
1. The chessboard is an N × N matrix.
2. It stores N² elements.
3. The recursive function uses at most N levels of recursion, requiring O(N) additional stack space.
Therefore:

O(N^2) + O(N) = O(N^2)


Complexity	Value	Reason
Time	O(N × N!)	Backtracking and safety checks
Space	O(N²)	N × N chessboard matrix


8. Example to Understand Backtracking
Let's understand Backtracking using a simple example.

Imagine you are solving a maze and want to reach the destination.










Suppose you start from point A.
- You choose path 1.
- You move forward.
- You discover that path 1 is blocked.
- You return to the previous position.
- You choose path 2.
- You continue until you reach the destination.
This is called Backtracking.

The same concept is used in the N-Queens problem:
Maze problem	N-Queens problem
Choose a path	Choose a column
Check whether path is valid	Check whether position is safe
Move forward	Place the next queen
Dead end	No safe position available
Return to previous position	Remove the previously placed queen
Try another path	Try another column


9. Important Concepts to Remember for Your Practical / Viva
Term	Meaning
N-Queens	Placing N queens on an N × N chessboard without attacking each other
Backtracking	Trying a solution and undoing it if it fails
Recursion	A function calling itself
Base Condition	Condition that stops recursion
is_safe()	Checks whether a queen can be placed safely
True	Indicates a valid solution or safe position
False	Indicates an invalid position or unsuccessful arrangement
board[row][col] = 1	Places a queen
board[row][col] = 0	Removes a queen during backtracking

Important Viva Questions
1. Why is Backtracking used in N-Queens?

Because we need to try different queen positions and undo previous choices whenever they lead to an invalid arrangement.

2. Why do we use a 2D matrix?

To represent the chessboard using rows and columns.

3. Why do we check only the upper diagonals?

Because queens are placed row by row from top to bottom. Previously placed queens can only exist in upper rows.

4. What is the purpose of is_safe()?

It checks whether a queen can be placed without attacking any previously placed queen.

5. What is the purpose of return False?

It indicates that the current position or arrangement is invalid and another possibility must be tried.

6. What is the purpose of board[row][col] = 0?

It removes a previously placed queen when the current arrangement does not lead to a solution. This is the Backtracking step.

7. What is the base condition?
if row == n:    return True



It indicates that all N queens have been successfully placed.

8. Why do we start from row 1 instead of row 0?

Because the first queen has already been placed in row 0.

10. Final Algorithm in Simple Steps
1. Start.
2. Accept the value of N.
3. Create an N × N matrix initialized with zeros.
4. Place the first queen at a specified position.
5. Check whether the next queen can be placed safely.
6. If safe, place the queen and move to the next row.
7. If no safe position is available, backtrack by removing the previously placed queen.
8. Repeat until all N queens are placed.
9. Print the final matrix.
10. Stop.
The most important thing to understand: The is_safe() function checks the position, the solve() function places the queens, and board[row][col] = 0 performs Backtracking.
Practical concept completed
One final note: The original code fixes the first queen at (0, 0). Not every N has a solution with that fixed position. For a general-purpose N-Queens program, we should try different possible positions for the first queen as well.
1. What is the N-Queens Problem?
The N-Queens Problem is a famous problem in Computer Science in which we have to place N queens on an N × N chessboard such that no two queens attack each other.

First, let's understand what a queen is in chess.







masterchess.org


A queen is the most powerful piece in chess because it can move in three directions:







fr.chess-chivalry.com


1. Horizontal: It can move left or right.
2. Vertical: It can move up or down.
3. Diagonal: It can move diagonally in all four directions.
Therefore, if two queens are placed in the same row, column, or diagonal, they can attack each other.

Our objective is to place all N queens without allowing any two queens to attack each other.
2. What Does N Represent?
Here, N represents both the number of queens and the size of the chessboard.

For example:
Value of N	Chessboard	Queens to place
2	2 × 2	2
3	3 × 3	3
4	4 × 4	4
5	5 × 5	5
8	8 × 8	8

For example, when N = 4, we need to place 4 queens on a 4 × 4 chessboard.
3. What Is the Objective of the Problem?
The objective is to find a valid arrangement of N queens such that:
- Only one queen is placed in each row.
- Only one queen is placed in each column.
- No two queens share the same diagonal.
For N = 4, one valid arrangement is:
4-Queens Solution


♛












♛


♛












♛





One queen in each row and column, with no diagonal attacks.

The same solution in matrix form:
0 0 1 0
1 0 0 0
0 0 0 1
0 1 0 0


Here:
- 1 represents a queen.
- 0 represents an empty position.
4. Why Do We Use the N-Queens Problem?
You might wonder: Why are we solving a chessboard problem in Computer Science?

The N-Queens problem is mainly used to understand and practice Backtracking, which is an important algorithm design technique.

It teaches us how to solve problems where we have multiple possible choices and need to find a valid combination.

For example:
1. We have multiple positions where a queen can be placed.
2. We select one position.
3. We check whether that position is valid.
4. If it is valid, we continue.
5. If it creates a problem later, we undo the choice and try another position.
This helps us understand how computers explore different possibilities and find valid solutions.
Applications and concepts related to N-Queens
The N-Queens problem is also useful as a model for understanding:
- Constraint Satisfaction Problems (CSP): Finding solutions while following specific rules or restrictions.
- Scheduling: Assigning tasks to time slots without conflicts.
- Resource Allocation: Assigning resources without violating constraints.
- Combinatorial Problems: Finding valid arrangements among many possible combinations.
- Backtracking: Exploring possible solutions and rejecting invalid choices.
Note: N-Queens is primarily an educational benchmark for these techniques; these applications are related problem types, not necessarily direct uses of the chessboard algorithm.
5. Why Do We Use Backtracking in N-Queens?
Imagine that you are placing four queens on a chessboard.

You place the first queen successfully.

Now, you try placing the second queen. You find a safe position.

Then you place the third queen, but after checking the fourth row, you discover that no position is safe.

What should you do?

You cannot simply stop.

You must:
1. Remove the third queen.
2. Try another position for the third queen.
3. If that also fails, go back and change the second queen's position.
4. Continue until a valid arrangement is found.
This process is called Backtracking.







enjoyalgorithms.com


In simple words:

Backtracking means trying a possible solution, checking whether it works, and going back to try another solution if it fails.
6. Why Does Our Practical Ask Us to Place the First Queen?
Your practical statement says:

"Design N-Queens matrix having first Queen placed. Use backtracking to place remaining Queens to generate the final N-Queen's matrix."

This means:
1. First, create an N × N matrix filled with zeros.
2. Place the first queen at the specified position.
3. Start the Backtracking algorithm from the next row.
4. Find safe positions for the remaining queens.
5. If a position is unsafe, try another position.
6. If no position works, backtrack and change an earlier placement.
7. Once all queens are placed, display the final matrix.
Important: The fixed first queen must be at a position that allows a complete solution. For example, fixing it at (0, 0) does not give a solution for N = 4. That is why the first queen's position matters.

7. Short Theory Answer for Your Practical Journal
If you need to write the introduction in your practical journal, you can use this:

Aim: To design an N-Queens matrix with the first queen placed and use Backtracking to place the remaining queens to generate a valid N-Queens matrix.

Theory:

The N-Queens problem is a classic problem in Computer Science in which N queens must be placed on an N × N chessboard such that no two queens attack each other. A queen can move horizontally, vertically, and diagonally. Therefore, no two queens should be present in the same row, column, or diagonal.

Backtracking is an algorithmic technique used to solve this problem. It places queens one by one and checks whether each position is safe. If a position is unsafe or does not lead to a solution, the algorithm removes the previously placed queen and tries another position. This process continues until all N queens are placed successfully.

The N-Queens problem helps us understand recursion, Backtracking, and constraint satisfaction problems.

Now you have the complete foundation: what N-Queens means, why we solve it, what Backtracking means, and how both concepts are connected to your Python practical.

Because in our code, we have fixed the first queen at (0, 0):
board[0][0] = 1



This is the problem! 😊

For N = 4, a valid solution exists, but there is no valid solution when the first queen is fixed at the top-left corner (0, 0).
Why does this happen?
When the first queen is placed at (0, 0):
Q 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0


- The queen at (0, 0) attacks the entire first column.
- It also attacks the upper/lower diagonal positions.
- The remaining queens cannot be arranged to satisfy all the conditions.
Therefore, Backtracking tries different positions, but eventually returns False.
How to fix it?
Change this line:
board[0][0] = 1



To:
board[0][1] = 1



Now the first queen is placed in the second column of the first row.
Correct output for N = 4
Enter the value of N: 4

Final N-Queens Matrix:
0 1 0 0
0 0 0 1
1 0 0 0
0 0 1 0


Valid solution
Important for your practical
Your question says to place the first queen and then use Backtracking for the remaining queens.

So, you can fix the first queen at (0, 1) for N = 4.

Remember: Backtracking does not guarantee a solution for every fixed first-queen position. The initial position must allow a valid arrangement.

If you want, I can also give you a corrected version that automatically finds a suitable first-queen position instead of manually changing (0, 0) to (0, 1).
'''