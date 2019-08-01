import argparse

success_rate = 1.00/6
num_throws = 1.00/success_rate

def run(n: int) -> int:
    # base case
    if n == 0:
        return 0
        
    # expected number of throws for n-1
    k = run(n-1)    
    
    # throw 1 add'l time as test for n
    k += 1

    # try num_throws times ( expected # of throws)
    return k*num_throws
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args()
    n = args.n
    try:
        print(run(n))
    except:
        print("Cannot be solved. TA can't sleep")
