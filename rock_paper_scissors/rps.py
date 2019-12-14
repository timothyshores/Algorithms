#!/usr/bin/python

import sys
from itertools import permutations


def rock_paper_scissors(n):
    moves = ['rock', 'paper', 'scissors']
    results = []

    if n == 0:
        return [[]]
    elif n == 1:
        for move in moves:
            results.append([move])
    elif n == 2:
        for move1 in moves:
            for move2 in moves:
                results.append([move1, move2])
    elif n == 3:
        for move1 in moves:
            for move2 in moves:
                for move3 in moves:
                    results.append([move1, move2, move3])
    elif n == 4:
        for move1 in moves:
            for move2 in moves:
                for move3 in moves:
                    for move4 in moves:
                        results.append([move1, move2, move3, move4])

    # if n == 0:
    #     answer.append(result)

    # def helper(n):
    #     print(f"Line 12 n: {n}")
    #     if n == 0:
    #         return results
    #     for result in results:
    #         results.append(plays[0])
    #         results.append(plays[1])
    #         results.append(plays[2])
    #     rock_paper_scissors(n - 1)

    # for play in plays:
    #     results.append(play)
    #     helper(n - 1)

    return results


print(rock_paper_scissors(0))
print(rock_paper_scissors(1))
print(rock_paper_scissors(2))
print(rock_paper_scissors(3))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
