# sleep4ta

import argparse

success_rate = 0.5
num_throws = 1.00/success_rate

def run(n: int) -> int:
	if n == 1:
		return 2
	k = run(n-1) 	# expected number of throws for n-1
	k = k + 1 		# because we throw 1 add'l time as test for n	
	return k*num_throws
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("n", type=int)
	args = parser.parse_args()
	n = args.n
	print(run(n))
