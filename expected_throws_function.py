#sleep4ta.py

import argparse

# use 6 instead of 2 for dice rolls
success_rate = 1.00/2
num_throws = 1.00/success_rate

def run(n: int) -> int:
    # base case
    if n == 0:
        return 0
    k = run(n-1)         # expected number of throws for n-1
    k += 1               # throw 1 add'l time as test for n
    return k*num_throws  # try num_throws times ( expected # of throws)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args()
    n = args.n
    try:
        print(run(n))
    except:
        print("Cannot be solved. TA can't sleep")
