
import heapq

def huffman_encoding(data):

    # Count frequency of each character
    freq = {}
    for char in data:
        freq[char] = freq.get(char, 0) + 1

    # Create a min heap
    heap = [[frequency, [char, ""]] for char, frequency in freq.items()]
    heapq.heapify(heap)

    # Build Huffman Tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        for pair in left[1:]:
            pair[1] = '0' + pair[1]

        for pair in right[1:]:
            pair[1] = '1' + pair[1]

        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])

    # Generate Huffman codes
    huffman_codes = dict(heap[0][1:])

    return huffman_codes


# Main program
text = input("Enter a string: ")

codes = huffman_encoding(text)

print("\nHuffman Codes:")
for char, code in codes.items():
    print(char, ":", code)

# Encode the input string
encoded = ""
for char in text:
    encoded += codes[char]

print("\nEncoded String:", encoded)


"
sample input:
Enter a string: aabbc

sample output:
Huffman Codes:
c : 00
a : 10
b : 11

Encoded String: 1010111100
7. Time and Space Complexity
Let:
- n = Total number of characters in the input string.
- k = Number of distinct characters.
Operation	Time Complexity
Frequency counting	O(n)
Creating min heap	O(k)
Building Huffman Tree	O(k log k)
Generating codes	O(k)
Encoding string	O(n)

Overall Time Complexity
O(n+k\log k)

Space Complexity:

