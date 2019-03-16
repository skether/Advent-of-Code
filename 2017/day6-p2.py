'''
--- Day 6: Memory Reallocation ---

--- Part Two ---

Out of curiosity, the debugger would also like to know the size of the loop: starting from a state that has already been seen, how many block redistribution cycles must be performed before that same state is seen again?

In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.

How many cycles are in the infinite loop that arises from the configuration in your puzzle input?

INPUT:
0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11

ANSWER:
1695
'''

def solve(banks):
	states = []
	banks = [int(n) for n in banks.split()]
	cycle = 0
	while not banks in states:
		states.append(list(banks))
		cI = banks.index(max(banks))
		blocks = banks[cI]
		banks[cI] = 0
		while blocks != 0:
			cI += 1
			if cI >= len(banks):
				cI = 0
			banks[cI] += 1
			blocks -= 1
		cycle += 1
	loopStart = list(banks)
	cycle = 0
	while True:
		cI = banks.index(max(banks))
		blocks = banks[cI]
		banks[cI] = 0
		while blocks != 0:
			cI += 1
			if cI >= len(banks):
				cI = 0
			banks[cI] += 1
			blocks -= 1
		cycle += 1
		if banks == loopStart:
			break
	return cycle

def main():
	print(solve("0 2 7 0"))
	print(solve("0	5	10	0	11	14	13	4	11	8	8	7	1	4	12	11"))

if __name__ == '__main__':
	main()