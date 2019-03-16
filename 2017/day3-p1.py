'''
--- Day 3: Spiral Memory ---

--- Part One ---

You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Your puzzle input is 277678.

INPUT:
277678

ANSWER:
475
'''

import math

def whereInSquare(num):
	squareSize = math.ceil(math.sqrt(num))
	if squareSize % 2 == 0:
		squareSize += 1
	evenSquare = (squareSize-1)**2
	col = -1
	row = -1
	if num > evenSquare:
		if num <= (evenSquare+squareSize):
			col = squareSize-1
			row = (((squareSize**2)-squareSize)+1)-num
		else:
			row = 0
			col = (squareSize**2)-num
	else:
		if num <= ((evenSquare-squareSize)+2):
			col = 0
			row = (squareSize-(((evenSquare-squareSize)+2)-num))-1
		else:
			row = squareSize-1
			col = num-((evenSquare-squareSize)+2)
	return -(row-(squareSize//2)), -(col-(squareSize//2))


def solve(num):
	return sum(abs(x) for x in whereInSquare(num))

def main():
	print(solve(1))
	print(solve(12))
	print(solve(23))
	print(solve(1024))
	print(solve(277678))

if __name__ == '__main__':
	main()