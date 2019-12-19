import random

_random_nums = [-1, 0, 1, 2, 3]
_probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]


class RandomGen(object):

    def next_num(self):
        num = random.random()
        acc_prob = 0
        num_probs = zip(_random_nums, _probabilities)

        for item, prob in num_probs:
            acc_prob += prob
            if acc_prob >= num:
                return item


if __name__ == '__main__':

    res = {
        -1: 0,
        0: 0,
        1: 0,
        2: 0,
        3: 0
    }

    rn = RandomGen()

    for i in range(0, 1000):
        k = rn.next_num()
        res[k] += 1

    for k, v in res.items():
        print("{}: {} times".format(k, v))
