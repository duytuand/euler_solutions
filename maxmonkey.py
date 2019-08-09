""" PROBLEM STATEMENT

  N pirates and one monkey find themselves an island with no
food. The pirates spend the entire day gathering bananas as they
work on a raft.

  After they fall asleep, one pirate wakes up and tries to take
his even(1/N)th share of the bananas from the pile. Finding one
extra banana over an even split, he gives one to the monkey and
takes (1/N)th of the remaining pile to hide.

  After the first pirate finally falls asleep, a second pirate
wakes up and does the same. Finding one extra banana over an even
split, he gives one banana to the monkey and takes (1/N)th of the
remaining pile to hide.

  All N pirates wake up over the night, do the same thing and
every time they find one more banana than an even split, give one
to the monkey, and take (1N)th of the remaining pile.

  When all N pirates wake up, they see the diminished pile and
a fat monkey.

Q: How many bananas were in the original pile for this to occur?

"""

import argparse


class MP:
    def __init__(self, pirates: int):
        self.n = pirates

    def an_chuoi(self):
        """ Counting backwards, starting from the number of bananas """

        for k in range(1, self.n ** self.n):
            b = k * self.n  # bananas left when n-th pirate wakes
            msg = self.solve(b)
            if msg:
                print("Solution found:\n{}".format(msg))
                break

    def solve(self, b: int):
        """ iterate through all pirates, find chain of banana counts

        Parameters
        ----------
        `b` : int
            number of bananas

        """
        res, i = [], self.n
        b_now = b
        while i > 0:
            if self.count_prev(b_now):
                b_monkey = 0
            elif self.count_prev(b_now + 1):
                b_now = b_now + 1
                b_monkey = 1
            else:
                return
            b_now = self.count_prev(b_now)
            res.append("pirate #{} finds {}, monkey eats {}, hides {}"
                       .format(i, b_now, b_monkey, int(b_now / self.n)))
            i -= 1
        res.reverse()
        return '\n'.join(res)

    def count_prev(self, b: int):
        """ Count bananas when previous pirate woke
        chronologically previous

        Parameters
        ----------
        `b` : int
            number of bananas

        """
        b_prev = (b * self.n) / (self.n - 1)
        return int(b_prev) if b_prev % self.n == 0 else None


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    args = parser.parse_args()
    n = args.n
    m = MP(pirates=n)
    m.an_chuoi()