\boxed{O(n+k)

- Frequency dictionary requires O(k).
- Min heap and Huffman codes require O(k).
- Encoded string requires O(n) space.
8. Applications of Huffman Encoding
1. File compression.
2. ZIP compression.
3. Image compression formats.
4. Data transmission.
5. Reducing storage space.
Conclusion: Huffman Encoding uses a Greedy Strategy to generate variable-length binary codes based on character frequencies. It reduces data size without losing any information.
We will cover:
1. What is Huffman Encoding?
2. What is Greedy Strategy?
3. What is a Min Heap?
4. Complete code explanation, block by block and line by line.
5. How the program executes with an example.
6. Sample input and output.
7. Time and space complexity.
8. One complete example of Huffman Encoding at the end.

1. What is Huffman Encoding?
Huffman Encoding is a lossless data compression algorithm.

Lossless means we can compress data and recover the original data without losing any information.

Suppose we have the following string:
aabbc


Here:
- a appears 2 times.
- b appears 2 times.
- c appears 1 time.
Instead of assigning every character the same number of bits, Huffman Encoding assigns:
- Shorter binary codes to frequently occurring characters.
- Longer binary codes to less frequently occurring characters.
For example:
Character	Frequency	Huffman Code
a	2	10
b	2	11
c	1	00

Therefore, the original string:
aabbc


Becomes:
1010111100


This is called Huffman Encoding.

Why do we use it?

It helps reduce the number of bits required to store or transmit data.
2. What is Greedy Strategy?
Greedy Strategy is an algorithmic technique in which we make the best possible choice at each step.

In Huffman Encoding, we always:
1. Find the two characters/nodes with the lowest frequencies.
2. Combine them into a new node.
3. Insert the new node back into the heap.
4. Repeat until only one node remains.
This is called a Greedy Approach because we select the two smallest frequencies at every step.
3. What is a Min Heap?
Before understanding the code, we need to understand a Min Heap.

A Min Heap is a data structure in which the smallest element is always available at the top.

For example:
       1
      / \
     2   3


Here, 1 is the smallest element.

In Python, we use the heapq module to implement a Min Heap.

It helps us quickly find and remove the two smallest frequencies required by Huffman Encoding.

4. Complete Python Program
This is the same program we are going to explain.
5. Code Explanation – Block by Block
Block 1: Importing the heapq module
import heapq



What is heapq?
- heapq is a built-in Python module.
- It provides functions to implement a Min Heap.
- A Min Heap always keeps the smallest element at the top.
Why do we use it?

In Huffman Encoding, we repeatedly need to find the two characters having the smallest frequencies.

Instead of manually sorting the frequencies every time, we use heapq.

For example, suppose we have:
frequencies = [5, 2, 8, 1]



After converting it into a heap:
heap = [1, 2, 8, 5]



The smallest element, 1, is at the top.

Some important heap functions:
Function	Purpose
heapq.heapify()	Converts a list into a Min Heap.
heapq.heappop()	Removes and returns the smallest element.
heapq.heappush()	Inserts a new element into the heap.

We will use all three functions in our program.

Block 2: Defining the Huffman Encoding function
def huffman_encoding(data):



Explanation:
- def is a Python keyword used to define a function.
- huffman_encoding is the name of our function.
- data is the input string provided by the user.
Why do we use a function?

A function groups related instructions together so that we can execute them whenever required.

For example:
huffman_encoding("aabbc")



Here, "aabbc" is passed to the function as data.

The function will calculate frequencies, build the Huffman structure and generate binary codes.

Block 3: Counting the frequency of each character
    freq = {}    for char in data:        freq[char] = freq.get(char, 0) + 1



This block is very important because Huffman Encoding depends on character frequencies.

Line 1:
freq = {}



- Creates an empty dictionary.
- A dictionary stores information in key-value pairs.
- Here, the character will be the key and its frequency will be the value.
Initially:
freq = {}



Line 2:
for char in data:



- for is used to repeat a statement.
- It visits every character in the input string one by one.
- Each character is temporarily stored in the variable char.
Suppose:
data = "aabbc"



The loop visits:
a → a → b → b → c


Line 3:
freq[char] = freq.get(char, 0) + 1



Let's understand this carefully.

freq.get(char, 0) means:
- Check whether the character already exists in the dictionary.
- If it exists, return its current frequency.
- If it does not exist, return 0.
Then + 1 increases its frequency by one.

For example:

Initially:
freq = {}



First character is a:
freq['a'] = 0 + 1



Dictionary becomes:
{'a': 1}



Second character is also a:
freq['a'] = 1 + 1



Dictionary becomes:
{'a': 2}



Third character is b:
freq['b'] = 0 + 1



Dictionary becomes:
{'a': 2, 'b': 1}



After processing all characters:
freq = {'a': 2, 'b': 2, 'c': 1}



Important
 This dictionary tells us how many times each character occurs in the input string.

Block 4: Creating a Min Heap
    heap = [[frequency, [char, ""]] for char, frequency in freq.items()]    heapq.heapify(heap)



This block converts our frequency dictionary into a Min Heap.

Let's understand both lines separately.

Line 1:
heap = [[frequency, [char, ""]] for char, frequency in freq.items()]



This is called a List Comprehension.

It creates a list using the dictionary values.

Let's break it down:
- freq.items() returns all key-value pairs from the dictionary.
- char stores the character.
- frequency stores its frequency.
- [frequency, [char, ""]] creates a structure containing the frequency, character and an initially empty code.
For our example:
freq = {'a': 2, 'b': 2, 'c': 1}



The heap list becomes:
[    [2, ['a', '']],    [2, ['b', '']],    [1, ['c', '']]]



Why are we using an empty string ""?

Because we have not assigned any binary codes yet.

We will generate the codes by adding 0 and 1 later.

Line 2:
heapq.heapify(heap)



- heapify() converts the list into a Min Heap.
- It arranges the elements so that the smallest frequency comes first.
Our frequencies are:
a = 2
b = 2
c = 1


The smallest frequency is 1.

Therefore, the heap will have the node containing c at the top.

Why is this required?

Because the Greedy Strategy always selects the two smallest frequencies first.

Block 5: Building the Huffman Tree
    while len(heap) > 1:        left = heapq.heappop(heap)        right = heapq.heappop(heap)



This block is the main part of the Huffman algorithm.

Line 1:
while len(heap) > 1:



- while executes a block repeatedly as long as its condition is true.
- len(heap) returns the number of elements in the heap.
- We continue until only one element remains.
Why?

Because we need to combine all characters into one final Huffman Tree.

Line 2:
left = heapq.heappop(heap)



- heappop() removes and returns the smallest element from the heap.
- We store that element in left.
Line 3:
right = heapq.heappop(heap)



- Again, heappop() removes the smallest remaining element.
- We store it in right.
Why do we take two elements?

Because Huffman Encoding combines the two nodes having the lowest frequencies at every step.

For our example:
a = 2
b = 2
c = 1


The first two selected nodes are:
left  = c (1)
right = a (2)


The two smallest frequencies have been selected.

Block 6: Assigning binary 0 to the left node
        for pair in left[1:]:            pair[1] = '0' + pair[1]



Let's understand this block.

Line 1:
for pair in left[1:]:



- left[1:] selects everything in left except the frequency.
- It accesses the character-code pairs inside the node.
- The loop processes each pair.
For example:
left = [1, ['c', '']]



Here:
left[1:]



gives:
[['c', '']]



The variable pair contains:
['c', '']



Line 2:
pair[1] = '0' + pair[1]



- pair[1] represents the binary code.
- We add 0 at the beginning of that code.
- This assigns 0 to the left branch.
Initially:
['c', '']



After execution:
['c', '0']



Why do we add 0?

In Huffman Encoding, we assign:
- Left branch = 0
- Right branch = 1
This is how binary codes are generated.

Block 7: Assigning binary 1 to the right node
        for pair in right[1:]:            pair[1] = '1' + pair[1]



This block is similar to the previous block.

Line 1:
for pair in right[1:]:



It accesses the character-code pairs of the right node, excluding its frequency.

Line 2:
pair[1] = '1' + pair[1]



- Adds 1 at the beginning of the existing code.
- This assigns 1 to the right branch.
For example:

Before:
['a', '']



After:
['a', '1']



Now our two selected nodes have:
c = 0
a = 1


Remember: These are intermediate codes. More bits may be added when their combined node is connected to another node.

Block 8: Combining the two nodes
        heapq.heappush(heap, [left[0] + right[0]] + left[1:] + right[1:])



This line combines the two selected nodes and inserts the new node back into the Min Heap.

Let's break it into three parts.

Part 1:
left[0] + right[0]



- left[0] gives the frequency of the left node.
- right[0] gives the frequency of the right node.
- We add their frequencies.
For example:
left frequency = 1
right frequency = 2


Therefore:
1 + 2 = 3


Part 2:
left[1:] + right[1:]



- left[1:] contains the character-code pairs from the left node.
- right[1:] contains the character-code pairs from the right node.
- We combine both lists.
For example:
left[1:]  = [['c', '0']]right[1:] = [['a', '1']]



Combined:
[['c', '0'], ['a', '1']]



Part 3:
heapq.heappush(heap, ...)



- heappush() inserts the newly combined node into the Min Heap.
- The heap automatically maintains its Min Heap property.
The new node becomes:
[3, ['c', '0'], ['a', '1']]



This represents a combined node with frequency 3.

Why do we push it back into the heap?

Because we need to compare this combined frequency with the remaining frequencies and continue the Greedy process.

Block 9: Generating Huffman Codes
    huffman_codes = dict(heap[0][1:])    return huffman_codes



Line 1:
huffman_codes = dict(heap[0][1:])



- Once the while loop finishes, only one node remains in the heap.
- heap[0] accesses that final node.
- [1:] excludes its frequency and selects the character-code pairs.
- dict() converts these pairs into a dictionary.
For example, the final node contains:
[5, ['b', '0'], ['c', '10'], ['a', '11']]



After conversion:
huffman_codes = {    'b': '0',    'c': '10',    'a': '11'}



Line 2:
return huffman_codes



return sends the generated Huffman codes back to the main program.

Block 10: Taking input from the user
text = input("Enter a string: ")



- input() accepts data from the user.
- The entered string is stored in the variable text.
Example:
Enter a string: aabbc


Now:
text = "aabbc"




Block 11: Calling the function
codes = huffman_encoding(text)



- Calls the huffman_encoding() function.
- Passes the user's string as an argument.
- The function calculates frequencies and generates Huffman codes.
- The returned dictionary is stored in codes.
For our example:
codes = {    'b': '0',    'c': '10',    'a': '11'}




Block 12: Displaying Huffman Codes
print("\nHuffman Codes:")for char, code in codes.items():    print(char, ":", code)



Line 1:
print("\nHuffman Codes:")



Displays the heading.

\n is used to insert a new line before the heading.

Line 2:
for char, code in codes.items():



- codes.items() returns character-code pairs.
- char stores the character.
- code stores its binary code.
- The loop visits every pair.
Line 3:
print(char, ":", code)



Displays each character and its corresponding Huffman code.

Example:
b : 0
c : 10
a : 11



Block 13: Encoding the original string
encoded = ""for char in text:    encoded += codes[char]



This block converts the original string into a binary encoded string.

Line 1:
encoded = ""



Creates an empty string to store the final encoded output.

Line 2:
for char in text:



Visits every character in the original input string.

For example:
a a b b c


Line 3:
encoded += codes[char]



- codes[char] finds the Huffman code for the current character.
- += adds that code to the existing encoded string.
For our example:
Character	Code	Encoded so far
a	11	11
a	11	1111
b	0	11110
b	0	111100
c	10	11110010

Final encoded string:
11110010



Block 14: Printing the encoded string
print("\nEncoded String:", encoded)



- Displays the heading Encoded String.
- Prints the final binary encoded string.
- \n moves the output to a new line.
For our example:
Encoded String: 11110010


6. Complete Program Execution with Example
Let's understand how the complete program works using:
aabbc


Step 1: Frequency calculation
The program counts how many times each character appears.
Character	Frequency
a	2
b	2
c	1

Step 2: Creating Min Heap
The heap contains:
c = 1
a = 2
b = 2


The smallest frequency is selected first.
Step 3: First combination
Select:
c = 1
a = 2


Combine:
1 + 2 = 3


Assign codes:
c = 0
a = 1


Remaining heap:
b = 2
Combined node = 3


Step 4: Second combination
Select:
b = 2
Combined node = 3


Combine:
2 + 3 = 5


Assign:
- b gets 0 because it is on the left.
- The combined node gets 1 because it is on the right.
Now the final codes are:
b = 0
c = 10
a = 11


Step 5: Encoding the original string
Original string:
aabbc


Replace each character with its binary code:
a = 11
a = 11
b = 0
b = 0
c = 10


Combine all the codes:
11 + 11 + 0 + 0 + 10


Final encoded string:
11110010



7. Sample Input and Output
Sample Input
Enter a string: aabbc



Sample Output
Huffman Codes:
b : 0
c : 10
a : 11

Encoded String: 11110010


Program executed successfully

Note: Huffman codes can differ when multiple characters have equal frequencies because different tie-breaking choices can produce different but equally valid codes.

8. Time Complexity
Let:
- n = Total number of characters in the input string.
- k = Number of distinct characters.
Operation	Time Complexity
Counting frequencies	O(n)
Creating Min Heap	O(k)
Building Huffman Tree	O(k log k)
Generating codes in this implementation	O(k²) worst case
Encoding the string using +=	O(n²) worst case

Overall Time Complexity:
\[
O(n+k\log k+k^2+n^2)
\]

Since \(k \leq n\), the overall worst-case complexity is:
\[
\boxed{O(n^2)}
\]

The quadratic complexity comes mainly from repeatedly concatenating immutable strings and updating code strings.
9. Space Complexity
Component	Space Complexity
Frequency dictionary	O(k)
Min Heap	O(k) references
Huffman codes	O(k²) worst case
Encoded string	O(n)

Overall Space Complexity:
\[
\boxed{O(n+k^2)}
\]


10. Example of the Huffman Encoding Concept
Let's take another example to understand the Greedy Strategy more clearly.

Suppose we have the following characters and frequencies:
Character	Frequency
A	5
B	9
C	12
D	13
E	16
F	45

Step 1: Select the two smallest frequencies.
A = 5
B = 9


Combine:
5 + 9 = 14


Step 2: Remaining frequencies:
12, 13, 14, 16, 45


Select 12 and 13.
12 + 13 = 25


Step 3: Remaining frequencies:
14, 16, 25, 45


Select 14 and 16.
14 + 16 = 30


Step 4: Remaining frequencies:
25, 30, 45


Select 25 and 30.
25 + 30 = 55


Step 5: Remaining frequencies:
45, 55


Combine:
45 + 55 = 100


The final Huffman Tree has a root frequency of 100.

What did we learn?
- Character F has the highest frequency, so it gets a shorter code.
- Character A has the lowest frequency, so it gets a longer code.
- At every step, we select the two smallest frequencies.
- This is the Greedy Strategy.

11. Important Points for Practical Examination (Viva)
Question	Answer
What is Huffman Encoding?	A lossless data compression algorithm.
Which strategy does it use?	Greedy Strategy.
Why do we use Greedy Strategy?	To repeatedly combine the two lowest frequencies.
Which data structure is used?	Min Heap.
Which Python module is used?	heapq.
What does heapify() do?	Converts a list into a Min Heap.
What does heappop() do?	Removes the smallest element.
What does heappush() do?	Inserts an element into the heap.
What is the purpose of 0 and 1?	To assign binary codes to branches.
Is Huffman Encoding lossless?	Yes.
Where is it used?	Data and file compression.

One important limitation of this program: If the input contains only one distinct character, the generated code is an empty string. A special case assigning 0 is needed to handle that input correctly.

Final conclusion: Huffman Encoding is a Greedy Algorithm that generates variable-length binary codes based on character frequencies. It gives shorter codes to frequently occurring characters and longer codes to less frequent characters, helping reduce storage and transmission requirements.

Huffman Encoding – Example, Uses and Decoding
Let's understand Huffman Encoding with a simple real-world example.
1. Why do we use Huffman Encoding?
Huffman Encoding is used for data compression.

Suppose you want to store or send a large amount of text. Normally, characters are represented using fixed-length binary codes.

For example, if we use 8-bit ASCII encoding, every character takes 8 bits.

But what if some characters occur very frequently and others occur rarely?

We can save space by:
- Giving shorter binary codes to frequently occurring characters.
- Giving longer binary codes to less frequently occurring characters.
This reduces the total number of bits required to store data.

Real-life applications:
- File compression.
- ZIP file compression techniques (Huffman coding is used in DEFLATE).
- Image and multimedia compression.
- Efficient data transmission.
2. Example of Huffman Encoding
Suppose we have the following message:
BANANA


Step 1: Calculate frequency
Character	Frequency
B	1
A	3
N	2

Step 2: Combine the two smallest frequencies

First select:
B = 1
N = 2


Combine:
1 + 2 = 3


Now we have:
A = 3
Combined node = 3


Combine them:
3 + 3 = 6


The Huffman Tree is:
Huffman Tree for BANANA
Step 3: Assign binary codes
- Left branch = 0
- Right branch = 1
Character	Frequency	Huffman Code
A	3	1
B	1	00
N	2	01

Step 4: Encode BANANA

Original message:
B A N A N A


Replace each character with its code:
B = 00
A = 1
N = 01
A = 1
N = 01
A = 1


Final encoded message:
001101011


Encoded successfully
Notice that we used only 9 bits instead of 48 bits (using 8-bit ASCII for each of the 6 characters).

Note: This is an illustrative comparison. Actual compressed file size also includes the information needed to store or transmit the Huffman codes.

3. What do we use for Decoding?
If Huffman Encoding converts normal text into binary codes, then Huffman Decoding converts the binary codes back into the original text.
Encoding	Decoding
Text → Binary	Binary → Original Text
Compression	Decompression
Uses Huffman Tree to generate codes	Uses Huffman Tree to identify characters

For decoding, we use the same Huffman Tree that was used during encoding.
4. Example of Huffman Decoding
Our encoded message was:
001101011


Our Huffman Tree has these codes:
Character	Code
B	00
A	1
N	01

Now decode the binary string from left to right.
00 | 1 | 01 | 1 | 01 | 1


Replace each binary code with its character:
B | A | N | A | N | A


Final decoded message:
ORIGINAL MESSAGE
BANANA
The original message is recovered successfully.

How does decoding work?
1. Start from the root of the Huffman Tree.
2. Read one bit at a time.
3. If the bit is 0, move left.
4. If the bit is 1, move right.
5. When you reach a leaf node, print that character.
6. Return to the root and continue until all bits are processed.

5. Python Code for Huffman Decoding
Here is a simple decoding function that works with the Huffman codes generated during encoding.
def huffman_decoding(encoded, codes):    decoded = ""    current = ""    reverse_codes = {v: k for k, v in codes.items()}    for bit in encoded:        current += bit        if current in reverse_codes:            decoded += reverse_codes[current]            current = ""    return decoded# Exampleencoded = "001101011"codes = {    'A': '1',    'B': '00',    'N': '01'}print("Decoded String:", huffman_decoding(encoded, codes))



Output:
Decoded String: BANANA



6. Important Viva Questions
Q1. Why do we use Huffman Encoding?

To compress data by assigning shorter binary codes to frequently occurring characters.

Q2. What is Huffman Decoding?

It is the process of converting an encoded binary string back into its original text.

Q3. Can we decode without the Huffman Tree?

We need the Huffman code table or the Huffman Tree to decode the data correctly. The decoder must receive or reconstruct the same coding information.

Q4. Is Huffman Encoding lossless or lossy?

It is lossless because the original data can be recovered exactly.

Q5. Why are shorter codes assigned to frequent characters?

To reduce the total number of bits required for storing or transmitting data.

Q6. What data structure is used in Huffman Encoding?

Min Heap (Priority Queue).

Q7. What is the main difference between encoding and decoding?
- Encoding: Original text → Binary code.
- Decoding: Binary code → Original text.
Remember this for your practical:

Huffman Encoding is used to compress data, whereas Huffman Decoding is used to decompress the data and recover the original message. Both use the same Huffman coding information.

'''