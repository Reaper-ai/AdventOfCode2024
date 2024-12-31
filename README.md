### My Advent of Code 2024 solutions 

## Day 1 
### Part 1 : 
Simple puzzle, sorted them and took their difference
### Part 2 :
Used dictionary to find store counts of each number  

## Day 2 
### Part 1 :
Just iterated the input row by row to find all the unsafe levels 
### Part 2 :
To account for the Problem Dampener, count the number of problems in each level, if only 1 problem is found ignore it
 
## Day 3
### Part 1 :
This puzzle finally forced me learn **regex**, extracted all ```mul(x,y)``` from the input and used ```eval()``` to calculate the value
### Part 2 :
For this part used regex to find ```do```s and ```don't```s in the input and used a boolen flag to only calculate the ```mul()``` when the operation is _enabled_.  

## Day 4 
### Part 1 :
Searched for _"XMAS"_ and _"SAMX"_ separately, searched horizontailly, took transpose and used same function to search vertically, and then diagonaly
### Part 2 :
Used if else to find all configuration of the **X(cross)**

## Day 5
### Part 1 :
For each ordering, check if both pairs exist in the manual, used their index to check if they are in correct order
### Part 2 :
For this part used custom sort function to correctly order the incorrect update manauls 

## Day 6
### Part 1 :
Normally iterated to move the guard through the grid and counted the places she visited
### Part 2 :
I wasted time thinking of a clever solution, but in the end used brotue force, for every position she visited one by one replaced it with walls and then checked for cycles

## Day 7
### Part 1 :
I first tried brute force using iterative * and + and but then in reddit i saw people use recursion and use / and - , i then modified my code to do the same
### Part 2 :
A new operator, designed its inverse operator and integrated it in the part 1 code

## Day 8
### Part 1 :
For each pair of antennas, calculated the antinodes using **section formula**, if they where in-bound of the map, considered them for calculating result  
### Part 2 :
For each pair went on generating antinodes till they go out of bounds, used a ```set``` to track only unique antinodes 

## Day 9
### Part 1 :
Expanded the disk, used two pointers to compress the disk, but the disk compressed like  this ```#####.....#####``` i wasted my mind what was the problem and in the end just rearranged the result disk to get the answer maybe look back at it later 
### Part 2 :
After many failed attempts, i took help from reddit, instead solve it visually, turn each fragment into a ```node(filename, size)``` and then transverse and rearrange the files in the disk

## Day 10
### Part 1 :
Implemented a DFS to find all the hiking trails 
### Part 2 :
Just modified the DFS (removed the visited set to reuse a node multiple times to find all trails from a single start)

## Day 11
### Part 1 :
Straight forward brute force to apply all the operations according to the conditions 
### Part 2 :
As always brute force lost to time, got a hint that order does not matter as opposed to that mentioned in the puzzle, used a ```dict``` instead of a ```list``` and now my brute force is fast 

## Day 12
### Part 1 :
Used BFS to find all the regions in the grid and calculate their area and perimeter 
### Part 2 :
Another tricky puzzle, i tried to solve it so to reuse my part 1 code as much as possible, i had a idea to use ray tracing to find the sides but there are too many regions, I got a hint that _no. of sides = no. of corners_ i used this detail to count corners and compute the result

## Day 13
### Part 1 :
Just system of linear equations, had to suffer a bit due to floating points 
### Part 2 :
Just added that big number in the B matrix in the solver  

## Day 14 
### Part 1 :
At first i got confused what _teleport_ meant in the puzzle took a some time to figure that out that, i calculated new position of robot every second, it was too slow, then realized the robots just travel in a straight line in a cycle, i then just directly found their final positions  
### Part 2 :
Used statistics to find standard deviation of first 10000 configurations, and plotted the configuration with the lowest std_dev, and found the ester egg
 
## Day 15
### Part 1 :
Just moved around boxes
### Part 2 :
Now the grid is twice as big, horizontal motion is same but vertical motion is now tricky after trying BFS, DFS like algorithms and some other things, my implementation always messed up the brackets as i tried to solve visually, i then used [u/bakibol's](https://www.reddit.com/r/adventofcode/comments/1hele8m/comment/m261opg/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) implementation to use complex number, and use a single process for both horizontal and vertical motion instead of seperate functions

## Day 16
### Part 1 :
Just a modified Dijkstra search
### Part 2 :
Modified the modified Dijkstra, get distance of all points from start and end, for each point in the path check if it lies in the best path

## Day 17
### Part 1 : 
Fun puzzle, got some insight about how assemblers work
### Part 2 :
First i tried to Brute force to solution, didn't work, then i tried to see any patterns by manual I/O, did not found something to use from it, then i finally sat down to see what the program was doing and manually performing the operations and reverse engineering the assembler. but could not implement it successfully alone, thanks to [hypernetrunio](http://www.youtube.com/@hyper-neutrino) to help implement it 

## Day 18
### Part 1 :
Another modified Dijkstra
### Part 2 :
Dijkstra with binary search

## Day 19
### Part 1 :
Used recursive backtracking to find the possible combinations
### Part 2 :
Scraped part 1 and used DP to find answer for part2 and then modified it to find part 1 answer

## Day 20
### Part 1 :
At first i though reusing the previous Dijkstra to find shortest path,and identify all potential cheats in the shortest path, and iterate over them to find the result but it was too slow on the input. My second approach was to find distances of all walkable positions from the end, then running Dijkstra to find optimal path, while finding neighbors, if neighbor is a wall and its neighbor is a free space and check if the difference of distances of both the points (current node and node behind wall of current node) is enough to save 100ps in the race   
### Part 2 :
About part 2 thought it was gonna be difficult but after i saw the puzzle, i was so proud of my implementation of first half, it was so perfectly set for part 2, i just needed to write a loop to check for all cheats that saved >=100ps 

## Day 21
### Part 1 :
This was the most difficult puzzle for me, because i didn't thought that the order of button presses will change the answer, also didn't thought that ```<``` is more costly that other due to it being further away from ```A``` thanks to [u/boojum](https://www.reddit.com/r/adventofcode/comments/1hj2odw/comment/m3482ai/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button) post and the comments under it for such insights, i also didn't thought the blank space wiil be of any significance but it was, after considering it all i finally made it work 
### Part 2 :
Ahh! for part two it didn't sacle well as i was calculating the path per iteration, i tried ```numba jit, cache , pypy and multiprocessing```and their combinations, in the end I just stored all combinations in dictonairies and looked them up when needed  

## Day 22
### Part 1 :
Just Brute forced all of it to find the result, it was faster than expected  
### Part 2 :
For every sequence of 4 differences store the first price value associated with it and result is the max value in the dictonary

## Day 23
### Part 1 :
Construct the Graph in form of a adjacency list then counted all the connections as per condition
### Part 2 :
Found the largest interconnected area in the graph by recursively expanding the current known largest interconnected region 

## Day 24
### Part 1 :
Just performed the operations as given
### Part 2 :
I could not think of any code to solve it, found out it was a 45-bit *Ripple-carry adder circuit*, i solved it manually by visualization, i studied the correct adder circuit and analyzed the graph and found 6 variables right away and correctly swapped them,then changed values of x and y inputs to find the last 2 pairs as they were not found in the given input and fixed them   

## Day 25
### Part 1 :
Converted the schematics into ```numpy``` arrays and checked if they overlap or not
### Part 2 :
```**MERRY CHRISTMAS**```
